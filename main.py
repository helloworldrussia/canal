import gspread
from db import connect
import requests
import xml.etree.ElementTree as ET


class TableSynchronizer:

    def __init__(self):
        self.conn, self.cursor = connect()

    def __del__(self):
        self.conn.close()

    def dispatcher(self):
        usd_value = self.get_usd_value()
        gs_data = self.get_gs_data()
        sql_string = "DELETE FROM api_tablebuffer;" \
                     "INSERT INTO api_tablebuffer SELECT * FROM api_table;" \
                     "DELETE FROM api_table;" \
                     + self.get_insert_string(gs_data, usd_value)
        self.perform_sql(sql_string)

    def perform_sql(self, sql_string):
        if type(sql_string) is not str:
            raise TypeError("sql_string must be str")
        self.cursor.execute(sql_string)
        self.conn.commit()

    @staticmethod
    def get_usd_value():
        response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?')
        tree = ET.fromstring(response.content)
        return float(tree.find('Valute[@ID="R01235"]/Value').text.replace(',', '.'))

    @staticmethod
    def get_insert_string(data, usd_value):
        del data[0]
        sql_string = ""
        base = "INSERT INTO api_table(id, order_id, price_usd, " \
               "delivery_date, price_rub) VALUES {};"

        for row in data:
            sql_string += f"({row[0]}, {row[1]}, {row[2]}, to_date('{row[3]}', 'DD.MM.YYYY'), " \
                          f"{round(float(row[2]) * usd_value, 2)}),"

        return base.format(sql_string)[:-2]

    @staticmethod
    def get_gs_data():
        # Указываем путь к JSON
        gc = gspread.service_account(filename='canal-353311-4c410ecaba8c.json')
        # Открываем тестовую таблицу
        sh = gc.open("test")
        gs_data = sh.sheet1.get_all_values()
        return gs_data


if __name__ == "__main__":
    synchronizer = TableSynchronizer()
    synchronizer.dispatcher()
