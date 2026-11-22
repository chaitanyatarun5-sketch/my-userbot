# ============================================================
# 👑 VILLAIN USERBOT - V15 FULL ANIMATION
# 🔥 SAB ME ANIMATION HOGA - SIMPLE KUCH NAHI BOLEGA
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

def is_owner(e):
    if e.chat_id == e.sender_id: return True
    if OWNER_ID == 0: return True
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
    try: await client.send_message(e.chat_id, txt)
    except:
        try: await e.reply(txt)
        except: pass

async def send_pic(e, txt):
    try: await client.send_message(e.chat_id, file=ALIVE_PIC_URL, message=txt)
    except: await send(e, txt)

# 🔥 YEHI HAI ANIMATION KA JADU - HAR MESSAGE EDIT HOGA! 🔥
async def anim(e, steps):
    m = await client.send_message(e.chat_id, steps[0])
    for s in steps[1:]:
        await asyncio.sleep(1.2)
        try: await m.edit(s)
        except: pass
    return m

async def anim_owner(e, steps):
    if not is_owner(e):
        await anim(e, ["**❌ CHECK HO RAHA HAI...**", "**❌ SIRF OWNER CHALA SAKTA HAI!**"])
        return
    await anim(e, steps)

# ================= SUDO =================
@client.on(events.NewMessage(pattern=r"\.addsudo(?: |$)(.*)"))
async def addsudo(e):
    if not is_owner(e): await anim(e, ["**❌ CHECK...**", "**❌ SIRF OWNER!**"]); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await anim(e, ["**❌ CHECK...**", "**❌ Use: `.addsudo 123456`**"]); return
    SUDO_USERS.add(uid); save_sudo()
    await anim(e, ["**⏳ SUDO ADD HO RAHA HAI...**", "**✅ SUDO ADDED!**", f"**👑 NEW KING!**\n**ID:** `{uid}`"])

@client.on(events.NewMessage(pattern=r"\.remsudo(?: |$)(.*)"))
async def remsudo(e):
    if not is_owner(e): await anim(e, ["**❌ CHECK...**", "**❌ SIRF OWNER!**"]); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await anim(e, ["**❌ CHECK...**", "**❌ Use: `.remsudo 123456`**"]); return
    SUDO_USERS.discard(uid); save_sudo()
    await anim(e, ["**⏳ SUDO HAT RAHA HAI...**", f"**❌ SUDO HATA DIYA! ID:** `{uid}`"])

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not is_owner(e): await anim(e, ["**❌ CHECK...**", "**❌ SIRF OWNER!**"]); return
    if not SUDO_USERS: await anim(e, ["**📋 LIST KHOL RAHA HU...**", "**📋 SUDO LIST KHALI HAI!**"])
    else: await anim(e, ["**📋 LIST KHOL RAHA HU...**", "**👑 SUDO LIST 👑**\n" + "\n".join([f"➤ `{x}`" for x in SUDO_USERS])])

# ================= ALIVE / HELP - ANIMATION WALA =================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    await anim(e, [
        "**👑 VILLAIN CHECK HO RAHA HAI...**",
        "**⚡ STATUS CHECK... ONLINE!**",
        "**🔥 VILLAIN IS ALIVE! 🔥**\n\n**👑 OWNER : VILLAIN**\n**⚡ STATUS : ONLINE**\n**🛠️ VERSION : V15 ANIMATION**\n**⏱️ UPTIME : " + uptime() + "**\n**👥 SUDO : " + str(len(SUDO_USERS)) + "**\n\n**😈 AB RAJ KAREGA VILLAIN!**"
    ])

