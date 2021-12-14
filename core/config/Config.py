from app.ResourcePath.app_provider.admin.main import resource_path
from tinydb import TinyDB

# import hashlib

config_path = "Config/"
config_db_name = 'config.json'
config_table_name = 'config'
config_db_path = resource_path(config_path + config_db_name)
hasConfig = False

try:
    config_db = TinyDB(config_db_path).table(config_table_name)
    sAll = config_db.all()[0]
    hasConfig = True
except:
    sAll = []

if hasConfig:
    username = sAll["username"]
    password = sAll["password"]
    main_url = sAll["main_url"]
    open_sep = sAll["open_sep"]
    login_flag = sAll["login_flag"]
else:
    username = ""
    password = ""
    open_sep = True
    main_url = [{"host": "192.168.155.228", "port": 80, "url_add": "", "method": "post/list/"},
                {"host": "94.182.46.6", "port": 8080, "url_add": "", "method": "post/list/"}]
    login_flag = False
