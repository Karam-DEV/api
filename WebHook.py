from pyrogram import *
from webhook_manage import *
from db_manage import *
app = Client("WebHook")


@app.on_message()
def echo(client, message):
	text = message.text
	chat_id = message.chat.id
	user_name = message.from_user.first_name
	user_id = message.from_user.id
	
	if Ustep(user_id,"") == None:
		adduser(user_id)
	
	token = info(user_id)["token"]
	first_name = info(user_id)["Bname"]
	username = info(user_id)["Buser"]
	id = info(user_id)["Bid"]
	url = info(user_id)["url"]
	
	step = Ustep(user_id,"")["step"]
	default_key = ReplyKeyboardMarkup(
            [
                ["• Set WeebHook ♻️", "• Delete WebHook 🗑"],
                ["• WebHook Info 📝"],
            ],
            resize_keyboard=True  # Make the keyboard smaller
        )
	cancel_key = ReplyKeyboardMarkup(
			[
				["• Cancel ❌"],
			],
			resize_keyboard=True  # Make the keyboard smaller
		)
	if text == "/start":
		app.send_message(chat_id,"•Hello {} 🍃❤\n• This Bot can Set Webhook,Remove it and git its Info 🌿🎫\n• You can use this bot by buttons bellow 🎟👇".format(user_name),reply_markup=default_key)
		Ustep(user_id,"none")
		
	if text == "• Set WeebHook ♻️":
		app.send_message(chat_id,"**• Now Send Token 📃**",reply_markup=cancel_key)
		Ustep(user_id,"ST_1")
		
	elif step == "ST_1" and text != "• Cancel ❌":
		ok = is_ok(text)
		if ok == True:
			app.send_message(chat_id,"**• Now Send URL 🖇**")
			Etoken(user_id,text)
			Ustep(user_id,"ST_2")
		else:
			app.send_message(chat_id,"**• Token is incorrect 📛**")
	elif step == "ST_2" and text != "• Cancel ❌":
		check_ssl = "https://" in text
		if check_ssl == True:
			Eurl(user_id,text)
			token = info(user_id)["token"]
			Fname,un,id,url,pending = whi(token)
			Ename(user_id,Fname)
			Euser(user_id,un)
			Eid(user_id,id)
			token = info(user_id)["token"]
			first_name = info(user_id)["Bname"]
			username = info(user_id)["Buser"]
			id = info(user_id)["Bid"]
			url = info(user_id)["url"]
			srwh("add",token,url)
			app.send_message(chat_id,"• Token : {} 🧾\n━━━━━━━━━━━━━\n• Bot Name : {} 🤖\n• Bot Username : @{} 🌀\n• Bot Id : {} 🆔\n•WebHook URL : {} 🖇\n━━━━━━━━━━━━━\n• WebHook Added Successfully ✅".format(token,first_name,username,id,url))
			Ustep(user_id,"none")
		else:
			app.send_message(chat_id,"**• URL is incorrect 🚫**")



	elif text == "• Delete WebHook 🗑":
		app.send_message(chat_id,"**• Now Send Token 📃**",reply_markup=cancel_key)
		Ustep(user_id,"Del_1")
	elif step == "Del_1" and text != "• Cancel ❌":
		ok = is_ok(text)
		if ok == True:
			Fname,un,id,url,pending = whi(text)
			Etoken(user_id,text)
			Eurl(user_id,url)
			Ename(user_id,Fname)
			Euser(user_id,un)
			Eid(user_id,id)
			token = info(user_id)["token"]
			first_name = info(user_id)["Bname"]
			username = info(user_id)["Buser"]
			id = info(user_id)["Bid"]
			url = info(user_id)["url"]
			srwh ("rm",text,"")
			app.send_message(chat_id,"• Token : {} 🧾\n━━━━━━━━━━━━━\n• Bot Name : {} 🤖\n• Bot Username : @{} 🌀\n• Bot Id : {} 🆔\n━━━━━━━━━━━━━\n• WebHook Removed Successfully ❎".format(token,first_name,username,id,url))
			Ustep(user_id,"none")
		else:
			app.send_message(chat_id,"**• Token is incorrect 📛**")



	elif text == "• WebHook Info 📝":
		app.send_message(chat_id,"**• Now Send Token 📃**",reply_markup=cancel_key)
		Ustep(user_id,"Info")


	elif step == "Info" and text != "• Cancel ❌":
		ok = is_ok(text)
		if ok == True:
			Fname,un,id,url,pending = whi(text)
			Etoken(user_id,text)
			Eurl(user_id,url)
			Ename(user_id,Fname)
			Euser(user_id,un)
			Eid(user_id,id)
			token = info(user_id)["token"]
			first_name = info(user_id)["Bname"]
			username = info(user_id)["Buser"]
			id = info(user_id)["Bid"]
			url = info(user_id)["url"]
			app.send_message(chat_id,"• Bot info 🧾\n━━━━━━━━━━━━━\n• Bot Name : {} 🤖\n• Bot username : @{} 🌀\n• Bot Id : {} 🆔\n━━━━━━━━━━━━━\n•\nWebHook URL : {}! 🖇\n• number of pending : {} 📮\n• last error : {}! 🚫".format(first_name,username,id,url,pending,"Not Found"))
			Ustep(user_id,"none")
		else:
			app.send_message(chat_id,"**• Token is incorrect 📛**")


app.run()  # Automatically start() and idle()
