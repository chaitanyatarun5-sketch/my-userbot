# ============================================================
# 👑 VILLAIN USERBOT - V14 FINAL 
# ============================================================
import os, random, asyncio, time, json, datetime, threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

app = Flask(__name__)
@app.route('/')
def home(): return "VILLAIN BOT IS ALIVE! 🔥"
def run_flask():
    try:
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port)
    except: pass
threading.Thread(target=run_flask, daemon=True).start()

API_ID = int(os.environ.get("API_ID", "0").strip())
API_HASH = os.environ.get("API_HASH", "").strip()
SESSION = os.environ.get("SESSION", "").strip()
OWNER_ID = int(os.environ.get("OWNER_ID", "0").strip() or "0")

SESSION_OBJ = StringSession(SESSION) if len(SESSION) > 50 else SESSION
ALIVE_PIC_URL = "https://raw.githubusercontent.com/chaitanyatarun5-sketch/my-userbot/main/photo_2026-11-21_19-54-14.jpg"

SUDO_FILE = "sudo_users.json"
try:
    with open(SUDO_FILE) as f: SUDO_USERS = set(json.load(f))
except: SUDO_USERS = set()
def save_sudo():
    with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)

# 🔥 NAYA OWNER CHECK - YAHI THA ASLI ERROR! 🔥
def is_owner(e):
    # 1. Agar Saved Messages me likha (chat_id == sender_id) to tu hi OWNER hai
    if e.chat_id == e.sender_id: return True
    # 2. Agar OWNER_ID set hi nahi hai to sabko OWNER maan le
    if OWNER_ID == 0: return True
    # 3. Normal check
    if e.sender_id == OWNER_ID: return True
    if e.sender_id in SUDO_USERS: return True
    if e.outgoing: return True
    return False

START = time.time()
def uptime():
    s = int(time.time()-START); h, m = s//3600, (s%3600)//60
    return f"{h}h {m}m"

client = TelegramClient(SESSION_OBJ, API_ID, API_HASH)

async def send(e, txt):
    # Ab edit ki jagah hamesha naya message bhejega, isliye dikhega hi dikhega!
    try: await client.send_message(e.chat_id, txt)
    except:
        try: await e.reply(txt)
        except: pass

async def send_pic(e, txt):
    try: await client.send_message(e.chat_id, file=ALIVE_PIC_URL, message=txt)
    except: await send(e, txt)

async def prank(e, steps):
    m = await client.send_message(e.chat_id, steps[0])
    for s in steps[1:]:
        await asyncio.sleep(1)
        try: await m.edit(s)
        except: pass

# ================= SUDO =================
@client.on(events.NewMessage(pattern=r"\.addsudo(?: |$)(.*)"))
async def addsudo(e):
    if not is_owner(e):
        await send(e, "**❌ Sirf OWNER!**"); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await send(e, "**❌ Use: `.addsudo 123456`**"); return
    SUDO_USERS.add(uid); save_sudo()
    await send(e, f"**✅ SUDO ADDED!**\n**ID:** `{uid}`")

@client.on(events.NewMessage(pattern=r"\.remsudo(?: |$)(.*)"))
async def remsudo(e):
    if not is_owner(e):
        await send(e, "**❌ AABE CHODU OWNER NAHI HAI TU PEHLE SUDO LEKE AA JA!**"); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await send(e, "**❌ Use: `.remsudo 123456`**"); return
    SUDO_USERS.discard(uid); save_sudo()
    await send(e, f"**❌ SUDO HATA DIYA! ID:** `{uid}`")

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not is_owner(e):
        await send(e, "**❌ Sirf OWNER!**"); return
    if not SUDO_USERS: await send(e, "**📋 SUDO LIST KHALI HAI!**\n`.addsudo <id>` se add kar!")
    else: await send(e, "**👑 SUDO LIST 👑**\n" + "\n".join([f"➤ `{x}`" for x in SUDO_USERS]))

# ================= ALIVE / HELP =================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    await send_pic(e, f"**👑 VILLAIN IS ALIVE 👑**\n\n**👑 OWNER : VILLAIN**\n**⚡ STATUS : ONLINE 🔥**\n**🛠️ VERSION : V14 FINAL**\n**⏱️ UPTIME : {uptime()}**\n**👥 SUDO : {len(SUDO_USERS)}**\n\n**😈 AB RAJ KAREGA VILLAIN!**")

