# ============================================================
# 👑 VILLAIN USERBOT - V16 ENGLISH 
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

async def anim(e, steps):
    m = await client.send_message(e.chat_id, steps[0])
    for s in steps[1:]:
        await asyncio.sleep(1.2)
        try: await m.edit(s)
        except: pass
    return m

async def anim_owner(e, steps):
    if not is_owner(e):
        await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER CAN USE THIS!**"])
        return
    await anim(e, steps)

# ================= SUDO =================
@client.on(events.NewMessage(pattern=r"\.addsudo(?: |$)(.*)"))
async def addsudo(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await anim(e, ["**❌ CHECKING...**", "**❌ Use: `.addsudo 123456`**"]); return
    SUDO_USERS.add(uid); save_sudo()
    await anim(e, ["**⏳ ADDING SUDO...**", "**✅ SUDO ADDED!**", f"**👑 NEW KING!**\n**ID:** `{uid}`"])

@client.on(events.NewMessage(pattern=r"\.remsudo(?: |$)(.*)"))
async def remsudo(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    arg = e.pattern_match.group(1).strip()
    rep = await e.get_reply_message()
    uid = int(arg) if arg.isdigit() else (rep.sender_id if rep else None)
    if not uid: await anim(e, ["**❌ CHECKING...**", "**❌ Use: `.remsudo 123456`**"]); return
    SUDO_USERS.discard(uid); save_sudo()
    await anim(e, ["**⏳ REMOVING SUDO...**", f"**❌ SUDO REMOVED! ID:** `{uid}`"])

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    if not SUDO_USERS: await anim(e, ["**📋 OPENING LIST...**", "**📋 SUDO LIST IS EMPTY!**"])
    else: await anim(e, ["**📋 OPENING LIST...**", "**👑 SUDO LIST 👑**\n" + "\n".join([f"➤ `{x}`" for x in SUDO_USERS])])

# ================= ALIVE / HELP =================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    await anim(e, [
        "**👑 CHECKING VILLAIN...**",
        "**⚡ STATUS CHECK... ONLINE!**",
        "**🔥 VILLAIN IS ALIVE! 🔥**\n\n**👑 OWNER : VILLAIN**\n**⚡ STATUS : ONLINE**\n**🛠️ VERSION : V16 ENGLISH**\n**⏱️ UPTIME : " + uptime() + "**\n**👥 SUDO : " + str(len(SUDO_USERS)) + "**\n\n**😈 NOW VILLAIN WILL RULE!**"
    ])

@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await anim(e, [
        "**👑 OPENING MENU...**",
        "**👑 OPENING MENU... 50%**",
        "**👑 VILLAIN V16 - ALL COMMANDS 👑**\n\n**SUDO:** `.addsudo` `.remsudo` `.sudolist`\n**MEGA ANIMATION:** `.megahack` `.megavirus` `.megalove` `.megabomb`\n**ANIMATION:** `.love` `.bomb` `.load` `.fire` `.moon` `.dance` `.rain` `.hackanim` `.heart` `.run`\n**FUN:** `.joke` `.roast` `.shayari` `.meme` `.attitude` `.truth` `.dare` `.ship` `.slap` `.kiss` `.hug` `.pickup` `.cute` `.flirt`\n**GAME:** `.dice` `.coin` `.luck` `.lovecalc` `.future` `.crush` `.horoscope`\n**STYLE:** `.echo` `.shout` `.bold` `.reverse` `.say` `.bio` `.caption`\n**WORK:** `.calc` `.weather` `.crypto` `.google` `.anime` `.songdl`\n**PRANK:** `.hack2` `.ddos` `.trace` `.virus` `.darkweb` `.cctv` `.whatsapp` `.passwordhack` `.location` `.number` `.varius`\n**VILLAIN:** `.jail` `.free` `.kill` `.revive` `.wanted` `.gang` `.sus` `.vs` `.top` `.mafia` `.don` `.king` `.queen`\n**GROUP:** `.tagall` `.purge` `.kick` `.ban` `.unban` `.mute` `.unmute` `.promote` `.demote`\n**BASIC:** `.alive` `.ping` `.id` `.info` `.time` `.uptime` `.profile` `.stats`"
    ])

