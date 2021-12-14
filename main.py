from eel import chrome
import eel
from webbrowser import get, open
from os import sep
from core.config.Config import main_url, open_sep, username, password, login_flag
from core.model.ping import ping

url = {"host": "192.168.155.228", "port": 80, "url_add": "", "method": "post/list/"}

for url_in in main_url:
    if ping(url_in["host"]):
        url = url_in
        break

my_options = {
    'mode': "chrome",
    'host': url["host"],
    'port': url["port"],
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

urlT = url["host"] + ":" + str(url["port"]) + "/" + url["url_add"] + url["method"]

chrome_path = chrome.find_path()

if chrome_path is not None:
    if open_sep:
        if login_flag and username != "" and password != "":
            url_with_UP = url["url_add"] + "client/access/login/test/" + username + "/" + password + \
                          "?callBack=http://" + urlT
            eel.start(url_with_UP, suppress_error=True, block=False, options=my_options)
        else:
            print("miad inja")
            eel.start(url["url_add"] + url["method"], suppress_error=True, block=False, options=my_options)
    else:
        chrome_path = chrome_path.replace(sep, '/') + ' %s'
        get(chrome_path).open(urlT)
else:
    open(urlT)
