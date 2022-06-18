from environs import Env

env = Env()
env.read_env()

django_secret = env.str("django_secret")

user = env.str("user")
password = env.str("password")
host = env.str("host")
port = env.int("port")
db_name = env.str("db_name")
