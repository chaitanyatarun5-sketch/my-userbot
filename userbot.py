from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
import threading, time, os

API_ID = int(os.environ.get("API_ID", "37781427"))
API_HASH = os.environ.get("API_HASH", "TERA_API_HASH")
SESSION = os.environ.get("SESSION", "TERA_SESSION")

app = Flask(__name__)
@app.route('/')
def home():
    return "Userbot Zinda Hai!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask).start()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'\.ping'))
async def ping(e):
    start = time.time()
    await e.edit("Pong! ??")
    await e.edit(f"Pong! `{round((time.time()-start)*1000)}ms`")

@client.on(events.NewMessage(pattern=r'\.alive'))
async def alive(e):
    await e.edit("**Tera Userbot Zinda Hai ?? 24x7**")

print("Userbot Chal Gaya...")
client.start()
client.run_until_disconnected()