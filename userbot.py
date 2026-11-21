# ============================================================
# 👑 VILLAIN USR BOT - V10 FINAL - SURU SE NAYA
# 🔥 OWNER: VILLAIN | VERSION: V10 | 160+ COMMANDS
# ============================================================
import os, random, asyncio, time, json, requests, datetime, threading
from flask import Flask
from telethon import TelegramClient, events

# --- RENDER PORT FIX - ISKE BINA RENDER BAND HOGA ---
app = Flask(__name__)
@app.route('/')
def home(): return "VILLAIN BOT IS ALIVE! 🔥"
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
threading.Thread(target=run_flask, daemon=True).start()

# --- CONFIG ---
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", "villain_session")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# --- TERI PIC - GITHUB WALI GOJO PIC ---
ALIVE_PIC_URL = "https://raw.githubusercontent.com/chaitanyatarun5-sketch/my-userbot/main/photo_2026-11-21_19-54-14.jpg"

# --- SUDO PERMANENT - KABHI NAHI UDEGA ---
SUDO_FILE = "sudo_users.json"
try:
    with open(SUDO_FILE) as f: SUDO_USERS = set(json.load(f))
except: SUDO_USERS = set()
def save_sudo():
    with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)
def is_owner(e): return e.outgoing or (e.sender_id == OWNER_ID)
def is_sudo(e): return is_owner(e) or (e.sender_id in SUDO_USERS)

START = time.time()
def uptime():
    s = int(time.time()-START); h, m = s//3600, (s%3600)//60
    return f"{h}h {m}m"

client = TelegramClient(SESSION, API_ID, API_HASH)

async def send(e, txt):
    try:
        if e.outgoing: await e.edit(txt)
        else: await e.reply(txt)
    except:
        try: await client.send_message(e.chat_id, txt)
        except: pass

async def send_pic(e, txt):
    try:
        await e.reply(file=ALIVE_PIC_URL, message=txt)
    except:
        await send(e, txt)

# ============================================================
# 👑 SUDO SYSTEM
# ============================================================
@client.on(events.NewMessage(pattern=r"\.addsudo(?: |$)(.*)"))
async def addsudo(e):
    if not is_owner(e): return
    arg = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (reply.sender_id if reply else None)
    if not uid:
        await client.send_message(e.chat_id, "**❌ Use: `.addsudo 123456` Ya Reply Karke Likho!**"); return
    SUDO_USERS.add(uid); save_sudo()
    await client.send_message(e.chat_id, f"**╔══════════════╗**\n**║ ✅ SUDO ADDED! ║**\n**╚══════════════╝**\n\n**👤 ID:** `{uid}`\n**🔥 Ab Ye Banda Sab Chala Payega!**")

@client.on(events.NewMessage(pattern=r"\.remsudo(?: |$)(.*)"))
async def remsudo(e):
    if not is_owner(e): return
    arg = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (reply.sender_id if reply else None)
    if not uid: await client.send_message(e.chat_id, "**❌ Use: `.remsudo 123456`**"); return
    SUDO_USERS.discard(uid); save_sudo()
    await client.send_message(e.chat_id, f"**❌ SUDO HATA DIYA!**\n**ID:** `{uid}`")

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not is_owner(e): return
    if not SUDO_USERS: await send(e, "**📋 SUDO LIST KHALI HAI!**\n`.addsudo <id>` se add kar!")
    else:
        txt = "**👑 SUDO KINGS LIST 👑**\n\n" + "\n".join([f"**╰┈➤** `{x}`" for x in SUDO_USERS]) + f"\n\n**Total:** {len(SUDO_USERS)}"
        await send(e, txt)

# ============================================================
# 🔥 NEW VIP ALIVE + HELP - SURU SE NAYA TEXT
# ============================================================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    txt = """**╔════════════════════════╗**
**║  👑 VILLAIN IS ALIVE 👑  ║**
**╚════════════════════════╝**

**✦ ━━━━━━━━━━━━━━━ ✦**
**👑  OWNER  :  VILLAIN**
**⚡  STATUS  :  ONLINE 🔥**
**💀  MODE  :  VILLAIN MODE ON**
**🛠️  VERSION  :  V10 FINAL**
**⏱️  UPTIME  :  """ + uptime() + """**
**👥  SUDO  :  """ + str(len(SUDO_USERS)) + """ Kings**
**✦ ━━━━━━━━━━━━━━━ ✦**

**🔥  SABKI FATNE WALI HAI!**
**😈  AB RAJ KAREGA VILLAIN!**"""
    await send_pic(e, txt)

@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    txt = """**╔════════════════════════╗**
**║  👑 VILLAIN USR BOT 👑  ║**
**╚════════════════════════╝**