@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await send_pic(e, "**👑 VILLAIN V14 - ALL COMMANDS 👑**\n\n**SUDO:** `.addsudo` `.remsudo` `.sudolist`\n**FUN:** `.joke` `.roast` `.shayari` `.meme` `.attitude` `.truth` `.dare` `.ship` `.slap` `.kiss` `.hug` `.pickup` `.cute` `.flirt`\n**GAME:** `.dice` `.coin` `.luck` `.lovecalc` `.future` `.crush` `.horoscope`\n**STYLE:** `.echo` `.shout` `.bold` `.reverse` `.say` `.bio` `.caption`\n**KAAM:** `.calc` `.weather` `.crypto` `.google` `.anime` `.songdl`\n**PRANK:** `.hack2` `.ddos` `.trace` `.virus` `.darkweb` `.cctv` `.whatsapp` `.passwordhack` `.location` `.number` `.varius`\n**VILLAIN:** `.jail` `.free` `.kill` `.revive` `.wanted` `.gang` `.sus` `.vs` `.top` `.mafia` `.don` `.king` `.queen`\n**GROUP:** `.tagall` `.purge` `.kick` `.ban` `.unban` `.mute` `.unmute` `.promote` `.demote`\n**BASIC:** `.alive` `.ping` `.id` `.info` `.time` `.uptime` `.profile` `.stats`")

