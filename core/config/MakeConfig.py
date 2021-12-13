from app.ResourcePath.app_provider.admin.main import resource_path
import os
from tinydb import TinyDB

config_path = "../../Config/"
config_db_name = 'config.json'
config_table_name = 'config'

developer = 1

os.makedirs(resource_path(config_path), exist_ok=True)

config_db_path = resource_path(config_path + config_db_name)
config_db = TinyDB(config_db_path)
config_db.drop_tables()
config_db = TinyDB(config_db_path).table(config_table_name)

# Start  System Config
username = "99100"
password = "123456"

config_db.insert({"username": str(username)})
config_db.update({"password": str(password)})
# end  System Config


# Start  URL Config
main_url = []
# main_url.append("http://192.168.1.4/Hafez/Monitoring_Tile/")
# main_url.append("http://192.168.1.4/Hafez/Monitoring_Tile/post/list/")
main_url.append({"host": "192.168.155.228", "port": 80, "url_add": "", "method": "post/list/"})
main_url.append({"host": "94.182.46.6", "port": 8080, "url_add": "", "method": "post/list/"})

config_db.update({"main_url": main_url})
config_db.update({"open_sep": True})
config_db.update({"login_flag": True})
# end  URL Config


print("config Create Successfully")
