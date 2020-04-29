import requests
import json
import sqlite3 as sq3
db = sq3.connect("data/data.db", check_same_thread=False)
db.row_factory = sq3.Row

def is_ok(token):
	link = requests.get("https://api.telegram.org/bot{}/getMe".format(token))
	json1 = json.loads(link.text)
	ok = json1["ok"]
	return ok
def whi(token):
	ok = is_ok(token)
	if ok == True:
		link = requests.get("https://api.telegram.org/bot{}/getMe".format(token))
		json1 = json.loads(link.text)
		first_name = json1["result"]["first_name"]
		username = json1['result']['username']
		id = json1['result']['id']
		link = requests.get("https://api.telegram.org/bot{}/getWebhookInfo".format(token))
		json1 = json.loads(link.text)
		wh_url = json1["result"]["url"]
		if wh_url == "":
			wh_url = "None"
		pending = json1["result"]["pending_update_count"]
		return first_name,username,id,wh_url,pending


def srwh(task,token,url):
	if task == "add":
		link = requests.get("https://api.telegram.org/bot{}/setwebhook?url={}".format(token,url))
	elif task == "rm":
		link = requests.get("https://api.telegram.org/bot{}/getWebhookInfo".format(token))
		json1 = json.loads(link.text)
		wh_url = json1["result"]["url"]
		link = requests.get("https://api.telegram.org/bot{}/deletewebhook?url={}".format(token,wh_url))
