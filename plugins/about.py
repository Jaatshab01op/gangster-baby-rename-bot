import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"BOT :- <a href='https://t.me/bamel_file_renamer_bot'>File Renamer</a>\nCreater :- <a href='https://t.me/Bamel_Shab'>🦋Developer🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- Private\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n ",quote=True)
