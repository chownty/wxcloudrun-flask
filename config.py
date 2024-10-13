import os
from dotenv import load_dotenv
# 是否开启debug模式
DEBUG = True

# 加载.env文件中的环境变量
load_dotenv()
# 使用环境变量
username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
db_address = os.getenv("MYSQL_ADDRESS")

# 读取数据库环境变量
if username is None or password is None or db_address is None:
    print("未找到数据库环境变量，使用默认配置")
    username = os.environ.get("MYSQL_USERNAME", 'root')
    password = os.environ.get("MYSQL_PASSWORD", 'root')
    db_address = os.environ.get("MYSQL_ADDRESS", '127.0.0.1:3306')