# ================= BASIC =================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await anim(e, ["**🏓 SENDING PING...**", "**🏓 PONG! VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r = await e.get_reply_message()
    if r: await anim(e, ["**🔍 FINDING ID...**", f"**👤 ID:** `{r.sender_id}`"])
    else: await anim(e, ["**🔍 FINDING ID...**", f"**👤 Your ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`"])
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await anim(e, ["**🕐 CHECKING TIME...**", f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')} | **📅 {datetime.datetime.now().strftime('%d %B %Y')}**"])
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await anim(e, ["**⏱️ CHECKING UPTIME...**", f"**⏱️ UPTIME:** {uptime()}"])
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r = await e.get_reply_message(); u = r.sender if r else await e.get_sender()
    await anim(e, ["**🔍 FETCHING INFO...**", f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Not Available'}"])
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await anim(e, ["**👑 OPENING PROFILE...**", f"**👑 PROFILE - VILLAIN**\n**ID:** `{e.sender_id}`\n**Status:** KING 👑"])
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await anim(e, ["**📊 LOADING STATS...**", f"**📊 STATS**\n**Uptime:** {uptime()}\n**Sudo:** {len(SUDO_USERS)}\n**Version:** V16"])

# ================= FUN - ALL ANIMATION IN ENGLISH =================
def anim_one(pattern, steps_list):
    async def h(e): await anim(e, steps_list)
    client.on(events.NewMessage(pattern=pattern))(h)

anim_one(r"\.joke", ["**😂 THINKING OF A JOKE...**", "**😂 FOUND IT!**", "**😂 JOKE:**\nTeacher: Why didn't you do homework?\nStudent: Sir, VILLAIN turned off the internet! 😂"])
anim_one(r"\.roast", ["**🔥 COOKING A ROAST...**", "**🔥 ROAST READY!**", "**🔥 ROAST:**\nYour face is so funny, even the mirror says - Bro, I will break! 😂"])
anim_one(r"\.shayari", ["**💔 WRITING SHAYARI...**", "**💔 SHAYARI:**\nI got so lost in your memories,\nEven VILLAIN said - Bro, you are gone! 💔"])
anim_one(r"\.meme", ["**😂 FINDING A MEME...**", "**😂 MEME:**\nWhen VILLAIN comes online, everyone's phone hangs! 📱🔥"])
anim_one(r"\.attitude", ["**😎 LOADING ATTITUDE...**", "**😎 ATTITUDE:**\n**I am VILLAIN, I don't bow, I make others bow!**"])
anim_one(r"\.truth", ["**🤔 THINKING TRUTH...**", "**🤔 TRUTH:**\nWhat is your biggest secret? Tell me! 😏"])
anim_one(r"\.dare", ["**😈 THINKING DARE...**", "**😈 DARE:**\nSend I Love You to your crush! 😂"])
anim_one(r"\.pickup", ["**😍 THINKING PICKUP LINE...**", "**😍 PICKUP:**\nAre you WiFi? Because I want to connect with you! 😂"])
anim_one(r"\.cute", ["**🥰 CHECKING...**", "**🥰 CUTE:**\nYou are so cute, even VILLAIN melted!"])
anim_one(r"\.flirt", ["**😏 FLIRT MODE ON...**", "**😏 FLIRT:**\nEven VILLAIN is in love with your smile!"])
anim_one(r"\.slap", ["**👋 RAISING HAND...**", "**👋 SLAP! That was hard!**"])
anim_one(r"\.kiss", ["**😘 COMING CLOSER...**", "**😘 KISS! Oh this love!**"])
anim_one(r"\.hug", ["**🤗 OPENING ARMS...**", "**🤗 HUG! One hug is a must!**"])
anim_one(r"\.dice", ["**🎲 ROLLING DICE...**", f"**🎲 DICE:** {random.randint(1,6)}"])
anim_one(r"\.coin", ["**🪙 TOSSING COIN...**", "**🪙 COIN:** HEADS 😎"])
anim_one(r"\.crush", ["**💘 CHECKING CRUSH...**", "**💘 CRUSH:**\nYour crush is also looking at you! 👀"])
anim_one(r"\.horoscope", ["**🔮 READING STARS...**", "**🔮 HOROSCOPE:**\nToday is your lucky day! VILLAIN promises!"])
anim_one(r"\.future", ["**🔮 SEEING FUTURE...**", "**🔮 FUTURE:**\nYou will become a very big man one day, VILLAIN promises! 👑"])
anim_one(r"\.jail", ["**⛓️ CATCHING YOU...**", "**⛓️ YOU ARE IN JAIL! You cannot go out now! 😈**"])
anim_one(r"\.free", ["**🔓 FINDING KEY...**", "**🔓 YOU ARE FREE! VILLAIN forgave you!**"])
anim_one(r"\.kill", ["**🔪 AIMING...**", "**🔪 KILL! VILLAIN FINISHED YOU! 💀 - IT'S A PRANK!**"])
anim_one(r"\.revive", ["**💉 GIVING INJECTION...**", "**💉 REVIVE! You are alive again!**"])
anim_one(r"\.wanted", ["**🚨 MAKING POSTER...**", "**🚨 WANTED! Reward: 10 Crore! Everyone is searching for VILLAIN!**"])
anim_one(r"\.gang", ["**😈 CALLING GANG...**", "**😈 GANG: VILLAIN GANG - Most Dangerous!**"])
anim_one(r"\.sus", ["**👀 CHECKING...**", "**👀 SUS: You are looking very SUS today!**"])
anim_one(r"\.vs", ["**⚔️ FIGHT STARTING...**", "**⚔️ VS: VILLAIN VS WORLD - VILLAIN WILL WIN! 🔥**"])
anim_one(r"\.top", ["**🏆 MAKING LIST...**", "**🏆 TOP: No.1 - VILLAIN 👑**"])
anim_one(r"\.mafia", ["**😈 MAFIA COMING...**", "**😈 MAFIA: VILLAIN MAFIA!**"])
anim_one(r"\.don", ["**👑 DON COMING...**", "**👑 DON: 11 countries police are waiting for Don!**"])
anim_one(r"\.king", ["**👑 WEARING CROWN...**", "**👑 KING: KING IS BACK - VILLAIN!**"])
anim_one(r"\.queen", ["**👸 QUEEN COMING...**", "**👸 QUEEN: Queen will be only VILLAIN's!**"])
anim_one(r"\.tagall", ["**📢 CALLING EVERYONE...**", "**📢 TAG ALL! Everyone come, VILLAIN is calling!**"])
anim_one(r"\.purge", ["**🧹 CLEANING...**", "**🧹 PURGE! All trash cleaned!**"])
anim_one(r"\.kick", ["**🦶 KICKING...**", "**🦶 KICK! Out of group!**"])
anim_one(r"\.ban", ["**🚫 BANNING...**", "**🚫 BAN! VILLAIN banned you!**"])
anim_one(r"\.unban", ["**✅ BRINGING BACK...**", "**✅ UNBAN! You are back!**"])
anim_one(r"\.mute", ["**🔇 MUTING...**", "**🔇 MUTE! Now be quiet!**"])
anim_one(r"\.unmute", ["**🔊 UNMUTING...**", "**🔊 UNMUTE! Now you can speak!**"])
anim_one(r"\.promote", ["**⬆️ PROMOTING...**", "**⬆️ PROMOTE! Now you are also Admin!**"])
anim_one(r"\.demote", ["**⬇️ DEMOTING...**", "**⬇️ DEMOTE! Removed from Admin!**"])
anim_one(r"\.bio", ["**📝 THINKING BIO...**", "**📝 BIO IDEA:**\n`👑 VILLAIN | 😈 King | 🔥 No Mercy`"])
anim_one(r"\.caption", ["**📸 THINKING CAPTION...**", "**📸 CAPTION:**\n`KING IS BACK 👑🔥 #VILLAIN`"])
anim_one(r"\.songdl", ["**🎵 FINDING SONG...**", "**🎵 SONG: Search on YouTube, VILLAIN is playing song! 🎧**"])

@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await anim(e, ["**🍀 CHECKING LUCK...**", f"**🍀 LUCK:** {random.randint(1,100)}%"])
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await anim(e, ["**💘 CALCULATING LOVE...**", "**💘 CALCULATING LOVE... 50%**", f"**💘 LOVE CALC:** {random.randint(50,100)}% Made For Each Other!"])
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await anim(e, ["**💘 MAKING SHIP...**", f"**💘 SHIP:** {random.randint(1,100)}% Match!"])
@client.on(events.NewMessage(pattern=r"\.calc(?: |$)(.*)"))
async def calc(e):
    q = e.pattern_match.group(1).strip()
    try:
        if not q or any(c not in "0123456789+-*/(). " for c in q): raise ValueError
        await anim(e, ["**🧮 CALCULATING...**", f"**🧮 CALC:** `{q}` = **{eval(q, {'__builtins__':{}})}**"])
    except: await anim(e, ["**❌ CHECKING...**", "**❌ Write correctly: `.calc 2+2`**"])
@client.on(events.NewMessage(pattern=r"\.echo(?: |$)(.*)"))
async def echo(e): await anim(e, ["**📢 LISTENING...**", e.pattern_match.group(1) or "**Write something!**"])
@client.on(events.NewMessage(pattern=r"\.say(?: |$)(.*)"))
async def say(e): await anim(e, ["**🗣️ SPEAKING...**", e.pattern_match.group(1) or "**Write something!**"])
@client.on(events.NewMessage(pattern=r"\.shout(?: |$)(.*)"))
async def shout(e): await anim(e, ["**📢 SHOUTING...**", f"**📢 {e.pattern_match.group(1).upper()}**"])
@client.on(events.NewMessage(pattern=r"\.bold(?: |$)(.*)"))
async def bold(e): await anim(e, ["**✨ MAKING BOLD...**", f"**{e.pattern_match.group(1)}**"])
@client.on(events.NewMessage(pattern=r"\.reverse(?: |$)(.*)"))
async def reverse(e): await anim(e, ["**🔄 REVERSING...**", e.pattern_match.group(1)[::-1]])
@client.on(events.NewMessage(pattern=r"\.weather(?: |$)(.*)"))
async def weather(e):
    c = e.pattern_match.group(1) or "Indore"
    await anim(e, ["**🌤️ CHECKING WEATHER...**", f"**🌤️ WEATHER - {c}**\n**Temp:** {random.randint(25,35)}°C ☀️"])
@client.on(events.NewMessage(pattern=r"\.crypto(?: |$)(.*)"))
async def crypto(e): await anim(e, ["**💰 CHECKING RATE...**", "**💰 CRYPTO:**\n**BTC:** $97,000 🔥\n**ETH:** $3,400"])
@client.on(events.NewMessage(pattern=r"\.google(?: |$)(.*)"))
async def google(e):
    q = e.pattern_match.group(1); await anim(e, ["**🔍 GOOGLING...**", f"**🔍 GOOGLE:** {q}\nhttps://www.google.com/search?q={q.replace(' ','+')}"])
@client.on(events.NewMessage(pattern=r"\.anime(?: |$)(.*)"))
async def anime(e): await anim(e, ["**🎌 FINDING ANIME...**", f"**🎌 ANIME:** {e.pattern_match.group(1)}\n**VILLAIN's fav: One Piece!**"])

# ================= ANIMATION SPECIAL - ENGLISH =================
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await anim(e, ["**🤍 HEART IS EMPTY...**", "**💛 HEART IS FILLING...**", "**🧡 HEART IS BEATING...**", "**❤️ HEART IS FULL!**", "**❤️❤️❤️ I LOVE YOU ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.heart"))
async def heart(e): await anim(e, ["**🤍**", "**🤍💛**", "**🤍💛🧡**", "**🤍💛🧡❤️**", "**❤️❤️❤️ HEART TO HEART ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.bomb"))
async def bomb(e): await anim(e, ["**💣 BOMB PLANTED! RUN!**", "**💣 5...**", "**💣 4...**", "**💣 3...**", "**💣 2...**", "**💣 1...**", "**💥💥 BOOM! 💥💥**\n**😂 IT'S A PRANK! NOTHING EXPLODED!**"])
@client.on(events.NewMessage(pattern=r"\.hackanim"))
async def hackanim(e): await anim(e, ["**💻 HACKING START...**\n**[□□□□□□□□□□] 0%**", "**💻 BREAKING PASSWORD...**\n**[███□□□□□□□] 30%**", "**💻 BREAKING FIREWALL...**\n**[██████□□□□] 60%**", "**💻 ENTERED INSIDE...**\n**[█████████□] 90%**", "**👑 HACK COMPLETE! BY VILLAIN 👑**\n**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.load"))
async def load(e): await anim(e, ["**⏳ LOADING...**", "**⏳ LOADING... ████ 25%**", "**⏳ LOADING... ████████ 50%**", "**⏳ LOADING... ████████████ 75%**", "**✅ LOADED! VILLAIN IS HERE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.fire"))
async def fire(e): await anim(e, ["**🔥**", "**🔥🔥**", "**🔥🔥🔥**", "**🔥🔥🔥🔥**", "**🔥 VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.moon"))
async def moon(e): await anim(e, ["**🌑**", "**🌒**", "**🌓**", "**🌔**", "**🌕 FULL MOON!**", "**🌖**", "**🌗**", "**🌘**", "**🌑 VILLAIN'S NIGHT! 😈**"])
@client.on(events.NewMessage(pattern=r"\.dance"))
async def dance(e): await anim(e, ["**🕺**", "**💃🕺**", "**🕺💃🕺**", "**💃🕺💃🕺 PARTY STARTED! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.rain"))
async def rain(e): await anim(e, ["**☁️**", "**🌧️☁️**", "**⛈️🌧️☁️**", "**🌧️ RAIN IS HERE! ☔**"])
@client.on(events.NewMessage(pattern=r"\.run"))
async def run(e): await anim(e, ["**🏃**", "**🏃‍♂️💨**", "**🏃‍♂️💨💨**", "**🏃‍♂️💨💨💨 VILLAIN RAN AWAY! 😂**"])

# ================= MEGA ANIMATION - ENGLISH - LONG =================
async def mega_anim(e, frames):
    m = await client.send_message(e.chat_id, frames[0])
    for f in frames[1:]:
        await asyncio.sleep(2)
        try: await m.edit(f)
        except: pass

@client.on(events.NewMessage(pattern=r"\.megahack"))
async def megahack(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    await mega_anim(e, [
        "**💻 VILLAIN TERMINAL OPENING...**",
        "**💻 TERMINAL OPENED ✅**\n```\n> villain@hack:~$ \n```",
        "**💻 SELECTING TARGET...**\n```\n> scanning... \n```",
        "**💻 TARGET FOUND!**\n```\n> target: VICTIM_007\n> ip: 192.168.***.***\n```",
        "**💻 CHECKING FIREWALL...**\n```\n> firewall: STRONG\n> bypassing...\n```",
        "**💻 BYPASSING FIREWALL... 10%**\n`[█□□□□□□□□□]`",
        "**💻 BYPASSING FIREWALL... 30%**\n`[███□□□□□□□]`",
        "**💻 BYPASSING FIREWALL... 55%**\n`[█████□□□□□]`",
        "**💻 BYPASSING FIREWALL... 80%**\n`[████████□□]`",
        "**💻 FIREWALL BYPASSED! ✅**\n`[██████████] 100%`",
        "**💻 ENTERING SYSTEM...**\n```\n> entering system...\n```",
        "**💻 CRACKING PASSWORD...**\n```\n> password: ****\n```",
        "**💻 CRACKING PASSWORD... 20%**\n`> pass: v****`",
        "**💻 CRACKING PASSWORD... 45%**\n`> pass: vi***`",
        "**💻 CRACKING PASSWORD... 70%**\n`> pass: vil**`",
        "**💻 CRACKING PASSWORD... 90%**\n`> pass: vill*`",
        "**💻 PASSWORD FOUND!**\n`> pass: villain123`",
        "**📸 ACCESSING CAMERA...**\n`> camera: connecting...`",
        "**📸 CAMERA ON!**\n`> camera: LIVE`",
        "**📁 COPYING FILES... 10%**\n`[█□□□□□□□□□]`",
        "**📁 COPYING FILES... 35%**\n`[███□□□□□□□]`",
        "**📁 COPYING FILES... 60%**\n`[██████□□□□]`",
        "**📁 COPYING FILES... 85%**\n`[████████□□]`",
        "**📁 FILES COPIED! ✅**\n`[██████████] 100%`",
        "**📍 TRACING LOCATION...**\n`> satellite: connecting...`",
        "**📍 LOCATION FOUND!**\n`> location: INDIA`",
        "**🦠 INJECTING VIRUS...**\n`> virus: injecting...`",
        "**🦠 VIRUS INJECTED!**\n`> virus: ACTIVE`",
        "**💣 DESTROYING SYSTEM... 5**",
        "**💣 DESTROYING SYSTEM... 4**",
        "**💣 DESTROYING SYSTEM... 3**",
        "**💣 DESTROYING SYSTEM... 2**",
        "**💣 DESTROYING SYSTEM... 1**",
        "**💥💥 BOOM! SYSTEM HACKED! 💥💥**",
        "**👑 HACK COMPLETE BY VILLAIN 👑**\n\n**😂 HEY IT WAS A PRANK!**\n**No Hack Happened, This Was Only Animation!**"
    ])

@client.on(events.NewMessage(pattern=r"\.megavirus"))
async def megavirus(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    await mega_anim(e, ["**🦠 VIRUS LAB OPENING...**", "**🦠 MAKING VIRUS... 10%**", "**🦠 MAKING VIRUS... 30%**", "**🦠 MAKING VIRUS... 55%**", "**🦠 MAKING VIRUS... 80%**", "**🦠 VIRUS READY! ✅**", "**🦠 SENDING TO TARGET...**", "**🦠 VIRUS ENTERED!**", "**📱 PHONE HANGING...**", "**📱 PHONE HANG... 50%**", "**📱 PHONE HANG... 99%**", "**📱 PHONE SWITCHED OFF!**", "**📱 PHONE SWITCHED ON AGAIN!**", "**✅ VIRUS ATTACK COMPLETE!**\n**😂 IT'S A PRANK! No Virus!**"])
@client.on(events.NewMessage(pattern=r"\.megalove"))
async def megalove(e):
    await mega_anim(e, ["**🤍 HEART IS EMPTY...**", "**🤍 SOMEONE IS COMING IN HEART...**", "**💛 HEART IS BEATING...**", "**💛 HEART IS BEATING FAST...**", "**🧡 LOVE IS HAPPENING...**", "**🧡 LOVE IS GROWING...**", "**❤️ LOVE HAPPENED!**", "**❤️❤️ HEARTS MET!**", "**❤️❤️❤️ I LOVE YOU ❤️❤️❤️**", "**💍 WILL YOU MARRY ME? 😍**"])
@client.on(events.NewMessage(pattern=r"\.megabomb"))
async def megabomb(e):
    await mega_anim(e, ["**💣 BOMB FOUND!**", "**💣 PLANTING BOMB...**", "**💣 BOMB PLANTED! RUN!**", "**💣 TIMER ON... 10**", "**💣 TIMER... 9**", "**💣 TIMER... 8**", "**💣 TIMER... 7**", "**💣 TIMER... 6**", "**💣 TIMER... 5**", "**💣 TIMER... 4**", "**💣 TIMER... 3**", "**💣 TIMER... 2**", "**💣 TIMER... 1**", "**💥💥 BOOM! 💥💥**", "**😂 IT'S A PRANK! NOTHING EXPLODED!**"])

# ================= PRANK ZONE - ENGLISH =================
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e): await anim_owner(e, ["**💻 HACKING START...**\n**[□□□□□] 10%**", "**💻 HACKING...**\n**[████□] 70%**", "**✅ HACK COMPLETE!**\n**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e): await anim_owner(e, ["**💥 PRANK DDOS START...**", "**💥 SERVER GOING DOWN...**", "**✅ DONE!**\n**😂 IT'S A PRANK! No Attack Happened!**"])
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e): await anim_owner(e, ["**📍 TRACING...**", "**📍 LOCATION FOUND...**", "**😂 IT'S A PRANK! No Trace!**"])
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e): await anim_owner(e, ["**🦠 MAKING VIRUS...**", "**🦠 INJECTING VIRUS...**", "**😂 IT'S A PRANK! No Virus!**"])
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e): await anim_owner(e, ["**🌑 OPENING DARKWEB...**", "**🌑 CONNECTING...**", "**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e): await anim_owner(e, ["**📹 FINDING CCTV...**", "**📹 CAMERA FOUND...**", "**📹 LIVE FEED ON...**", "**😂 IT'S A PRANK! CCTV Cannot Be Hacked Like This!**"])
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e): await anim_owner(e, ["**📱 CONNECTING WHATSAPP... 25%**", "**📱 SCANNING CHAT... 60%**", "**✅ DONE!**\n**😂 IT'S A PRANK! Whatsapp Cannot Be Hacked!**"])
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def phack(e): await anim_owner(e, ["**🔓 HACKING PASSWORD...**", "**🔓 CRACKING...**", "**✅ PASSWORD: `i_am_prank_123` 😂**\n**IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.location"))
async def location(e): await anim_owner(e, ["**📍 TRACING LOCATION...**", "**📍 CONNECTING SATELLITE...**", "**📍 LOCATION: IN YOUR HEART 😍**\n**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.number"))
async def number(e): await anim_owner(e, ["**📞 TRACING NUMBER...**", "**📞 FINDING NAME...**", "**✅ Name: VILLAIN'S FRIEND 😎**\n**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.varius"))
async def varius(e): await anim_owner(e, ["**🦠 MAKING VARIUS...**", "**🦠 INJECTING VARIUS... 50%**", "**✅ VARIUS INJECTED!**\n**😂 JUST KIDDING! No Varius!**"])

print("VILLAIN V16 STARTED! 🔥")
client.start()
client.run_until_disconnected()
