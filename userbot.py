# ============================================================
# 👑 VILLAIN USERBOT - V13 FINAL - FULL MIXED - 1 FILE
# 🔥 OWNER: VILLAIN | PRANK ONLY | ERROR FREE
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

if len(SESSION) > 50:
    SESSION_OBJ = StringSession(SESSION)
else:
    SESSION_OBJ = SESSION

ALIVE_PIC_URL = "https://raw.githubusercontent.com/chaitanyatarun5-sketch/my-userbot/main/photo_2026-11-21_19-54-14.jpg"

SUDO_FILE = "sudo_users.json"
try:
    with open(SUDO_FILE) as f: SUDO_USERS = set(json.load(f))
except: SUDO_USERS = set()
def save_sudo():
    with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)
def is_owner(e): return e.outgoing or (e.sender_id == OWNER_ID) or (e.sender_id in SUDO_USERS)

START = time.time()
def uptime():
    s = int(time.time()-START); h, m = s//3600, (s%3600)//60
    return f"{h}h {m}m"

client = TelegramClient(SESSION_OBJ, API_ID, API_HASH)

async def send(e, txt):
    try:
        if e.outgoing: await e.edit(txt)
        else: await e.reply(txt)
    except:
        try: await client.send_message(e.chat_id, txt)
        except: pass

async def send_pic(e, txt):
    try: await e.reply(file=ALIVE_PIC_URL, message=txt)
    except: await send(e, txt)

async def prank_anim(e, steps):
    m = await e.reply(steps[0]) if not e.outgoing else await e.edit(steps[0])
    for s in steps[1:]:
        await asyncio.sleep(1)
        try: await m.edit(s)
        except: pass
    return m

async def need_owner(e):
    if not is_owner(e):
        await send(e, "**❌ Abeee nikal BAAP KA BOT NAHI HAI!**\n`.id` likh ke apni ID check kar, Render me OWNER_ID me wahi daal!")
        return False
    return True

# ============================================================
# 👑 SUDO
# ============================================================
@client.on(events.NewMessage(pattern=r"\.addsudo(?: |$)(.*)"))
async def addsudo(e):
    if not await need_owner(e): return
    arg = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (reply.sender_id if reply else None)
    if not uid:
        await send(e, "**❌ Use: `.addsudo 123456` Ya Reply Karke Likho!**"); return
    SUDO_USERS.add(uid); save_sudo()
    await send(e, f"**✅ AAB TU BHI TARUN KA BETA HAI!**\n**👤 ID:** `{uid}`")

@client.on(events.NewMessage(pattern=r"\.remsudo(?: |$)(.*)"))
async def remsudo(e):
    if not await need_owner(e): return
    arg = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (reply.sender_id if reply else None)
    if not uid: await send(e, "**❌ Use: `.remsudo 123456`**"); return
    SUDO_USERS.discard(uid); save_sudo()
    await send(e, f"**❌ SUDO HATA DIYA!**\n**ID:** `{uid}`")

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not await need_owner(e): return
    if not SUDO_USERS: await send(e, "**📋 SUDO LIST KHALI HAI!**")
    else:
        txt = "**👑 SUDO KINGS 👑**\n\n" + "\n".join([f"**╰┈➤** `{x}`" for x in SUDO_USERS]) + f"\n\n**Total:** {len(SUDO_USERS)}"
        await send(e, txt)

# ============================================================
# 🔥 ALIVE / HELP
# ============================================================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    txt = f"""**╔══════════════════════════╗**
**║   👑  VILLAIN IS ALIVE  👑   ║**
**╚══════════════════════════╝**

**👑 OWNER : VILLAIN**
**⚡ STATUS : ONLINE 🔥**
**💀 MODE : VILLAIN MODE ON**
**🛠️ VERSION : V13 FINAL**
**⏱️ UPTIME : {uptime()}**
**👥 SUDO : {len(SUDO_USERS)} Kings**

**🔥 SABKI FATNE WALI HAI!**
**😈 AB RAJ KAREGA VILLAIN!**"""
    await send_pic(e, txt)

@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    txt = """**👑 VILLAIN USERBOT - V13 👑**

