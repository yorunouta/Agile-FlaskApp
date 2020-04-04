# -*- coding: utf-8 -*-
SERVER_PORT = 8998
DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql://root:Weimiaode18@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf-8"
DEBUG = True

JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "myfood"

SEO_TITLE = "Flask构建微信订餐系统"
##过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wxd10a0b3ffef63cb9',
    'appkey':'4c32da8ef513d4b132ed1e20a7fd84c0',
    'paykey':'xxxxxxxxxxxxxx换自己的',
    'mch_id':'xxxxxxxxxxxx换自己的',
    'callback_url':'/api/order/callback'
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://0.0.0.0:8998'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}