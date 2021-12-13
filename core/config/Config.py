from app.ResourcePath.app_provider.admin.main import resource_path
import os
from tinydb import TinyDB
import hashlib

config_path = "Config/"
config_db_name = 'config.json'
config_table_name = 'config'

os.makedirs(resource_path(config_path), exist_ok=True)

config_db_path = resource_path(config_path + config_db_name)
config_db = TinyDB(config_db_path).table(config_table_name)

try:
    sAll = config_db.all()[0]
except:
    print("config not found in {link} with table {table}".format(link=config_db_path, table=config_table_name))
# sAll = ConfigTB.get(doc_id=1)

if not len(config_db):
    print(len(config_db))
    print("import Config First")

username = sAll["username"]
password = sAll["password"]
main_url = sAll["main_url"]
open_sep = sAll["open_sep"]
login_flag = sAll["login_flag"]