@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await anim(e, [
        "**👑 MENU KHOL RAHA HU...**",
        "**👑 MENU KHOL RAHA HU... 50%**",
        "**👑 VILLAIN V15 - ALL COMMANDS 👑**\n\n**SUDO:** `.addsudo` `.remsudo` `.sudolist`\n**ANIMATION:** `.love` `.bomb` `.load` `.fire` `.moon` `.dance` `.rain` `.hackanim` `.heart` `.run`\n**FUN:** `.joke` `.roast` `.shayari` `.meme` `.attitude` `.truth` `.dare` `.ship` `.slap` `.kiss` `.hug` `.pickup` `.cute` `.flirt`\n**GAME:** `.dice` `.coin` `.luck` `.lovecalc` `.future` `.crush` `.horoscope`\n**STYLE:** `.echo` `.shout` `.bold` `.reverse` `.say` `.bio` `.caption`\n**KAAM:** `.calc` `.weather` `.crypto` `.google` `.anime` `.songdl`\n**PRANK:** `.hack2` `.ddos` `.trace` `.virus` `.darkweb` `.cctv` `.whatsapp` `.passwordhack` `.location` `.number` `.varius`\n**VILLAIN:** `.jail` `.free` `.kill` `.revive` `.wanted` `.gang` `.sus` `.vs` `.top` `.mafia` `.don` `.king` `.queen`\n**GROUP:** `.tagall` `.purge` `.kick` `.ban` `.unban` `.mute` `.unmute` `.promote` `.demote`\n**BASIC:** `.alive` `.ping` `.id` `.info` `.time` `.uptime` `.profile` `.stats`"
    ])