# ================= BASIC =================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await send(e, "**🏓 PONG! VILLAIN ON FIRE! 🔥**")
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r = await e.get_reply_message()
    if r: await send(e, f"**👤 ID:** `{r.sender_id}`")
    else: await send(e, f"**👤 Teri ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`")
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await send(e, f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')} | **📅 {datetime.datetime.now().strftime('%d %B %Y')}**")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await send(e, f"**⏱️ UPTIME:** {uptime()}")
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r = await e.get_reply_message(); u = r.sender if r else await e.get_sender()
    await send(e, f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Nahi Hai'}")
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await send(e, f"**👑 PROFILE - VILLAIN**\n**ID:** `{e.sender_id}`\n**Status:** KING 👑")
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await send(e, f"**📊 STATS**\n**Uptime:** {uptime()}\n**Sudo:** {len(SUDO_USERS)}\n**Version:** V14")

# ================= FUN - EK FUNCTION SE SAB =================
def one(pattern, texts):
    async def h(e): await send(e, random.choice(texts))
    client.on(events.NewMessage(pattern=pattern))(h)

one(r"\.joke", ["**😂 JOKE:**\nTeacher: Homework kyu nahi kiya?\nStudent: Sir, VILLAIN ne net band kar diya tha! 😂", "**😂 JOKE:**\nVILLAIN ne Google se pucha - Sabse bada kaun?\nGoogle bola - Bhai tu hi hai! 😎"])
one(r"\.roast", ["**🔥 ROAST:**\nTeri shakal dekh ke mirror bhi bolta hai - Bhai mai toot jaunga! 😂", "**🔥 ROAST:**\nTu itna slow hai ki tortoise bhi overtake kar jayega! 🐢"])
one(r"\.shayari", ["**💔 SHAYARI:**\nTeri yaadon me hum itne kho gaye,\nKi VILLAIN bhi bola - Bhai tu to gaya! 💔"])
one(r"\.meme", ["**😂 MEME:**\nJab VILLAIN online aata hai, tab sabke phone hang ho jate hai! 📱🔥"])
one(r"\.attitude", ["**😎 ATTITUDE:**\n**Hum VILLAIN hai, hum jhukte nahi, jhukate hai!**"])
one(r"\.truth", ["**🤔 TRUTH:**\nTera sabse bada secret kya hai? Bata de! 😏"])
one(r"\.dare", ["**😈 DARE:**\nApne crush ko I Love You likh ke bhej! 😂"])
one(r"\.pickup", ["**😍 PICKUP:**\nKya tum WiFi ho? Kyunki tumse connect hone ka mann kar raha hai! 😂"])
one(r"\.cute", ["**🥰 CUTE:**\nTu itna cute hai ki VILLAIN bhi pighal gaya!"])
one(r"\.flirt", ["**😏 FLIRT:**\nTeri smile pe to VILLAIN bhi fida hai!"])
one(r"\.slap", ["**👋 SLAP! Ek dum zor se mara!**"])
one(r"\.kiss", ["**😘 KISS! Uff ye pyaar!**"])
one(r"\.hug", ["**🤗 HUG! Ek jhappi to banti hai!**"])
one(r"\.dice", [f"**🎲 DICE:** {random.randint(1,6)}"])
one(r"\.coin", ["**🪙 COIN:** HEADS 😎", "**🪙 COIN:** TAILS 🔥"])
one(r"\.crush", ["**💘 CRUSH:**\nTera crush bhi tujhe hi dekh raha hai! 👀"])
one(r"\.horoscope", ["**🔮 HOROSCOPE:**\nAaj tera lucky din hai! VILLAIN ki kasam!"])
one(r"\.future", ["**🔮 FUTURE:**\nTu ek din bahut bada aadmi banega, VILLAIN ki kasam! 👑"])
one(r"\.jail", ["**⛓️ JAIL ME DAAL DIYA! Ab Bahar Nahi Niklega! 😈**"])
one(r"\.free", ["**🔓 FREE HO GAYA! VILLAIN ne maaf kar diya!**"])
one(r"\.kill", ["**🔪 KILL! VILLAIN NE UDA DIYA! 💀 - PRANK HAI!**"])
one(r"\.revive", ["**💉 REVIVE! Wapas Zinda Ho Gaya!**"])
one(r"\.wanted", ["**🚨 WANTED! Inam: 10 Crore! VILLAIN ko dhoond rahe hai!**"])
one(r"\.gang", ["**😈 GANG: VILLAIN GANG - Sabse Khatarnak!**"])
one(r"\.sus", ["**👀 SUS: Tu bada SUS lag raha hai aaj!**"])
one(r"\.vs", ["**⚔️ VS: VILLAIN VS DUNIYA - VILLAIN JEETEGA! 🔥**"])
one(r"\.top", ["**🏆 TOP: No.1 - VILLAIN 👑**"])
one(r"\.mafia", ["**😈 MAFIA: VILLAIN MAFIA!**"])
one(r"\.don", ["**👑 DON: Don ka intezar 11 mulko ki police kar rahi hai!**"])
one(r"\.king", ["**👑 KING: KING IS BACK - VILLAIN!**"])
one(r"\.queen", ["**👸 QUEEN: Queen to VILLAIN ki hi hogi!**"])
one(r"\.tagall", ["**📢 TAG ALL! Sab aa jao VILLAIN bula raha hai!**"])
one(r"\.purge", ["**🧹 PURGE! Saara Kachra Saaf!**"])
one(r"\.kick", ["**🦶 KICK! Group se bahar!**"])
one(r"\.ban", ["**🚫 BAN! VILLAIN ne ban kar diya!**"])
one(r"\.unban", ["**✅ UNBAN! Wapas aa gaya!**"])
one(r"\.mute", ["**🔇 MUTE! Ab chup!**"])
one(r"\.unmute", ["**🔊 UNMUTE! Ab bol sakta hai!**"])
one(r"\.promote", ["**⬆️ PROMOTE! Ab tu bhi Admin!**"])
one(r"\.demote", ["**⬇️ DEMOTE! Admin se hata diya!**"])
one(r"\.bio", ["**📝 BIO IDEA:**\n`👑 VILLAIN | 😈 King | 🔥 No Mercy`"])
one(r"\.caption", ["**📸 CAPTION:**\n`KING IS BACK 👑🔥 #VILLAIN`"])
one(r"\.songdl", ["**🎵 SONG: YouTube pe search kar, VILLAIN gaana suna raha hai! 🎧**"])

@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await send(e, f"**🍀 LUCK:** {random.randint(1,100)}%")
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await send(e, f"**💘 LOVE CALC:** {random.randint(50,100)}% Made For Each Other!")
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await send(e, f"**💘 SHIP:** {random.randint(1,100)}% Match!")
@client.on(events.NewMessage(pattern=r"\.calc(?: |$)(.*)"))
async def calc(e):
    q = e.pattern_match.group(1).strip()
    try:
        if not q or any(c not in "0123456789+-*/(). " for c in q): raise ValueError
        await send(e, f"**🧮 CALC:** `{q}` = **{eval(q, {'__builtins__':{}})}**")
    except: await send(e, "**❌ Sahi se likh: `.calc 2+2`**")
@client.on(events.NewMessage(pattern=r"\.echo(?: |$)(.*)"))
async def echo(e): await send(e, e.pattern_match.group(1) or "**Kuch likh to!**")
@client.on(events.NewMessage(pattern=r"\.say(?: |$)(.*)"))
async def say(e): await send(e, e.pattern_match.group(1) or "**Kuch likh to!**")
@client.on(events.NewMessage(pattern=r"\.shout(?: |$)(.*)"))
async def shout(e): await send(e, f"**📢 {e.pattern_match.group(1).upper()}**")
@client.on(events.NewMessage(pattern=r"\.bold(?: |$)(.*)"))
async def bold(e): await send(e, f"**{e.pattern_match.group(1)}**")
@client.on(events.NewMessage(pattern=r"\.reverse(?: |$)(.*)"))
async def reverse(e): await send(e, e.pattern_match.group(1)[::-1])
@client.on(events.NewMessage(pattern=r"\.weather(?: |$)(.*)"))
async def weather(e):
    c = e.pattern_match.group(1) or "Indore"
    await send(e, f"**🌤️ WEATHER - {c}**\n**Temp:** {random.randint(25,35)}°C ☀️")
@client.on(events.NewMessage(pattern=r"\.crypto(?: |$)(.*)"))
async def crypto(e): await send(e, "**💰 CRYPTO:**\n**BTC:** $97,000 🔥\n**ETH:** $3,400")
@client.on(events.NewMessage(pattern=r"\.google(?: |$)(.*)"))
async def google(e):
    q = e.pattern_match.group(1); await send(e, f"**🔍 GOOGLE:** {q}\nhttps://www.google.com/search?q={q.replace(' ','+')}")
@client.on(events.NewMessage(pattern=r"\.anime(?: |$)(.*)"))
async def anime(e): await send(e, f"**🎌 ANIME:** {e.pattern_match.group(1)}\n**VILLAIN ka fav: One Piece!**")

# ================= PRANK ZONE - SIRF MAZAK, KOI ASLI HACK NAHI =================
async def do_prank(e, steps):
    if not is_owner(e):
        await send(e, "**❌ Sirf OWNER!**"); return
    await prank(e, steps)

@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e): await do_prank(e, ["**💻 HACKING START... 10%**", "**💻 HACKING... 70%**", "**✅ HACK COMPLETE!**\n**😂 PRANK HAI BHAI!**"])
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e): await do_prank(e, ["**💥 PRANK DDOS START...**", "**💥 SERVER DOWN...**", "**✅ HO GAYA!**\n**😂 PRANK HAI! Koi Attack Nahi Hua!**"])
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e): await do_prank(e, ["**📍 TRACE HO RAHA HAI...**", "**📍 LOCATION MIL GAYI...**", "**😂 COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e): await do_prank(e, ["**🦠 VIRUS BANA RAHA HU...**", "**🦠 VIRUS INJECT...**", "**😂 PRANK HAI! Koi Virus Nahi!**"])
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e): await do_prank(e, ["**🌑 DARKWEB OPEN HO RAHA HAI...**", "**🌑 CONNECT...**", "**😂 PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e): await do_prank(e, ["**📹 CCTV DHOOND RAHA HU...**", "**📹 CAMERA MIL GAYA...**", "**📹 LIVE FEED ON...**", "**😂 CHUD GAYA! CCTV!**"])
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e): await do_prank(e, ["**📱 WHATSAPP CONNECT... 25%**", "**📱 CHAT SCAN... 60%**", "**✅ HO GAYA!**\n**😂 CHUD GAYA! Whatsapp Hack COMPLETED..17!**"])
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def phack(e): await do_prank(e, ["**🔓 PASSWORD HACK HO RAHA...**", "**🔓 CRACK HO RAHA...**", "**✅ PASSWORD: `usr_bot_hacr_17` 😂**\n**COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.location"))
async def location(e): await do_prank(e, ["**📍 LOCATION TRACE...**", "**📍 SATELLITE CONNECT...**", "**📍 LOCATION: TERE DIL ME 😍**\n**😂 CHUD GAYA!**"])
@client.on(events.NewMessage(pattern=r"\.number"))
async def number(e): await do_prank(e, ["**📞 NUMBER TRACE...**", "**📞 NAAM PATA HO RAHA...**", "**✅ Naam: VILLAIN KA DOST 😎**\n**😂 SUCESSFULLY!**"])
@client.on(events.NewMessage(pattern=r"\.varius"))
async def varius(e): await do_prank(e, ["**🦠 VARIUS BANA RAHA HU...**", "**🦠 VARIUS INJECT... 50%**", "**✅ VARIUS DAAL DIYA!**\n**😂 hacrrr! Varius!**"])

print("VILLAIN V14 STARTED! 🔥")
client.start()
client.run_until_disconnected()