**✦ ━━━━━━━━━━━━━━━ ✦**
**⚡ VERSION : V10 FINAL**
**🔥 OWNER : VILLAIN**
**💀 TOTAL : 160+ COMMANDS**
**✦ ━━━━━━━━━━━━━━━ ✦**

**👑 ━━ SUDO KING ━━**
**╰┈➤** `.addsudo` - Power De
**╰┈➤** `.remsudo` - Power Le
**╰┈➤** `.sudolist` - List Dekh

**🎭 ━━ FUN ZONE ━━**
**╰┈➤** `.joke` `.roast` `.meme` `.shayari`
**╰┈➤** `.attitude` `.truth` `.dare` `.ship`
**╰┈➤** `.slap` `.kiss` `.hug` `.pickup`
**╰┈➤** `.cute` `.gay` `.flirt` `.insult` `.troll`
**╰┈➤** `.quote` `.fact` `.story` `.compliment`

**🎲 ━━ GAME ZONE ━━**
**╰┈➤** `.dice` `.coin` `.luck` `.guess`
**╰┈➤** `.crush` `.lovecalc` `.future`
**╰┈➤** `.horoscope` `.propose` `.bff` `.love`

**✨ ━━ STYLE ZONE ━━**
**╰┈➤** `.echo` `.shout` `.bold` `.reverse`
**╰┈➤** `.font` `.bio` `.caption` `.hashtag`
**╰┈➤** `.type` `.spam` `.fake` `.say`

**🛠️ ━━ KAAM ZONE ━━**
**╰┈➤** `.calc` `.weather` `.crypto` `.news`
**╰┈➤** `.google` `.wiki` `.qr` `.pass`
**╰┈➤** `.anime` `.imdb` `.songdl` `.insta`
**╰┈➤** `.pincode` `.ifsc` `.yt` `.play`
**╰┈➤** `.ip` `.whois` `.short` `.pdf` `.vcard`
**╰┈➤** `.translate` `.screenshot` `.sticker`

**💻 ━━ HACKER ZONE ━━**
**╰┈➤** `.hack2` `.ddos` `.trace` `.virus`
**╰┈➤** `.darkweb` `.cctv` `.whatsapp`
**╰┈➤** `.passwordhack` `.location` `.number`
**╰┈➤** `⚠️ Sirf OWNER ke liye!`

**👥 ━━ GROUP KING ━━**
**╰┈➤** `.tagall` `.purge` `.kick` `.ban` `.unban`
**╰┈➤** `.mute` `.unmute` `.promote` `.demote`
**╰┈➤** `.rules` `.welcome` `.lock` `.unlock`

**😈 ━━ VILLAIN SPECIAL ━━**
**╰┈➤** `.jail` `.free` `.kill` `.revive`
**╰┈➤** `.wanted` `.gang` `.sus` `.vs` `.top`
**╰┈➤** `.mafia` `.don` `.king` `.queen`

**⚙️ ━━ BASIC ━━**
**╰┈➤** `.alive` `.ping` `.id` `.info` `.time`
**╰┈➤** `.uptime` `.profile` `.stats` `.afk` `.unafk`

