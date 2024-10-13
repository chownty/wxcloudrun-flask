from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config
import os

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

# 设定数据库链接,使用 URL 编码设置数据库链接以处理特殊字符
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(
#     urllib.parse.quote(config.username),
#     urllib.parse.quote(config.password),
#     config.db_address
# )
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mysql+pymysql://{os.environ["MYSQL_USERNAME"]}:{os.environ["MYSQL_PASSWORD"]}'
    f'@{os.environ["MYSQL_ADDRESS"]}/flask_demo')

# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载控制器
from wxcloudrun import views

# 加载配置
app.config.from_object('config')
