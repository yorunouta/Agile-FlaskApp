SERVER_PORT = 8999
SERVER_HOST = '127.0.0.1'
SQLALCHEMY_ECHO = False
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'mysql://root:Weimiaode18@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf-8"
DEBUG = True

AUTH_COOKIE_NAME = "myfood"

IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^favicon.icon"
]