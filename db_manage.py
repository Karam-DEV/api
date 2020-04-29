import sqlite3 as sq3
db = sq3.connect("data/data.db", check_same_thread=False)
db.row_factory = sq3.Row
		

def Ustep(user_id,text):
	if text == "":
		cusror = db.execute("select * from Users where id={}".format(user_id))
		for row in cusror:
			return row
	else:
		db.execute("update Users set step='{}' where id={}".format(text,user_id))
		db.commit()

def info(user_id):
	cusror = db.execute("select * from Users where id={}".format(user_id))
	for row in cusror:
		return row

def adduser(user_id):
	db.execute("insert into Users (id) values (?)",(user_id,))
	db.commit()

def Etoken(user_id,token):
	db.execute("update Users set token='{}' where id={}".format(token,user_id))
	db.commit()

def Eurl(user_id,url):
	db.execute("update Users set url='{}' where id={}".format(url,user_id))
	db.commit()

def Ename(user_id,name):
	db.execute("update Users set Bname='{}' where id={}".format(name,user_id))
	db.commit()

def Euser(user_id,username):
	db.execute("update Users set Buser='{}' where id={}".format(username,user_id))
	db.commit()

def Eid(user_id,id):
	db.execute("update Users set Bid={} where id={}".format(id,user_id))
	db.commit()