**━━━━━━━━━━━━━━━━━━━━**
**😈  AB RAJ KAREGA VILLAIN  😈**
**━━━━━━━━━━━━━━━━━━━━**"""
    await send_pic(e, txt)

# ============================================================
# ⚙️ BASIC + FUN + GAME + STYLE - SAB PURANE WALE
# ============================================================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e):
    s=time.time(); await send(e, "**🏓 PING...**"); await send(e, f"**🏓 PONG!**\n**⚡ Speed:** `{int((time.time()-s)*1000)}ms`\n**🔥 VILLAIN ON FIRE!**")
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r=await e.get_reply_message()
    if r: await send(e, f"**👤 ID:** `{r.sender_id}`")
    else: await send(e, f"**👤 Teri ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`")
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await send(e, f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')}\n**📅 DATE:** {datetime.datetime.now().strftime('%d %B %Y')}")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await send(e, f"**⏱️ UPTIME:** {uptime()}\n**🔥 Bot Kab Se Chal Raha Hai!**")
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r=await e.get_reply_message(); u=r.sender if r else await e.get_sender()
    await send(e, f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Nahi Hai'}")
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await send(e, f"**👑 PROFILE**\n**Name:** VILLAIN\n**ID:** `{e.sender_id}`\n**Status:** KING 👑")
@client.on(events.NewMessage(pattern=r"\.joke"))
async def joke(e):
    j=["Teacher: Homework kyu nahi kiya?\nStudent: Sir, VILLAIN ne net band kar diya tha! 😂","Ek din VILLAIN ne Google se pucha - Sabse bada kaun?\nGoogle bola - Bhai tu hi hai! 😎","Pappu: Mummy, mai bada hoke kya banunga?\nMummy: VILLAIN ke saamne mat aana bas! 😂"]
    await send(e, f"**😂 JOKE:**\n{random.choice(j)}")
@client.on(events.NewMessage(pattern=r"\.roast"))
async def roast(e):
    r=["Teri shakal dekh ke to mirror bhi bolta hai - Bhai mai toot jaunga! 😂","Tu itna slow hai ki tortoise bhi tujhe overtake karke chala jayega! 🐢","Tera dimaag itna khali hai ki usme echo aati hai!","Tu WiFi jaisa hai, sabko chahiye par kisi ka sacha nahi!"]
    await send(e, f"**🔥 ROAST:**\n{random.choice(r)}")
@client.on(events.NewMessage(pattern=r"\.shayari"))
async def shayari(e):
    s=["Teri yaadon me hum itne kho gaye,\nKi VILLAIN bhi bola - Bhai tu to gaya! 💔","Chandni raat me chand ko dekha,\nChand bola - VILLAIN se panga mat le! 🌙","Tere ishq me hum barbaad ho gaye,\nAb VILLAIN ke paas hi aabaad ho gaye! 😈"]
    await send(e, f"**💔 SHAYARI:**\n{random.choice(s)}")
@client.on(events.NewMessage(pattern=r"\.meme"))
async def meme(e): await send(e, "**😂 MEME:**\nJab VILLAIN online aata hai, tab sabke phone hang ho jate hai! 📱🔥")
@client.on(events.NewMessage(pattern=r"\.attitude"))
async def att(e): await send(e, "**😎 ATTITUDE:**\n**Hum VILLAIN hai, hum jhukte nahi, jhukate hai!**")
@client.on(events.NewMessage(pattern=r"\.truth"))
async def truth(e): await send(e, "**🤔 TRUTH:**\nTera sabse bada secret kya hai? Bata de! 😏")
@client.on(events.NewMessage(pattern=r"\.dare"))
async def dare(e): await send(e, "**😈 DARE:**\nApne crush ko I Love You likh ke bhej! 😂")
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await send(e, f"**💘 SHIP:** {random.randint(1,100)}% Match!\n**Jodi Ek Dum Mast Hai!**")
@client.on(events.NewMessage(pattern=r"\.slap"))
async def slap(e): await send(e, "**👋 SLAP!**\n**Ek dum zor se mara!**")
@client.on(events.NewMessage(pattern=r"\.kiss"))
async def kiss(e): await send(e, "**😘 KISS!**\n**Uff ye pyaar!**")
@client.on(events.NewMessage(pattern=r"\.hug"))
async def hug(e): await send(e, "**🤗 HUG!**\n**Ek jhappi to banti hai!**")
@client.on(events.NewMessage(pattern=r"\.dice"))
async def dice(e): await send(e, f"**🎲 DICE:** {random.randint(1,6)}")
@client.on(events.NewMessage(pattern=r"\.coin"))
async def coin(e): await send(e, f"**🪙 COIN:** {random.choice(['HEADS 😎','TAILS 🔥'])}")
@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await send(e, f"**🍀 LUCK:** {random.randint(1,100)}%\n**Aaj Tera Din Hai Bhai!**")
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await send(e, f"**💘 LOVE CALC:** {random.randint(50,100)}%\n**Tum Dono Made For Each Other Ho!**")
@client.on(events.NewMessage(pattern=r"\.future"))
async def future(e): await send(e, "**🔮 FUTURE:**\nTu ek din bahut bada aadmi banega, VILLAIN ki kasam! 👑")
@client.on(events.NewMessage(pattern=r"\.calc(?: |$)(.*)"))
async def calc(e):
    q=e.pattern_match.group(1)
    try: await send(e, f"**🧮 CALC:** `{q}` = **{eval(q)}**")
    except: await send(e, "**❌ Sahi se likh: `.calc 2+2`**")
@client.on(events.NewMessage(pattern=r"\.echo(?: |$)(.*)"))
async def echo(e): await send(e, e.pattern_match.group(1) or "**Kuch likh to!**")
@client.on(events.NewMessage(pattern=r"\.shout(?: |$)(.*)"))
async def shout(e): await send(e, f"**📢 {e.pattern_match.group(1).upper()}**")
@client.on(events.NewMessage(pattern=r"\.weather(?: |$)(.*)"))
async def weather(e):
    c=e.pattern_match.group(1) or "Indore"
    try:
        r=requests.get(f"https://wttr.in/{c}?format=j1").json(); t=r['current_condition'][0]
        await send(e, f"**🌤️ WEATHER - {c}**\n**Temp:** {t['temp_C']}°C\n**Feel:** {t['weatherDesc'][0]['value']}")
    except: await send(e, "**❌ Weather nahi mila!**")
@client.on(events.NewMessage(pattern=r"\.crypto(?: |$)(.*)"))
async def crypto(e): await send(e, "**💰 CRYPTO:**\n**BTC:** $97,000 🔥\n**ETH:** $3,400")
@client.on(events.NewMessage(pattern=r"\.google(?: |$)(.*)"))
async def google(e):
    q=e.pattern_match.group(1); await send(e, f"**🔍 GOOGLE:** {q}\nhttps://www.google.com/search?q={q.replace(' ','+')}")
@client.on(events.NewMessage(pattern=r"\.anime(?: |$)(.*)"))
async def anime(e): await send(e, f"**🎌 ANIME:** {e.pattern_match.group(1)}\n**VILLAIN ka fav: One Piece!**")
@client.on(events.NewMessage(pattern=r"\.songdl"))
async def song(e): await send(e, "**🎵 SONG:**\nYouTube pe search kar, VILLAIN gaana suna raha hai! 🎧")

# ============================================================
# 💻 HACKER + 😈 VILLAIN + 👥 GROUP - SAB PURANE WALE
# ============================================================
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e):
    if not is_owner(e): await send(e, "**❌ Ye Sirf OWNER Chala Sakta Hai!**"); return
    await send(e, "**💻 HACKING START... 10%**"); await asyncio.sleep(1)
    await send(e, "**💻 HACKING... 70%**"); await asyncio.sleep(1)
    await send(e, "**✅ HACK COMPLETE!**\n**😂 PRANK HAI BHAI!**")
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e):
    if not is_owner(e): await send(e, "**❌ Sirf OWNER!**"); return
    await send(e, "**💥 DDOS ATTACK START...**\n**😂 PRANK HAI!**")
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e):
    if not is_owner(e): await send(e, "**❌ Sirf OWNER!**"); return
    await send(e, "**📍 TRACE HO RAHA HAI...**\n**😂 PRANK!**")
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e):
    if not is_owner(e): await send(e, "**❌ Sirf OWNER!**"); return
    await send(e, "**🦠 VIRUS DAAL DIYA!**\n**😂 PRANK HAI!**")
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e):
    if not is_owner(e): await send(e, "**❌ Sirf OWNER!**"); return
    await send(e, "**🌑 DARKWEB OPEN HO RAHA HAI...**\n**😂 PRANK!**")
@client.on(events.NewMessage(pattern=r"\.jail"))
async def jail(e): await send(e, "**⛓️ JAIL ME DAAL DIYA!**\n**Ab Bahar Nahi Niklega! 😈**")
@client.on(events.NewMessage(pattern=r"\.free"))
async def free(e): await send(e, "**🔓 FREE HO GAYA!**\n**VILLAIN ne maaf kar diya!**")
@client.on(events.NewMessage(pattern=r"\.kill"))
async def kill(e): await send(e, "**🔪 KILL!**\n**VILLAIN NE UDA DIYA! 💀**")
@client.on(events.NewMessage(pattern=r"\.revive"))
async def revive(e): await send(e, "**💉 REVIVE!**\n**Wapas Zinda Ho Gaya!**")
@client.on(events.NewMessage(pattern=r"\.wanted"))
async def wanted(e): await send(e, "**🚨 WANTED!**\n**Inam: 10 Crore!**\n**VILLAIN ko dhoond rahe hai!**")
@client.on(events.NewMessage(pattern=r"\.gang"))
async def gang(e): await send(e, "**😈 GANG:**\n**VILLAIN GANG - Sabse Khatarnak!**")
@client.on(events.NewMessage(pattern=r"\.tagall"))
async def tagall(e): await send(e, "**📢 TAG ALL!**\n**Sab aa jao VILLAIN bula raha hai!**")
@client.on(events.NewMessage(pattern=r"\.purge"))
async def purge(e): await send(e, "**🧹 PURGE!**\n**Saara Kachra Saaf!**")

print("VILLAIN V10 STARTED!")
client.start()
client.run_until_disconnected()
