import psycopg2
from config import user, password, host, port, db_name


def connect():
    conn = psycopg2.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port)
    cursor = conn.cursor()
    return conn, cursor


# def create_main_tables():
#     conn, cursor = connect()
#     sql_string = "CREATE TABLE {}(id serial, order_id serial," \
#                  "price_usd float8, price_rub float8, delivery_date date);"
#     cursor.execute(sql_string.format("main") + sql_string.format("main_buffer"))
#     conn.commit()
#     conn.close()