**👑 SUDO:** `.addsudo` `.remsudo` `.sudolist`
**🎭 FUN:** `.joke` `.roast` `.shayari` `.meme` `.attitude` `.truth` `.dare` `.ship` `.slap` `.kiss` `.hug` `.pickup` `.cute` `.flirt` `.insult` `.troll` `.quote` `.fact` `.story` `.compliment`
**🎲 GAME:** `.dice` `.coin` `.luck` `.guess` `.crush` `.lovecalc` `.future` `.horoscope` `.propose` `.bff` `.love`
**✨ STYLE:** `.echo` `.shout` `.bold` `.reverse` `.font` `.bio` `.caption` `.hashtag` `.type` `.say` `.fake`
**🛠️ KAAM:** `.calc` `.weather` `.crypto` `.news` `.google` `.wiki` `.qr` `.pass` `.anime` `.songdl` `.pincode` `.yt` `.ip` `.translate`
**💻 PRANK ZONE - Sirf OWNER:**
`.hack2` `.ddos` `.trace` `.virus` `.darkweb` `.cctv` `.whatsapp` `.passwordhack` `.location` `.number` `.varius`
**👥 GROUP:** `.tagall` `.purge` `.kick` `.ban` `.unban` `.mute` `.unmute` `.promote` `.demote` `.rules`
**😈 VILLAIN:** `.jail` `.free` `.kill` `.revive` `.wanted` `.gang` `.sus` `.vs` `.top` `.mafia` `.don` `.king` `.queen`
**⚙️ BASIC:** `.alive` `.ping` `.id` `.info` `.time` `.uptime` `.profile` `.stats` `.afk` `.unafk`