# ================= BASIC - ANIMATION =================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await anim(e, ["**🏓 PING BHEJ RAHA HU...**", "**🏓 PONG! VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r = await e.get_reply_message()
    if r: await anim(e, ["**🔍 ID DHOOND RAHA HU...**", f"**👤 ID:** `{r.sender_id}`"])
    else: await anim(e, ["**🔍 ID DHOOND RAHA HU...**", f"**👤 Teri ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`"])
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await anim(e, ["**🕐 TIME DEKH RAHA HU...**", f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')} | **📅 {datetime.datetime.now().strftime('%d %B %Y')}**"])
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await anim(e, ["**⏱️ UPTIME CHECK...**", f"**⏱️ UPTIME:** {uptime()}"])
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r = await e.get_reply_message(); u = r.sender if r else await e.get_sender()
    await anim(e, ["**🔍 INFO NIKAL RAHA HU...**", f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Nahi Hai'}"])
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await anim(e, ["**👑 PROFILE KHOL RAHA HU...**", f"**👑 PROFILE - VILLAIN**\n**ID:** `{e.sender_id}`\n**Status:** KING 👑"])
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await anim(e, ["**📊 STATS LOAD HO RAHE HAI...**", f"**📊 STATS**\n**Uptime:** {uptime()}\n**Sudo:** {len(SUDO_USERS)}\n**Version:** V15"])

# ================= FUN - SAB ANIMATION =================
def anim_one(pattern, steps_list):
    async def h(e): await anim(e, steps_list)
    client.on(events.NewMessage(pattern=pattern))(h)

anim_one(r"\.joke", ["**😂 JOKE SOCH RAHA HU...**", "**😂 JOKE MIL GAYA!**", "**😂 JOKE:**\nTeacher: Homework kyu nahi kiya?\nStudent: Sir, VILLAIN ne net band kar diya tha! 😂"])
anim_one(r"\.roast", ["**🔥 ROAST BANA RAHA HU...**", "**🔥 ROAST READY!**", "**🔥 ROAST:**\nTeri shakal dekh ke mirror bhi bolta hai - Bhai mai toot jaunga! 😂"])
anim_one(r"\.shayari", ["**💔 SHAYARI LIKH RAHA HU...**", "**💔 SHAYARI:**\nTeri yaadon me hum itne kho gaye,\nKi VILLAIN bhi bola - Bhai tu to gaya! 💔"])
anim_one(r"\.meme", ["**😂 MEME DHOOND RAHA HU...**", "**😂 MEME:**\nJab VILLAIN online aata hai, tab sabke phone hang ho jate hai! 📱🔥"])
anim_one(r"\.attitude", ["**😎 ATTITUDE LOAD HO RAHA HAI...**", "**😎 ATTITUDE:**\n**Hum VILLAIN hai, hum jhukte nahi, jhukate hai!**"])
anim_one(r"\.truth", ["**🤔 TRUTH SOCH RAHA HU...**", "**🤔 TRUTH:**\nTera sabse bada secret kya hai? Bata de! 😏"])
anim_one(r"\.dare", ["**😈 DARE SOCH RAHA HU...**", "**😈 DARE:**\nApne crush ko I Love You likh ke bhej! 😂"])
anim_one(r"\.pickup", ["**😍 PICKUP LINE SOCH RAHA HU...**", "**😍 PICKUP:**\nKya tum WiFi ho? Kyunki tumse connect hone ka mann kar raha hai! 😂"])
anim_one(r"\.cute", ["**🥰 CHECK HO RAHA HAI...**", "**🥰 CUTE:**\nTu itna cute hai ki VILLAIN bhi pighal gaya!"])
anim_one(r"\.flirt", ["**😏 FLIRT MODE ON...**", "**😏 FLIRT:**\nTeri smile pe to VILLAIN bhi fida hai!"])
anim_one(r"\.slap", ["**👋 HAATH UTHA RAHA HU...**", "**👋 SLAP! Ek dum zor se mara!**"])
anim_one(r"\.kiss", ["**😘 PAAS AA RAHA HU...**", "**😘 KISS! Uff ye pyaar!**"])
anim_one(r"\.hug", ["**🤗 BAAHE FAILA RAHA HU...**", "**🤗 HUG! Ek jhappi to banti hai!**"])
anim_one(r"\.dice", ["**🎲 DICE GHUMA RAHA HU...**", f"**🎲 DICE:** {random.randint(1,6)}"])
anim_one(r"\.coin", ["**🪙 COIN UCHAL RAHA HU...**", "**🪙 COIN:** HEADS 😎"])
anim_one(r"\.crush", ["**💘 CRUSH CHECK HO RAHA HAI...**", "**💘 CRUSH:**\nTera crush bhi tujhe hi dekh raha hai! 👀"])
anim_one(r"\.horoscope", ["**🔮 TARE DEKH RAHA HU...**", "**🔮 HOROSCOPE:**\nAaj tera lucky din hai! VILLAIN ki kasam!"])
anim_one(r"\.future", ["**🔮 FUTURE DEKH RAHA HU...**", "**🔮 FUTURE:**\nTu ek din bahut bada aadmi banega, VILLAIN ki kasam! 👑"])
anim_one(r"\.jail", ["**⛓️ PAKAD RAHA HU...**", "**⛓️ JAIL ME DAAL DIYA! Ab Bahar Nahi Niklega! 😈**"])
anim_one(r"\.free", ["**🔓 CHABI DHOOND RAHA HU...**", "**🔓 FREE HO GAYA! VILLAIN ne maaf kar diya!**"])
anim_one(r"\.kill", ["**🔪 NISHANA LAGA RAHA HU...**", "**🔪 KILL! VILLAIN NE UDA DIYA! 💀 - PRANK HAI!**"])
anim_one(r"\.revive", ["**💉 INJECTION LAGA RAHA HU...**", "**💉 REVIVE! Wapas Zinda Ho Gaya!**"])
anim_one(r"\.wanted", ["**🚨 POSTER BANA RAHA HU...**", "**🚨 WANTED! Inam: 10 Crore! VILLAIN ko dhoond rahe hai!**"])
anim_one(r"\.gang", ["**😈 GANG BULA RAHA HU...**", "**😈 GANG: VILLAIN GANG - Sabse Khatarnak!**"])
anim_one(r"\.sus", ["**👀 CHECK HO RAHA HAI...**", "**👀 SUS: Tu bada SUS lag raha hai aaj!**"])
anim_one(r"\.vs", ["**⚔️ LADAI SHURU...**", "**⚔️ VS: VILLAIN VS DUNIYA - VILLAIN JEETEGA! 🔥**"])
anim_one(r"\.top", ["**🏆 LIST BANA RAHA HU...**", "**🏆 TOP: No.1 - VILLAIN 👑**"])
anim_one(r"\.mafia", ["**😈 MAFIA AA RAHI HAI...**", "**😈 MAFIA: VILLAIN MAFIA!**"])
anim_one(r"\.don", ["**👑 DON AA RAHA HAI...**", "**👑 DON: Don ka intezar 11 mulko ki police kar rahi hai!**"])
anim_one(r"\.king", ["**👑 TAAJ PEHNA RAHA HU...**", "**👑 KING: KING IS BACK - VILLAIN!**"])
anim_one(r"\.queen", ["**👸 QUEEN AA RAHI HAI...**", "**👸 QUEEN: Queen to VILLAIN ki hi hogi!**"])
anim_one(r"\.tagall", ["**📢 SABKO BULA RAHA HU...**", "**📢 TAG ALL! Sab aa jao VILLAIN bula raha hai!**"])
anim_one(r"\.purge", ["**🧹 JHAADU LAGA RAHA HU...**", "**🧹 PURGE! Saara Kachra Saaf!**"])
anim_one(r"\.kick", ["**🦶 LAAT MAAR RAHA HU...**", "**🦶 KICK! Group se bahar!**"])
anim_one(r"\.ban", ["**🚫 BAN KAR RAHA HU...**", "**🚫 BAN! VILLAIN ne ban kar diya!**"])
anim_one(r"\.unban", ["**✅ WAPAS LA RAHA HU...**", "**✅ UNBAN! Wapas aa gaya!**"])
anim_one(r"\.mute", ["**🔇 CHUP KARA RAHA HU...**", "**🔇 MUTE! Ab chup!**"])
anim_one(r"\.unmute", ["**🔊 BOLNE DE RAHA HU...**", "**🔊 UNMUTE! Ab bol sakta hai!**"])
anim_one(r"\.promote", ["**⬆️ UPAR CHADHA RAHA HU...**", "**⬆️ PROMOTE! Ab tu bhi Admin!**"])
anim_one(r"\.demote", ["**⬇️ NEECHE UTAR RAHA HU...**", "**⬇️ DEMOTE! Admin se hata diya!**"])
anim_one(r"\.bio", ["**📝 BIO SOCH RAHA HU...**", "**📝 BIO IDEA:**\n`👑 VILLAIN | 😈 King | 🔥 No Mercy`"])
anim_one(r"\.caption", ["**📸 CAPTION SOCH RAHA HU...**", "**📸 CAPTION:**\n`KING IS BACK 👑🔥 #VILLAIN`"])
anim_one(r"\.songdl", ["**🎵 GAANA DHOOND RAHA HU...**", "**🎵 SONG: YouTube pe search kar, VILLAIN gaana suna raha hai! 🎧**"])

@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await anim(e, ["**🍀 LUCK CHECK HO RAHA HAI...**", f"**🍀 LUCK:** {random.randint(1,100)}%"])
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await anim(e, ["**💘 LOVE NAP RAHA HU...**", "**💘 LOVE NAP RAHA HU... 50%**", f"**💘 LOVE CALC:** {random.randint(50,100)}% Made For Each Other!"])
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await anim(e, ["**💘 SHIP BANA RAHA HU...**", f"**💘 SHIP:** {random.randint(1,100)}% Match!"])
@client.on(events.NewMessage(pattern=r"\.calc(?: |$)(.*)"))
async def calc(e):
    q = e.pattern_match.group(1).strip()
    try:
        if not q or any(c not in "0123456789+-*/(). " for c in q): raise ValueError
        await anim(e, ["**🧮 CALC HO RAHA HAI...**", f"**🧮 CALC:** `{q}` = **{eval(q, {'__builtins__':{}})}**"])
    except: await anim(e, ["**❌ CHECK...**", "**❌ Sahi se likh: `.calc 2+2`**"])
@client.on(events.NewMessage(pattern=r"\.echo(?: |$)(.*)"))
async def echo(e): await anim(e, ["**📢 SUN RAHA HU...**", e.pattern_match.group(1) or "**Kuch likh to!**"])
@client.on(events.NewMessage(pattern=r"\.say(?: |$)(.*)"))
async def say(e): await anim(e, ["**🗣️ BOL RAHA HU...**", e.pattern_match.group(1) or "**Kuch likh to!**"])
@client.on(events.NewMessage(pattern=r"\.shout(?: |$)(.*)"))
async def shout(e): await anim(e, ["**📢 CHILLA RAHA HU...**", f"**📢 {e.pattern_match.group(1).upper()}**"])
@client.on(events.NewMessage(pattern=r"\.bold(?: |$)(.*)"))
async def bold(e): await anim(e, ["**✨ BOLD KAR RAHA HU...**", f"**{e.pattern_match.group(1)}**"])
@client.on(events.NewMessage(pattern=r"\.reverse(?: |$)(.*)"))
async def reverse(e): await anim(e, ["**🔄 ULTA KAR RAHA HU...**", e.pattern_match.group(1)[::-1]])
@client.on(events.NewMessage(pattern=r"\.weather(?: |$)(.*)"))
async def weather(e):
    c = e.pattern_match.group(1) or "Indore"
    await anim(e, ["**🌤️ MAUSAM DEKH RAHA HU...**", f"**🌤️ WEATHER - {c}**\n**Temp:** {random.randint(25,35)}°C ☀️"])
@client.on(events.NewMessage(pattern=r"\.crypto(?: |$)(.*)"))
async def crypto(e): await anim(e, ["**💰 RATE CHECK HO RAHA HAI...**", "**💰 CRYPTO:**\n**BTC:** $97,000 🔥\n**ETH:** $3,400"])
@client.on(events.NewMessage(pattern=r"\.google(?: |$)(.*)"))
async def google(e):
    q = e.pattern_match.group(1); await anim(e, ["**🔍 GOOGLE KAR RAHA HU...**", f"**🔍 GOOGLE:** {q}\nhttps://www.google.com/search?q={q.replace(' ','+')}"])
@client.on(events.NewMessage(pattern=r"\.anime(?: |$)(.*)"))
async def anime(e): await anim(e, ["**🎌 ANIME DHOOND RAHA HU...**", f"**🎌 ANIME:** {e.pattern_match.group(1)}\n**VILLAIN ka fav: One Piece!**"])

# ================= ANIMATION SPECIAL =================
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await anim(e, ["**🤍 DIL KHALI HAI...**", "**💛 DIL BHAR RAHA HAI...**", "**🧡 DIL DHADAK RAHA HAI...**", "**❤️ DIL BHAR GAYA!**", "**❤️❤️❤️ I LOVE YOU ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.heart"))
async def heart(e): await anim(e, ["**🤍**", "**🤍💛**", "**🤍💛🧡**", "**🤍💛🧡❤️**", "**❤️❤️❤️ DIL SE DIL TAK ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.bomb"))
async def bomb(e): await anim(e, ["**💣 BOMB LAG GAYA! BHAG!**", "**💣 5...**", "**💣 4...**", "**💣 3...**", "**💣 2...**", "**💣 1...**", "**💥💥 BOOM! 💥💥**\n**😂 UD GAYA! BOOOMMBB!**"])
@client.on(events.NewMessage(pattern=r"\.hackanim"))
async def hackanim(e): await anim(e, ["**💻 HACKING START...**\n**[□□□□□□□□□□] 0%**", "**💻 PASSWORD TOD RAHA HU...**\n**[███□□□□□□□] 30%**", "**💻 FIREWALL TOD RAHA HU...**\n**[██████□□□□] 60%**", "**💻 ANDAR GHUS GAYA...**\n**[█████████□] 90%**", "**👑 HACK COMPLETE! BY VILLAIN 👑**\n**😂 USRBAN!**"])
@client.on(events.NewMessage(pattern=r"\.load"))
async def load(e): await anim(e, ["**⏳ LOADING...**", "**⏳ LOADING... ████ 25%**", "**⏳ LOADING... ████████ 50%**", "**⏳ LOADING... ████████████ 75%**", "**✅ LOADED! VILLAIN AA GAYA! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.fire"))
async def fire(e): await anim(e, ["**🔥**", "**🔥🔥**", "**🔥🔥🔥**", "**🔥🔥🔥🔥**", "**🔥 VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.moon"))
async def moon(e): await anim(e, ["**🌑**", "**🌒**", "**🌓**", "**🌔**", "**🌕 FULL MOON!**", "**🌖**", "**🌗**", "**🌘**", "**🌑 VILLAIN KI RAAT! 😈**"])
@client.on(events.NewMessage(pattern=r"\.dance"))
async def dance(e): await anim(e, ["**🕺**", "**💃🕺**", "**🕺💃🕺**", "**💃🕺💃🕺 PARTY SHURU! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.rain"))
async def rain(e): await anim(e, ["**☁️**", "**🌧️☁️**", "**⛈️🌧️☁️**", "**🌧️ BAARISH AA GAYI! ☔**"])
@client.on(events.NewMessage(pattern=r"\.run"))
async def run(e): await anim(e, ["**🏃**", "**🏃‍♂️💨**", "**🏃‍♂️💨💨**", "**🏃‍♂️💨💨💨 VILLAIN BHAG GAYA! 😂**"])

# ================= PRANK ZONE - SAB ANIMATION =================
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e): await anim_owner(e, ["**💻 HACKING START...**\n**[□□□□□] 10%**", "**💻 HACKING...**\n**[████□] 70%**", "**✅ HACK COMPLETE!**\n**😂 chud gaya!**"])
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e): await anim_owner(e, ["**💥 PRANK DDOS START...**", "**💥 SERVER DOWN HO RAHA...**", "**✅ HO GAYA!**\n**😂 COMPLETED! Attack!**"])
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e): await anim_owner(e, ["**📍 TRACE HO RAHA HAI...**", "**📍 LOCATION MIL GAYI...**", "**😂 COMPLETED! Trace!**"])
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e): await anim_owner(e, ["**🦠 VIRUS BANA RAHA HU...**", "**🦠 VIRUS INJECT HO RAHA...**", "**😂 PRANK HAI! Koi Virus Nahi!**"])
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e): await anim_owner(e, ["**🌑 DARKWEB OPEN HO RAHA HAI...**", "**🌑 CONNECT HO RAHA...**", "**😂 PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e): await anim_owner(e, ["**📹 CCTV DHOOND RAHA HU...**", "**📹 CAMERA MIL GAYA...**", "**📹 LIVE FEED ON...**", "**😂 COMPLETED! CCTV !**"])
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e): await anim_owner(e, ["**📱 WHATSAPP CONNECT... 25%**", "**📱 CHAT SCAN... 60%**", "**✅ HO GAYA!**\n**😂 COMPLETED! Whatsapp Hack!**"])
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def phack(e): await anim_owner(e, ["**🔓 PASSWORD HACK HO RAHA...**", "**🔓 CRACK HO RAHA...**", "**✅ PASSWORD: `KASHYAP_USR_BOT_17` 😂**\n**COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.location"))
async def location(e): await anim_owner(e, ["**📍 LOCATION TRACE...**", "**📍 SATELLITE CONNECT...**", "**📍 LOCATION: TERE DIL ME 😍**\n**😂 COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.number"))
async def number(e): await anim_owner(e, ["**📞 NUMBER TRACE...**", "**📞 NAAM PATA HO RAHA...**", "**✅ Naam: VILLAIN KA DOST 😎**\n**😂 COMPLETED!**"])
@client.on(events.NewMessage(pattern=r"\.varius"))
async def varius(e): await anim_owner(e, ["**🦠 VARIUS BANA RAHA HU...**", "**🦠 VARIUS INJECT... 50%**", "**✅ VARIUS DAAL DIYA!**\n**VARIOUS!**"])

print("VILLAIN V15 STARTED! 🔥")
client.start()
client.run_until_disconnected()