**😈 AB RAJ KAREGA VILLAIN 😈**"""
    await send_pic(e, txt)

# ============================================================
# ⚙️ BASIC + FUN + GAME + STYLE + KAAM
# ============================================================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e):
    s=time.time(); await send(e, "**🏓 PING...**"); await send(e, f"**🏓 PONG!**\n**⚡ Speed:** `{int((time.time()-s)*1000)}ms`")
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r=await e.get_reply_message()
    if r: await send(e, f"**👤 ID:** `{r.sender_id}`")
    else: await send(e, f"**👤 Teri ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`")
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await send(e, f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')}\n**📅 DATE:** {datetime.datetime.now().strftime('%d %B %Y')}")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await send(e, f"**⏱️ UPTIME:** {uptime()}")
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r=await e.get_reply_message(); u=r.sender if r else await e.get_sender()
    await send(e, f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Nahi Hai'}")
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await send(e, f"**👑 PROFILE**\n**Name:** VILLAIN\n**ID:** `{e.sender_id}`\n**Status:** KING 👑")
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await send(e, f"**📊 STATS**\n**Uptime:** {uptime()}\n**Sudo:** {len(SUDO_USERS)}\n**Version:** V13")
@client.on(events.NewMessage(pattern=r"\.afk"))
async def afk(e): await send(e, "**💤 VILLAIN AFK HAI! Baad me milte hai!**")
@client.on(events.NewMessage(pattern=r"\.unafk"))
async def unafk(e): await send(e, "**🔥 VILLAIN WAPAS AA GAYA!**")

def one_cmd(pattern, replies):
    async def h(e): await send(e, random.choice(replies))
    client.on(events.NewMessage(pattern=pattern))(h)

one_cmd(r"\.joke", ["**😂 JOKE:**\nTeacher: Homework kyu nahi kiya?\nStudent: Sir, VILLAIN ne net band kar diya tha! 😂", "**😂 JOKE:**\nEk din VILLAIN ne Google se pucha - Sabse bada kaun?\nGoogle bola - Bhai tu hi hai! 😎"])
one_cmd(r"\.roast", ["**🔥 ROAST:**\nTeri shakal dekh ke mirror bhi bolta hai - Bhai mai toot jaunga! 😂", "**🔥 ROAST:**\nTu itna slow hai ki tortoise bhi overtake kar jayega! 🐢"])
one_cmd(r"\.shayari", ["**💔 SHAYARI:**\nTeri yaadon me hum itne kho gaye,\nKi VILLAIN bhi bola - Bhai tu to gaya! 💔", "**💔 SHAYARI:**\nChandni raat me chand ko dekha,\nChand bola - VILLAIN se panga mat le! 🌙"])
one_cmd(r"\.meme", ["**😂 MEME:**\nJab VILLAIN online aata hai, tab sabke phone hang ho jate hai! 📱🔥"])
one_cmd(r"\.attitude", ["**😎 ATTITUDE:**\n**Hum VILLAIN hai, hum jhukte nahi, jhukate hai!**"])
one_cmd(r"\.truth", ["**🤔 TRUTH:**\nTera sabse bada secret kya hai? Bata de! 😏"])
one_cmd(r"\.dare", ["**😈 DARE:**\nApne crush ko I Love You likh ke bhej! 😂"])
one_cmd(r"\.pickup", ["**😍 PICKUP:**\nKya tum WiFi ho? Kyunki tumse connect hone ka mann kar raha hai! 😂"])
one_cmd(r"\.cute", ["**🥰 CUTE:**\nTu itna cute hai ki VILLAIN bhi pighal gaya!"])
one_cmd(r"\.flirt", ["**😏 FLIRT:**\nTeri smile pe to VILLAIN bhi fida hai!"])
one_cmd(r"\.insult", ["**😂 INSULT:**\nBhai tu itna boring hai ki neend bhi tujhe dekh ke so jati hai!"])
one_cmd(r"\.troll", ["**😈 TROLL:**\nVILLAIN ne tujhe troll kar diya! Ab has le! 😂"])
one_cmd(r"\.quote", ["**💭 QUOTE:**\nJeetne wale alag cheez nahi karte, wo cheezo ko alag tarike se karte hai! 👑"])
one_cmd(r"\.fact", ["**🧠 FACT:**\nTera dimaag din me 70,000 khayal sochta hai!"])
one_cmd(r"\.story", ["**📖 STORY:**\nEk tha VILLAIN, jo sabka KING ban gaya! 👑"])
one_cmd(r"\.compliment", ["**✨ COMPLIMENT:**\nBhai tu aaj ek dum HERO lag raha hai! 🔥"])
one_cmd(r"\.gay", ["**🏳️‍🌈 GAY METER:**\nResult aa raha hai... 2% 😂"])
one_cmd(r"\.slap", ["**👋 SLAP!**\n**Ek dum zor se mara!**"])
one_cmd(r"\.kiss", ["**😘 KISS!**\n**Uff ye pyaar!**"])
one_cmd(r"\.hug", ["**🤗 HUG!**\n**Ek jhappi to banti hai!**"])
one_cmd(r"\.dice", [f"**🎲 DICE:** {random.randint(1,6)}"])
one_cmd(r"\.coin", ["**🪙 COIN:** HEADS 😎", "**🪙 COIN:** TAILS 🔥"])
one_cmd(r"\.guess", ["**🎯 GUESS:**\nMaine 7 socha tha, tune kya socha? 😏"])
one_cmd(r"\.crush", ["**💘 CRUSH:**\nTera crush bhi tujhe hi dekh raha hai! 👀"])
one_cmd(r"\.horoscope", ["**🔮 HOROSCOPE:**\nAaj tera lucky din hai! VILLAIN ki kasam!"])
one_cmd(r"\.propose", ["**💍 PROPOSE:**\nKya tum meri VILLAIN Queen banogi? 😍"])
one_cmd(r"\.bff", ["**👯 BFF:**\nTu aur VILLAIN - Best Friends Forever!"])
one_cmd(r"\.love", ["**❤️ LOVE:**\nPyaar me sab VILLAIN bhi hero ban jata hai!"])
one_cmd(r"\.future", ["**🔮 FUTURE:**\nTu ek din bahut bada aadmi banega, VILLAIN ki kasam! 👑"])
one_cmd(r"\.sus", ["**👀 SUS:**\nTu bada SUS lag raha hai aaj!"])
one_cmd(r"\.vs", ["**⚔️ VS:**\nVILLAIN VS DUNIYA - VILLAIN JEETEGA! 🔥"])
one_cmd(r"\.top", ["**🏆 TOP:**\nNo.1 - VILLAIN 👑"])
one_cmd(r"\.mafia", ["**😈 MAFIA:**\nVILLAIN MAFIA - Sabse khatarnak!"])
one_cmd(r"\.don", ["**👑 DON:**\nDon ka intezar to 11 mulko ki police kar rahi hai!"])
one_cmd(r"\.king", ["**👑 KING:**\nKING is BACK - VILLAIN!"])
one_cmd(r"\.queen", ["**👸 QUEEN:**\nQueen to VILLAIN ki hi hogi!"])
one_cmd(r"\.jail", ["**⛓️ JAIL ME DAAL DIYA!**\n**Ab Bahar Nahi Niklega! 😈**"])
one_cmd(r"\.free", ["**🔓 FREE HO GAYA!**\n**VILLAIN ne maaf kar diya!**"])
one_cmd(r"\.kill", ["**🔪 KILL!**\n**VILLAIN NE UDA DIYA! 💀 - PRANK HAI!**"])
one_cmd(r"\.revive", ["**💉 REVIVE!**\n**Wapas Zinda Ho Gaya!**"])
one_cmd(r"\.wanted", ["**🚨 WANTED!**\n**Inam: 10 Crore!**\n**VILLAIN ko dhoond rahe hai!**"])
one_cmd(r"\.gang", ["**😈 GANG:**\n**VILLAIN GANG - Sabse Khatarnak!**"])
one_cmd(r"\.tagall", ["**📢 TAG ALL!**\n**Sab aa jao VILLAIN bula raha hai!**"])
one_cmd(r"\.purge", ["**🧹 PURGE!**\n**Saara Kachra Saaf!**"])
one_cmd(r"\.kick", ["**🦶 KICK!**\n**Group se bahar! - Prank, Admin se hi hoga!**"])
one_cmd(r"\.ban", ["**🚫 BAN!**\n**VILLAIN ne ban kar diya! - Prank, Admin se hi hoga!**"])
one_cmd(r"\.unban", ["**✅ UNBAN!**\n**Wapas aa gaya!**"])
one_cmd(r"\.mute", ["**🔇 MUTE!**\n**Ab chup!**"])
one_cmd(r"\.unmute", ["**🔊 UNMUTE!**\n**Ab bol sakta hai!**"])
one_cmd(r"\.promote", ["**⬆️ PROMOTE!**\n**Ab tu bhi Admin!**"])
one_cmd(r"\.demote", ["**⬇️ DEMOTE!**\n**Admin se hata diya!**"])
one_cmd(r"\.rules", ["**📜 RULES:**\n1. VILLAIN ki izzat karo\n2. Bakwas mat karo\n3. Masti karo!"])
one_cmd(r"\.welcome", ["**👋 WELCOME!**\n**VILLAIN GANG me swagat hai!**"])
one_cmd(r"\.lock", ["**🔒 LOCK!**\n**Group lock ho gaya!**"])
one_cmd(r"\.unlock", ["**🔓 UNLOCK!**\n**Group khul gaya!**"])
one_cmd(r"\.news", ["**📰 NEWS:**\nVILLAIN ne phir se dhamaka kar diya! 🔥"])
one_cmd(r"\.wiki", ["**📚 WIKI:**\nGoogle pe search kar le, VILLAIN wahi milega! 😎"])
one_cmd(r"\.qr", ["**📷 QR:**\nQR banane ke liye link bhej!"])
one_cmd(r"\.pass", ["**🔑 PASS IDEA:**\n`Villain@123` - Ye strong hai, apna khud ka bana le!"])
one_cmd(r"\.pincode", ["**📍 PINCODE:**\nApna city bata, mai pincode bata dunga!"])
one_cmd(r"\.yt", ["**▶️ YT:**\nYouTube pe VILLAIN search kar!"])
one_cmd(r"\.ip", ["**🌐 IP:**\nTera IP to sirf tujhe hi pata hona chahiye! Safe reh!"])
one_cmd(r"\.translate", ["**🌍 TRANSLATE:**\nKya translate karna hai, wo bhi likh! `.translate hello`"])
one_cmd(r"\.font", ["**✨ FONT:**\n**VILLAIN** - Ye font mast hai na!"])
one_cmd(r"\.bio", ["**📝 BIO IDEA:**\n`👑 VILLAIN | 😈 King | 🔥 No Mercy`"])
one_cmd(r"\.caption", ["**📸 CAPTION:**\n`KING IS BACK 👑🔥 #VILLAIN`"])
one_cmd(r"\.hashtag", ["**#VILLAIN #KING #ATTITUDE #DON**"])
one_cmd(r"\.type", ["**⌨️ TYPE:**\nMai type kar raha hu... VILLAIN!"])
one_cmd(r"\.fake", ["**🎭 FAKE:**\nYe sab nakli hai, asli to VILLAIN hai! 😂"])
one_cmd(r"\.insta", ["**📸 INSTA:**\nInsta pe VILLAIN search kar!"])
one_cmd(r"\.imdb", ["**🎬 IMDB:**\nBest movie - VILLAIN ki kahani! 😎"])
one_cmd(r"\.play", ["**▶️ PLAY:**\nGaana baj raha hai... 🎵"])
one_cmd(r"\.screenshot", ["**📸 SCREENSHOT:**\nScreenshot le liya! 😂"])
one_cmd(r"\.sticker", ["**😀 STICKER:**\nSticker bhej diya!"])
one_cmd(r"\.vcard", ["**📇 VCARD:**\nVILLAIN - KING 👑"])
one_cmd(r"\.pdf", ["**📄 PDF:**\nPDF banane ke liye text bhej!"])
one_cmd(r"\.whois", ["**🔍 WHOIS:**\nYe domain VILLAIN ka hai! 😎"])
one_cmd(r"\.short", ["**🔗 SHORT:**\nLink chota kar diya! 😂"])

@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await send(e, f"**🍀 LUCK:** {random.randint(1,100)}%\n**Aaj Tera Din Hai Bhai!**")
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await send(e, f"**💘 LOVE CALC:** {random.randint(50,100)}%\n**Tum Dono Made For Each Other Ho!**")
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await send(e, f"**💘 SHIP:** {random.randint(1,100)}% Match!")
@client.on(events.NewMessage(pattern=r"\.calc(?: |$)(.*)"))
async def calc(e):
    q=e.pattern_match.group(1).strip()
    try:
        # safe calc - sirf number + - * / ()
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
    c=e.pattern_match.group(1) or "Indore"
    await send(e, f"**🌤️ WEATHER - {c}**\n**Temp:** {random.randint(25,35)}°C\n**Feel:** Clear Sky ☀️")
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
# 💻 PRANK ZONE - KOI ASLI HACK NAHI, SIRF ANIMATION + MAZAK
# ============================================================
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**💻 HACKING START... 10%**", "**💻 HACKING... 70%**", "**✅ HACK COMPLETE!**\n**😂 HOGAYA! COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**💥 PRANK DDOS START...**", "**💥 SERVER DOWN HO RAHA...**", "**✅ HO GAYA!**\n**😂 PRANK HAI! Koi Attack Nahi Hua!**"])
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**📍 TRACE HO RAHA HAI...**", "**📍 LOCATION MIL GAYI...**", "**😂 PRANK! Koi Trace Nahi Hua!**"])
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**🦠 VIRUS BANA RAHA HU...**", "**🦠 VIRUS INJECT HO RAHA...**", "**😂 PRANK HAI! Koi Virus Nahi Daala!**"])
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**🌑 DARKWEB OPEN HO RAHA HAI...**", "**🌑 CONNECT HO GAYA...**", "**😂 PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**📹 CCTV CAMERA DHOOND RAHA HU...**", "**📹 CAMERA MIL GAYA...**", "**📹 LIVE FEED ON...**", "**😂 SUCCESSFUL! CCTV BAAP KO BOL CHUD GAYA!**"])
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**📱 WHATSAPP CONNECT HO RAHA HAI... 25%**", "**📱 CHAT SCAN HO RAHI HAI... 60%**", "**✅ HO GAYA!**\n**😂 CHUD GAYA!**"])
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def phack(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**🔓 PASSWORD HACK HO RAHA HAI...**", "**🔓 PASSWORD CRACK HO RAHA...**", "**✅ PASSWORD: `CHUD GAYA_123` 😂**\n**UHHAAA!**"])
@client.on(events.NewMessage(pattern=r"\.location"))
async def location(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**📍 LOCATION TRACE HO RAHI HAI...**", "**📍 SATELLITE SE CONNECT...**", "**📍 LOCATION: TERE DIL ME 😍**\n**😂 !**"])
@client.on(events.NewMessage(pattern=r"\.number"))
async def number(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**📞 NUMBER TRACE HO RAHA HAI...**", "**📞 NAAM PATA HO RAHA HAI...**", "**✅ Naam: VILLAIN KA DOST 😎**\n**😂 COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.varius"))
async def varius(e):
    if not await need_owner(e): return
    await prank_anim(e, ["**🦠 VARIUS BANA RAHA HU...**", "**🦠 VARIUS INJECT HO RAHA... 50%**", "**✅ VARIUS DAAL DIYA!**\n**😂 SUCCESSFULL! Varius!**"])

print("VILLAIN V13 STARTED! 🔥")
client.start()
client.run_until_disconnected()
