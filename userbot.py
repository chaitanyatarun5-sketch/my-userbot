# ============================================================
# 👑 VILLAIN USERBOT - V19 FINAL - ALL IN ONE - 151 COMMANDS + .tarunpapa PRIVATE....!
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
async def mega_anim(e, frames):
    m = await client.send_message(e.chat_id, frames[0])
    for f in frames[1:]:
        await asyncio.sleep(2)
        try: await m.edit(f)
        except: pass
    return m
async def blue_anim(e, frames):
    m = await client.send_message(e.chat_id, frames[0])
    for f in frames[1:]:
        await asyncio.sleep(2)
        try: await m.edit(f)
        except: pass
    return m
async def white_anim(e, frames):
    m = await client.send_message(e.chat_id, frames[0])
    for f in frames[1:]:
        await asyncio.sleep(2)
        try: await m.edit(f)
        except: pass
    return m
def BLUE(txt): return f"```\n{txt}\n```"
def WHITE(txt): return f"```\n{txt}\n```"

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

# ================= ALIVE / HELP - BLUE SCREEN - 5 PAGE JAISE PEHLE THA =================
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    await anim(e, [BLUE("VILLAIN USERBOT\nLOADING..."), BLUE("VILLAIN USERBOT\nSTATUS : ONLINE\nVERSION : V19"), "**🔥 VILLAIN IS ALIVE! 🔥**\n\n**👑 OWNER : VILLAIN**\n**⚡ STATUS : ONLINE**\n**🛠️ VERSION : V19 ALL IN ONE**\n**⏱️ UPTIME : " + uptime() + "**\n**👥 SUDO : " + str(len(SUDO_USERS)) + "**\n\n**😈 NOW VILLAIN WILL RULE!**"])
@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await anim(e, [
        BLUE("╔══════════════════════════════╗\n║   👑 VILLAIN USERBOT 👑      ║\n║      HELP MENU - V19         ║\n╚══════════════════════════════╝\n\n> EXTRAS\n──────────────────────────────\n\n• UTILITIES\n  .alive .ping .help .id .info\n  .time .uptime .stats .profile\n\n• SUDO\n  .addsudo .remsudo .sudolist\n\n• FUN\n  .joke .roast .shayari .meme\n  .attitude .truth .dare .ship\n  .slap .kiss .hug .pickup\n  .cute .flirt .dice .coin\n  .luck .lovecalc .future\n  .crush .horoscope\n\n• STYLE\n  .echo .shout .bold .reverse\n  .say .bio .caption\n\n• WORK\n  .calc .weather .crypto\n  .google .anime .songdl\n\n• GROUP\n  .tagall .purge .kick .ban\n  .unban .mute .unmute\n  .promote .demote\n\n──────────────────────────────\nVILLAIN • USERBOT • PRIME"),
        BLUE("╔══════════════════════════════╗\n║   😈 HACK MENU 😈           ║\n╚══════════════════════════════╝\n\n> HACK - BLUE SCREEN\n──────────────────────────────\n\n• MEGA HACK\n  .megahack .hackwifi .hackinsta\n  .hackphone .hackbank .hackcctv\n\n• PRANK HACK\n  .hack2 .ddos .trace .virus\n  .darkweb .cctv .whatsapp\n  .passwordhack .location\n  .number .varius .hackanim\n\n──────────────────────────────\nALL HACK ARE PRANK! 😂"),
        BLUE("╔══════════════════════════════╗\n║   🔥 MEGA MENU 🔥          ║\n╚══════════════════════════════╝\n\n> MEGA ANIMATION\n──────────────────────────────\n\n• MEGA LOVE\n  .megalove .megapropose\n  .megawedding .megabreakup\n  .megacrush .love .heart\n\n• MEGA FUN\n  .megapolice .megaexam .megaghost\n  .megamoney .megafight .megabirthday\n  .megaalien .megajailbreak .megadon\n  .megamafia .megachai .megapizza\n  .megacricket .megafootball .megaschool\n  .megaiphone .megasuperhero .megazombie\n  .megavirus .megabomb\n\n• ANIMATION\n  .bomb .load .fire .moon\n  .dance .rain .run\n\n──────────────────────────────\nVILLAIN • USERBOT • PRIME"),
        BLUE("╔══════════════════════════════╗\n║   👑 VILLAIN MENU 👑       ║\n╚══════════════════════════════╝\n\n> VILLAIN\n──────────────────────────────\n  .jail .free .kill .revive\n  .wanted .gang .sus .vs\n  .top .mafia .don .king .queen\n\n──────────────────────────────\nTYPE .help FOR ALL MENU\nVILLAIN WILL RULE! 🔥"),
        BLUE("╔══════════════════════════════╗\n║   🚂 MOVING ANIMATION 🚂   ║\n║   EMOJI WALA - V19          ║\n╚══════════════════════════════╝\n\n> MOVING - SIRF EMOJI CHALEGA!\n──────────────────────────────\n\n• MOVING 1\n  .train .heartbig .fightbig\n  .rocket .carrace .plane\n  .bike .cycle .ship .runbig\n\n• MOVING 2 - 15 NAYE\n  .bus .policechase .cricketbig\n  .footballbig .firebig .rainbig\n  .snake .catdog .pubg .moneyfly\n  .dancebig .maggi .thief\n  .ghostrun .lovefly\n\n──────────────────────────────\nTU BAS COMMAND LIKH\nBOT KHUD EMOJI CHALAYEGA!")
    ])

# ================= PRIVATE - .tarunpapa - WHITE SCREEN - 1 HI MESSAGE ME SAB - PURA KA PURA =================
@client.on(events.NewMessage(pattern=r"\.tarunpapa"))
async def tarunpapa(e):
    if not is_owner(e):
        await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER CAN USE THIS!**"])
        return
    await client.send_message(e.chat_id, WHITE("""╔══════════════════════════════╗
║   👑 VILLAIN - TARUNPAPA 👑   ║
║   ALL COMMANDS - 1 SCREEN    ║
╚══════════════════════════════╝

UTILITIES:
.alive .ping .help .id .info .time .uptime .stats .profile

SUDO:
.addsudo .remsudo .sudolist

FUN:
.joke .roast .shayari .meme .attitude .truth .dare .ship .slap .kiss .hug .pickup .cute .flirt .dice .coin .luck .lovecalc .future .crush .horoscope

STYLE:
.echo .shout .bold .reverse .say .bio .caption

WORK:
.calc .weather .crypto .google .anime .songdl

GROUP:
.tagall .purge .kick .ban .unban .mute .unmute .promote .demote

HACK - PRANK:
.megahack .hackwifi .hackinsta .hackphone .hackbank .hackcctv .hack2 .ddos .trace .virus .darkweb .cctv .whatsapp .passwordhack .location .number .varius .hackanim

MEGA LOVE:
.megalove .megapropose .megawedding .megabreakup .megacrush .love .heart

MEGA FUN:
.megapolice .megaexam .megaghost .megamoney .megafight .megabirthday .megaalien .megajailbreak .megadon .megamafia .megachai .megapizza .megacricket .megafootball .megaschool .megaiphone .megasuperhero .megazombie .megavirus .megabomb

ANIMATION:
.bomb .load .fire .moon .dance .rain .run

VILLAIN:
.jail .free .kill .revive .wanted .gang .sus .vs .top .mafia .don .king .queen

MOVING 1:
.train .heartbig .fightbig .rocket .carrace .plane .bike .cycle .ship .runbig

MOVING 2:
.bus .policechase .cricketbig .footballbig .firebig .rainbig .snake .catdog .pubg .moneyfly .dancebig .maggi .thief .ghostrun .lovefly

PRIVATE:
.tarunpapa
"""

# ================= BASIC =================
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await anim(e, [BLUE("PING..."), "**🏓 PONG! VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e):
    r = await e.get_reply_message()
    if r: await anim(e, [BLUE("FINDING ID..."), f"**👤 ID:** `{r.sender_id}`"])
    else: await anim(e, [BLUE("FINDING ID..."), f"**👤 Your ID:** `{e.sender_id}`\n**💬 Chat ID:** `{e.chat_id}`"])
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await anim(e, [BLUE("CHECKING TIME..."), f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')} | **📅 {datetime.datetime.now().strftime('%d %B %Y')}**"])
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await anim(e, [BLUE("CHECKING UPTIME..."), f"**⏱️ UPTIME:** {uptime()}"])
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    r = await e.get_reply_message(); u = r.sender if r else await e.get_sender()
    await anim(e, [BLUE("FETCHING INFO..."), f"**👤 INFO**\n**Name:** {u.first_name}\n**ID:** `{u.id}`\n**Username:** @{u.username or 'Not Available'}"])
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e): await anim(e, [BLUE("OPENING PROFILE..."), f"**👑 PROFILE - VILLAIN**\n**ID:** `{e.sender_id}`\n**Status:** KING 👑"])
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await anim(e, [BLUE("LOADING STATS..."), f"**📊 STATS**\n**Uptime:** {uptime()}\n**Sudo:** {len(SUDO_USERS)}\n**Version:** V19"])

# ================= FUN =================
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
        await anim(e, [BLUE("CALCULATING..."), f"**🧮 CALC:** `{q}` = **{eval(q, {'__builtins__':{}})}**"])
    except: await anim(e, ["**❌ CHECKING...**", "**❌ Write correctly: `.calc 2+2`**"])
@client.on(events.NewMessage(pattern=r"\.echo(?: |$)(.*)"))
async def echo(e):
    rep = await e.get_reply_message()
    if rep and rep.text:
        await anim(e, ["**📢 LISTENING...**", rep.text])
    else:
        await anim(e, ["**📢 LISTENING...**", e.pattern_match.group(1) or "**Write something!**"])
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
    await anim(e, [BLUE("CHECKING WEATHER..."), f"**🌤️ WEATHER - {c}**\n**Temp:** {random.randint(25,35)}°C ☀️"])
@client.on(events.NewMessage(pattern=r"\.crypto(?: |$)(.*)"))
async def crypto(e): await anim(e, [BLUE("CHECKING RATE..."), "**💰 CRYPTO:**\n**BTC:** $97,000 🔥\n**ETH:** $3,400"])
@client.on(events.NewMessage(pattern=r"\.google(?: |$)(.*)"))
async def google(e):
    q = e.pattern_match.group(1); await anim(e, [BLUE("GOOGLING..."), f"**🔍 GOOGLE:** {q}\nhttps://www.google.com/search?q={q.replace(' ','+')}"])
@client.on(events.NewMessage(pattern=r"\.anime(?: |$)(.*)"))
async def anime(e): await anim(e, [BLUE("FINDING ANIME..."), f"**🎌 ANIME:** {e.pattern_match.group(1)}\n**VILLAIN's fav: One Piece!**"])

# ================= ANIMATION CHHOTE =================
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await anim(e, ["**🤍 HEART IS EMPTY...**", "**💛 HEART IS FILLING...**", "**🧡 HEART IS BEATING...**", "**❤️ HEART IS FULL!**", "**❤️❤️❤️ I LOVE YOU ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.heart"))
async def heart(e): await anim(e, ["**🤍**", "**🤍💛**", "**🤍💛🧡**", "**🤍💛🧡**", "**🤍**", "**🤍💛🧡❤️**", "**❤️❤️❤️ HEART TO HEART ❤️❤️❤️**"])
@client.on(events.NewMessage(pattern=r"\.bomb"))
async def bomb(e): await anim(e, ["**💣 BOMB PLANTED! RUN!**", "**💣 5...**", "**💣 4...**", "**💣 3...**", "**💣 2...**", "**💣 1...**", "**💥💥 BOOM! 💥💥**\n**EXPLODED!**"])
@client.on(events.NewMessage(pattern=r"\.hackanim"))
async def hackanim(e): await anim(e, [BLUE("HACKING START...\n[          ] 0%"), BLUE("BREAKING PASSWORD...\n[███       ] 30%"), BLUE("BREAKING FIREWALL...\n[██████    ] 60%"), BLUE("ENTERED INSIDE...\n[█████████ ] 90%"), "**👑 HACK COMPLETE! BY VILLAIN 👑**\n**DONE✅👍!**"])
@client.on(events.NewMessage(pattern=r"\.load"))
async def load(e): await anim(e, [BLUE("LOADING..."), BLUE("LOADING... ████ 25%"), BLUE("LOADING... ████████ 50%"), BLUE("LOADING... ████████████ 75%"), "**✅ LOADED! VILLAIN IS HERE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.fire"))
async def fire(e): await anim(e, ["**🔥**", "**🔥🔥**", "**🔥🔥🔥**", "**🔥🔥🔥🔥**", "**🔥 VILLAIN ON FIRE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.moon"))
async def moon(e): await anim(e, ["**🌑**", "**🌒**", "**🌓**", "**🌔**", "**🌕 FULL MOON!**", "**🌖**", "**🌗**", "**🌘**", "**🌑♨️♨️! 😈**"])
@client.on(events.NewMessage(pattern=r"\.dance"))
async def dance(e): await anim(e, ["**🕺**", "**💃🕺**", "**🕺💃🕺**",  "**🕺💃🕺**", "**💃🕺**", "**💃🕺💃🕺 PARTY STARTED! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.rain"))
async def rain(e): await anim(e, ["**☁️**", "**🌧️☁️**", "**⛈️🌧️☁️**", "**🌧️ RAIN IS HERE! ☔**"])
@client.on(events.NewMessage(pattern=r"\.run"))
async def run(e): await anim(e, ["**🏃 RUNNING...**", "**🏃‍♂️💨 RUNNING FAST...**", "**🏃‍♂️💨💨 FULL SPEED!**", "**🏃♨️ VILLAIN IS FAST! ♨️**"])

# ================= BLUE SCREEN HACK - ALL PRANK =================
@client.on(events.NewMessage(pattern=r"\.megahack"))
async def megahack(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    await blue_anim(e, [BLUE("VILLAIN TERMINAL v19\n> opening terminal..."), BLUE("VILLAIN TERMINAL v19\n> terminal opened ✅\n> villain@hack:~$"), BLUE("VILLAIN TERMINAL v19\n> scanning target..."), BLUE("VILLAIN TERMINAL v19\n> TARGET FOUND!\n> target : VICTIM_007\n> ip : 192.168.***.***"), BLUE("VILLAIN TERMINAL v19\n> checking firewall...\n> firewall : STRONG"), BLUE("VILLAIN TERMINAL v19\n> bypassing firewall... 10%\n[█         ]"), BLUE("VILLAIN TERMINAL v19\n> bypassing firewall... 30%\n[███       ]"), BLUE("VILLAIN TERMINAL v19\n> bypassing firewall... 55%\n[█████     ]"), BLUE("VILLAIN TERMINAL v19\n> bypassing firewall... 80%\n[████████  ]"), BLUE("VILLAIN TERMINAL v19\n> FIREWALL BYPASSED! ✅\n[██████████] 100%"), BLUE("VILLAIN TERMINAL v19\n> entering system..."), BLUE("VILLAIN TERMINAL v19\n> cracking password...\n> password : ****"), BLUE("VILLAIN TERMINAL v19\n> cracking password... 20%\n> pass : v****"), BLUE("VILLAIN TERMINAL v19\n> cracking password... 45%\n> pass : vi***"), BLUE("VILLAIN TERMINAL v19\n> cracking password... 70%\n> pass : vil**"), BLUE("VILLAIN TERMINAL v19\n> cracking password... 90%\n> pass : vill*"), BLUE("VILLAIN TERMINAL v19\n> PASSWORD FOUND!\n> pass : villain123"), BLUE("VILLAIN TERMINAL v19\n> accessing camera..."), BLUE("VILLAIN TERMINAL v19\n> CAMERA ON!\n> camera : LIVE"), BLUE("VILLAIN TERMINAL v19\n> copying files... 10%"), BLUE("VILLAIN TERMINAL v19\n> copying files... 35%"), BLUE("VILLAIN TERMINAL v19\n> copying files... 60%"), BLUE("VILLAIN TERMINAL v19\n> copying files... 85%"), BLUE("VILLAIN TERMINAL v19\n> FILES COPIED! ✅"), BLUE("VILLAIN TERMINAL v19\n> tracing location..."), BLUE("VILLAIN TERMINAL v19\n> LOCATION FOUND!\n> location : INDIA"), BLUE("VILLAIN TERMINAL v19\n> injecting virus..."), BLUE("VILLAIN TERMINAL v19\n> VIRUS INJECTED!"), BLUE("VILLAIN TERMINAL v19\n> destroying system... 5"), BLUE("VILLAIN TERMINAL v19\n> destroying system... 4"), BLUE("VILLAIN TERMINAL v19\n> destroying system... 3"), BLUE("VILLAIN TERMINAL v19\n> destroying system... 2"), BLUE("VILLAIN TERMINAL v19\n> destroying system... 1"), BLUE("VILLAIN TERMINAL v19\n> BOOM! SYSTEM HACKED!"), "**👑 HACK COMPLETE♨️ BY VILLAIN♨️ 👑**\n\n**♨️ COMPLETED♨️!**\n**♨️ Hack Happened, ♨️♨️♨️ ♨️♨️♨️♨️Animation!**"])
@client.on(events.NewMessage(pattern=r"\.hackwifi"))
async def hackwifi(e): await blue_anim(e, [BLUE("WIFI HACK v19\n> start..."), BLUE("WIFI HACK v19\n> scanning wifi..."), BLUE("WIFI HACK v19\n> 5 wifi found!"), BLUE("WIFI HACK v19\n> target : VILLAIN_WIFI"), BLUE("WIFI HACK v19\n> trying password..."), BLUE("WIFI HACK v19\n> password... 10%"), BLUE("WIFI HACK v19\n> password... 30%"), BLUE("WIFI HACK v19\n> password... 55%"), BLUE("WIFI HACK v19\n> password... 80%"), BLUE("WIFI HACK v19\n> password... 95%"), BLUE("WIFI HACK v19\n> PASSWORD FOUND!"), BLUE("WIFI HACK v19\n> connecting..."), BLUE("WIFI HACK v19\n> CONNECTED! ✅"), BLUE("WIFI HACK v19\n> speed : 100 Mbps!"), BLUE("WIFI HACK v19\n> HACK COMPLETE!"), "**😂 IT'S A PRANK! WIFI HACK NAHI HOTA AISE!**"])
@client.on(events.NewMessage(pattern=r"\.hackinsta"))
async def hackinsta(e): await blue_anim(e, [BLUE("INSTA HACK v19\n> start..."), BLUE("INSTA HACK v19\n> searching username..."), BLUE("INSTA HACK v19\n> username found!"), BLUE("INSTA HACK v19\n> scanning profile..."), BLUE("INSTA HACK v19\n> followers : 10K"), BLUE("INSTA HACK v19\n> cracking password... 15%"), BLUE("INSTA HACK v19\n> cracking password... 35%"), BLUE("INSTA HACK v19\n> cracking password... 60%"), BLUE("INSTA HACK v19\n> cracking password... 85%"), BLUE("INSTA HACK v19\n> cracking password... 99%"), BLUE("INSTA HACK v19\n> logging in..."), BLUE("INSTA HACK v19\n> LOGGED IN!"), BLUE("INSTA HACK v19\n> checking photos..."), BLUE("INSTA HACK v19\n> checking DM..."), BLUE("INSTA HACK v19\n> HACK COMPLETE!"), "**😂 IT'S A PRANK! INSTA HACK NAHI HOTA!**"])
@client.on(events.NewMessage(pattern=r"\.hackphone"))
async def hackphone(e): await blue_anim(e, [BLUE("PHONE HACK v19\n> start..."), BLUE("PHONE HACK v19\n> connecting phone..."), BLUE("PHONE HACK v19\n> phone found!"), BLUE("PHONE HACK v19\n> opening gallery..."), BLUE("PHONE HACK v19\n> 1000 photos found!"), BLUE("PHONE HACK v19\n> copying contacts... 20%"), BLUE("PHONE HACK v19\n> copying contacts... 50%"), BLUE("PHONE HACK v19\n> copying contacts... 80%"), BLUE("PHONE HACK v19\n> contacts copied! ✅"), BLUE("PHONE HACK v19\n> camera turning on..."), BLUE("PHONE HACK v19\n> CAMERA ON! LIVE!"), BLUE("PHONE HACK v19\n> mic turning on..."), BLUE("PHONE HACK v19\n> tracing location..."), BLUE("PHONE HACK v19\n> location found!"), BLUE("PHONE HACK v19\n> HACK COMPLETE!"), "**♨️ DONE ♨️! COMPLETEE!**"])
@client.on(events.NewMessage(pattern=r"\.hackbank"))
async def hackbank(e): await blue_anim(e, [BLUE("BANK HACK v19\n> start..."), BLUE("BANK HACK v19\n> searching bank server..."), BLUE("BANK HACK v19\n> server found!"), BLUE("BANK HACK v19\n> firewall : STRONG!"), BLUE("BANK HACK v19\n> bypassing firewall... 25%"), BLUE("BANK HACK v19\n> bypassing firewall... 50%"), BLUE("BANK HACK v19\n> bypassing firewall... 75%"), BLUE("BANK HACK v19\n> FIREWALL BYPASSED! ✅"), BLUE("BANK HACK v19\n> searching account..."), BLUE("BANK HACK v19\n> account found!"), BLUE("BANK HACK v19\n> checking balance..."), BLUE("BANK HACK v19\n> balance : 10 CRORE!"), BLUE("BANK HACK v19\n> transferring money... 30%"), BLUE("BANK HACK v19\n> transferring money... 70%"), BLUE("BANK HACK v19\n> TRANSFER COMPLETE!"), "**😂 IT'S A PRANK! BANK HACK NAHI HOTA!**"])
@client.on(events.NewMessage(pattern=r"\.hackcctv"))
async def hackcctv(e): await blue_anim(e, [BLUE("CCTV HACK v19\n> start..."), BLUE("CCTV HACK v19\n> searching CCTV..."), BLUE("CCTV HACK v19\n> 10 camera found!"), BLUE("CCTV HACK v19\n> camera 1 connect..."), BLUE("CCTV HACK v19\n> camera 1 LIVE! ✅"), BLUE("CCTV HACK v19\n> camera 2 connect..."), BLUE("CCTV HACK v19\n> camera 2 LIVE! ✅"), BLUE("CCTV HACK v19\n> camera 3 connect..."), BLUE("CCTV HACK v19\n> camera 3 LIVE! ✅"), BLUE("CCTV HACK v19\n> all camera ON!"), BLUE("CCTV HACK v19\n> recording start..."), BLUE("CCTV HACK v19\n> detecting face..."), BLUE("CCTV HACK v19\n> face found!"), BLUE("CCTV HACK v19\n> HACK COMPLETE!"), "**😂 IT'S A PRANK! CCTV HACK NAHI HOTA AISE!**"])

# ================= MEGA LOVE + FUN =================
@client.on(events.NewMessage(pattern=r"\.megalove"))
async def megalove(e): await mega_anim(e, ["**🤍 HEART IS EMPTY...**", "**🤍 SOMEONE IS COMING IN HEART...**", "**💛 HEART IS BEATING...**", "**💛 HEART IS BEATING FAST...**", "**🧡 LOVE IS HAPPENING...**", "**🧡 LOVE IS GROWING...**", "**❤️ LOVE HAPPENED!**", "**❤️❤️ HEARTS MET!**", "**❤️❤️❤️ I LOVE YOU ❤️❤️❤️**", "**💍 WILL YOU MARRY ME? 😍**"])
@client.on(events.NewMessage(pattern=r"\.megavirus"))
async def megavirus(e):
    if not is_owner(e): await anim(e, ["**❌ CHECKING...**", "**❌ ONLY OWNER!**"]); return
    await mega_anim(e, ["**🦠 VIRUS LAB OPENING...**", "**🦠 MAKING VIRUS... 10%**", "**🦠 MAKING VIRUS... 30%**", "**🦠 MAKING VIRUS... 55%**", "**🦠 MAKING VIRUS... 80%**", "**🦠 VIRUS READY! ✅**", "**🦠 SENDING TO TARGET...**", "**🦠 VIRUS ENTERED!**", "**📱 PHONE HANGING...**", "**📱 PHONE HANG... 50%**", "**📱 PHONE HANG... 99%**", "**📱 PHONE SWITCHED OFF!**", "**📱 PHONE SWITCHED ON AGAIN!**", "**✅ VIRUS ATTACK COMPLETE!**\n**😂 IT'S A PRANK! No Virus!**"])
@client.on(events.NewMessage(pattern=r"\.megabomb"))
async def megabomb(e): await mega_anim(e, ["**💣 BOMB FOUND!**", "**💣 PLANTING BOMB...**", "**💣 BOMB PLANTED! RUN!**", "**💣 TIMER ON... 10**", "**💣 TIMER... 9**", "**💣 TIMER... 8**", "**💣 TIMER... 7**", "**💣 TIMER... 6**", "**💣 TIMER... 5**", "**💣 TIMER... 4**", "**💣 TIMER... 3**", "**💣 TIMER... 2**", "**💣 TIMER... 1**", "**💥💥 BOOM! 💥💥**", "**😂 IT'S A PRANK! NOTHING EXPLODED!**"])
@client.on(events.NewMessage(pattern=r"\.megapolice"))
async def megapolice(e): await mega_anim(e, ["**🚨 CALLING POLICE...**", "**🚨 POLICE IS COMING...**", "**🚓 POLICE CAR LEFT!**", "**🚓 POLICE CAR COMING... 50%**", "**🚓 POLICE IS HERE! RUN!**", "**🏃‍♂️ VILLAIN RAN AWAY! 😂**", "**😂 IT'S A PRANK! NO POLICE!**"])
@client.on(events.NewMessage(pattern=r"\.megapropose"))
async def megapropose(e): await mega_anim(e, ["**💌 I HAVE SOMETHING TO SAY...**", "**💌 MY HEART IS BEATING FAST...**", "**💌 I LIKE YOU FROM LONG TIME...**", "**🌹 TAKING ROSE...**", "**🌹 SITTING ON KNEES...**", "**💍 WILL YOU BE MY GIRLFRIEND? 💍**", "**❤️ SAY YES PLEASE! 😍**"])
@client.on(events.NewMessage(pattern=r"\.megaexam"))
async def megaexam(e): await mega_anim(e, ["**📚 EXAM IS COMING...**", "**📚 STUDY START... 10%**", "**📚 STUDY... 50% - FEELING SLEEPY!**", "**😴 SLEPT!**", "**⏰ WOKE UP ON EXAM DAY!**", "**📝 WRITING EXAM... I KNOW EVERYTHING!**", "**🏆 BECAME TOPPER! VILLAIN IS GENIUS! 😎**"])
@client.on(events.NewMessage(pattern=r"\.megaghost"))
async def megaghost(e): await mega_anim(e, ["**🌑 IT'S 12 AM...**", "**👻 SOMEONE IS COMING...**", "**👻 HEARING SOUND...**", "**👻 LOOK BEHIND!**", "**👻👻 GHOST IS HERE! RUN!**", "**🏃‍♂️ RUNNING...**", "**😂 IT'S A PRANK! NO GHOST!**"])
@client.on(events.NewMessage(pattern=r"\.megamoney"))
async def megamoney(e): await mega_anim(e, ["**💰 BANK OPENING...**", "**💰 LOCKER OPENING...**", "**💰 MONEY FOUND!**", "**💰💰 MONEY EVERYWHERE!**", "**💰💰💰 BECAME CROREPATI!**", "**🏎️ BOUGHT LAMBO!**", "**👑 VILLAIN IS RICH NOW! 😎**"])
@client.on(events.NewMessage(pattern=r"\.megafight"))
async def megafight(e): await mega_anim(e, ["**⚔️ FIGHT IS ABOUT TO START...**", "**👊 FIRST PUNCH!**", "**👊 SECOND PUNCH!**", "**🥊 OPPONENT FELL DOWN!**", "**🥊 OPPONENT GETTING UP...**", "**💥 FINAL PUNCH! BOOM!**", "**🏆 VILLAIN WON THE FIGHT! 👑**"])
@client.on(events.NewMessage(pattern=r"\.megabirthday"))
async def megabirthday(e): await mega_anim(e, ["**🎂 BIRTHDAY IS COMING...**", "**🎂 CAKE MAKING... 50%**", "**🎂 CAKE READY! 🎂**", "**🎈 BALLOONS ARE COMING...**", "**🎉 PARTY START! 🎉**", "**🎁 GIFT IS ALSO THERE!**", "**🎂🎉 HAPPY BIRTHDAY! 🎉🎂**"])
@client.on(events.NewMessage(pattern=r"\.megacrush"))
async def megacrush(e): await mega_anim(e, ["**👀 LOOKING AT CRUSH...**", "**👀 CRUSH SAW ME!**", "**😍 CRUSH SMILED!**", "**💌 WRITING MESSAGE...**", "**💌 MESSAGE SENT!**", "**✅ CRUSH REPLIED!**", "**❤️ CRUSH SAID YES! 😍**"])
@client.on(events.NewMessage(pattern=r"\.megaalien"))
async def megaalien(e): await mega_anim(e, ["**🛸 SOMETHING IN SKY...**", "**🛸 UFO IS COMING!**", "**👽 ALIEN LANDED!**", "**👽 ALIEN SAID - HELLO EARTH!**", "**👽 ALIEN TOOK VILLAIN!**", "**🌌 TRAVELLING IN SPACE!**", "**😂 IT'S A PRANK! NO ALIEN!**"])
@client.on(events.NewMessage(pattern=r"\.megajailbreak"))
async def megajailbreak(e): await mega_anim(e, ["**⛓️ I AM IN JAIL...**", "**🔑 FINDING KEY...**", "**🔑 KEY FOUND!**", "**🚪 OPENING DOOR...**", "**🏃‍♂️ RUNNING!**", "**🚓 POLICE BEHIND ME!**", "**✅ ESCAPED! VILLAIN IS FREE! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.megadon"))
async def megadon(e): await mega_anim(e, ["**👑 DON'S ENTRY...**", "**👑 DON IS HERE! EVERYONE SIDE!**", "**🕶️ WEARING SUNGLASSES...**", "**🚬 WALKING IN STYLE...**", "**🚓 POLICE BEHIND...**", "**💥 DON BEAT EVERYONE!**", "**👑 DON IS BACK! VILLAIN IS DON! 👑**"])
@client.on(events.NewMessage(pattern=r"\.megamafia"))
async def megamafia(e): await mega_anim(e, ["**😈 MAFIA MEETING START...**", "**😈 ALL DONS CAME...**", "**💰 DEAL HAPPENING... 50%**", "**💰 DEAL DONE! 10 CRORE!**", "**🔫 ENEMY CAME!**", "**🔫 FIGHT HAPPENED!**", "**👑 MAFIA KING - VILLAIN! 😈**"])
@client.on(events.NewMessage(pattern=r"\.megawedding"))
async def megawedding(e): await mega_anim(e, ["**💍 MARRIAGE FIXED!**", "**👰 BRIDE GETTING READY...**", "**🤵 GROOM GETTING READY...**", "**🎉 BARAT CAME!**", "**💃 DANCE AND MUSIC!**", "**💍 PHERE HAPPENING...**", "**❤️ MARRIAGE DONE! HAPPY MARRIED LIFE! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.megabreakup"))
async def megabreakup(e): await mega_anim(e, ["**💔 CALL COMING...**", "**💔 SHE SAID - WE NEED TO TALK...**", "**💔 BREAKUP DONE...**", "**😭 CRYING...**", "**🍺 FRIENDS CAME TO EXPLAIN...**", "**💪 MOVING ON...**", "**🔥 NOW VILLAIN IS SINGLE AND STRONG! 👑**"])
@client.on(events.NewMessage(pattern=r"\.megachai"))
async def megachai(e): await mega_anim(e, ["**☕ MAKING CHAI...**", "**☕ WATER HEATING...**", "**☕ ADDED CHAI PATTI...**", "**☕ ADDED MILK...**", "**☕ CHAI READY!**", "**☕ DRINKING CHAI... AHAA!**", "**☕ VILLAIN'S CHAI = BEST CHAI! 😎**"])
@client.on(events.NewMessage(pattern=r"\.megapizza"))
async def megapizza(e): await mega_anim(e, ["**🍕 ORDERING PIZZA...**", "**🍕 PIZZA MAKING...**", "**🍕 ADDING CHEESE...**", "**🍕 IN OVEN...**", "**🛵 DELIVERY BOY COMING...**", "**🍕 PIZZA CAME!**", "**🍕 EATING... SO TASTY! 😋**"])
@client.on(events.NewMessage(pattern=r"\.megacricket"))
async def megacricket(e): await mega_anim(e, ["**🏏 MATCH STARTING...**", "**🏏 VILLAIN CAME TO BAT!**", "**🏏 FIRST BALL - FOUR!**", "**🏏 SECOND BALL - SIX!**", "**🏏 THIRD BALL - SIX!**", "**🏏 CENTURY DONE! 💯**", "**🏆 VILLAIN WON THE MATCH! INDIA WON! 🇮🇳**"])
@client.on(events.NewMessage(pattern=r"\.megafootball"))
async def megafootball(e): await mega_anim(e, ["**⚽ MATCH START!**", "**⚽ BALL WITH VILLAIN...**", "**⚽ DRIBBLING...**", "**⚽ FOOLED DEFENDER!**", "**⚽ IN FRONT OF GOAL...**", "**⚽ GOALLLLL! ⚽**", "**🏆 VILLAIN SCORED GOAL! CHAMPION! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.megaschool"))
async def megaschool(e): await mega_anim(e, ["**🏫 GOING TO SCHOOL...**", "**😴 FEELING SLEEPY IN CLASS...**", "**👩‍🏫 TEACHER CAUGHT ME!**", "**📚 DIDN'T DO HOMEWORK...**", "**🏃‍♂️ LUNCH BREAK! RUN!**", "**😎 FUN WITH FRIENDS!**", "**🏠 SCHOOL OVER! GOING HOME! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.megaiphone"))
async def megaiphone(e): await mega_anim(e, ["**📱 NEW IPHONE LAUNCHING...**", "**📱 STANDING IN LINE...**", "**📱 MY NUMBER CAME!**", "**💳 CARD SWIPED...**", "**📱 IPHONE GOT!**", "**📸 TESTING CAMERA...**", "**📱 VILLAIN HAS NEW IPHONE 17 PRO! 😎**"])
@client.on(events.NewMessage(pattern=r"\.megasuperhero"))
async def megasuperhero(e): await mega_anim(e, ["**🦸 I AM NORMAL BOY...**", "**⚡ LIGHTNING FELL!**", "**🦸 POWER CAME!**", "**🦸 FLYING!**", "**🦸 SAVING PEOPLE!**", "**💥 BEAT ENEMY!**", "**🦸 VILLAIN IS NOW SUPERHERO! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.megazombie"))
async def megazombie(e): await mega_anim(e, ["**🧟 IT'S NIGHT... EVERYONE SLEEPING...**", "**🧟 HEARD SOUND...**", "**🧟 ZOMBIE CAME!**", "**🏃‍♂️ RUNNING!**", "**🧟 ZOMBIE BEHIND ME!**", "**🔫 KILLED ZOMBIE!**", "**✅ SURVIVED! VILLAIN IS ALIVE! 😎**"])

# ================= PRANK =================
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e): await anim_owner(e, [BLUE("HACKING START...\n[          ] 10%"), BLUE("HACKING...\n[████      ] 70%"), "**✅ HACK COMPLETE!**\n**DONE♨️!**"])
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e): await anim_owner(e, [BLUE("PRANK DDOS START..."), BLUE("SERVER GOING DOWN..."), "**✅ DONE!**\n**😂 IT'S A PRANK! No Attack Happened!**"])
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e): await anim_owner(e, [BLUE("TRACING..."), BLUE("LOCATION FOUND..."), "**😂 IT'S A PRANK! No Trace!**"])
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e): await anim_owner(e, [BLUE("MAKING VIRUS..."), BLUE("INJECTING VIRUS..."), "**😂 IT'S A PRANK! No Virus!**"])
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e): await anim_owner(e, [BLUE("OPENING DARKWEB..."), BLUE("CONNECTING..."), "**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e): await anim_owner(e, [BLUE("FINDING CCTV..."), BLUE("CAMERA FOUND..."), BLUE("LIVE FEED ON..."), "**😂 IT'S A PRANK! CCTV Cannot Be Hacked Like This!**"])
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e): await anim_owner(e, [BLUE("CONNECTING WHATSAPP... 25%"), BLUE("SCANNING CHAT... 60%"), "**✅ DONE!**\n**♨️DONNE♨️!**"])
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def phack(e): await anim_owner(e, [BLUE("HACKING PASSWORD..."), BLUE("CRACKING..."), "**✅ PASSWORD: `♨️` 😂**\n**DONE♨️!**"])
@client.on(events.NewMessage(pattern=r"\.location"))
async def location(e): await anim_owner(e, [BLUE("TRACING LOCATION..."), BLUE("CONNECTING SATELLITE..."), "**📍 LOCATION: IN YOUR HEART 😍**\n**♨️DONE♨️!**"])
@client.on(events.NewMessage(pattern=r"\.number"))
async def number(e): await anim_owner(e, [BLUE("TRACING NUMBER..."), BLUE("FINDING NAME..."), "**✅ Name: VILLAIN'S FRIEND 😎**\n**😂 IT'S A PRANK!**"])
@client.on(events.NewMessage(pattern=r"\.varius"))
async def varius(e): await anim_owner(e, [BLUE("MAKING VARIUS..."), BLUE("INJECTING VARIUS... 50%"), "**✅ VARIUS INJECTED!**\n**😂 JUST KIDDING! No Varius!**"])

# ================= MOVING ANIMATION 1 =================
@client.on(events.NewMessage(pattern=r"\.train"))
async def train(e): await mega_anim(e, ["**🚂 TRAIN AA RAHI HAI...**", "**🚂 TRAIN STATION PE HAI...**\n`🚂____`", "**🚂 TRAIN CHAL PADI!**\n`_🚂___`", "**🚂 TRAIN TEZ HO RAHI HAI!**\n`__🚂__`", "**🚂 TRAIN FULL SPEED!**\n`___🚂_`", "**🚂💨💨 TRAIN BHAG RAHI HAI!**\n`____🚂💨`", "**🚂💨💨💨 TRAIN NIKAL GAYI!**\n`_____🚂💨💨`", "**🚉 TRAIN NEXT STATION PE PAHUCH GAYI!**\n**🚂 VILLAIN EXPRESS! 😎**"])
@client.on(events.NewMessage(pattern=r"\.heartbig"))
async def heartbig(e): await mega_anim(e, ["**🤍 DIL KHALI HAI...**", "**🤍 DIL ME KOI AA RAHA HAI...**", "**💛 DIL DHADAK RAHA HAI...**\n`🤍 💛`", "**💛🧡 DIL TEZ DHADAK RAHA HAI...**\n`🤍 💛 🧡`", "**🧡❤️ DIL FULL HO GAYA!**\n`🤍 💛 🧡 ❤️`", "**❤️❤️ DIL SE DIL MIL GAYA!**\n`❤️❤️❤️`", "**❤️❤️❤️❤️ LOVE HO GAYA!**", "**💍 I LOVE YOU! WILL YOU MARRY ME? 😍**"])
@client.on(events.NewMessage(pattern=r"\.fightbig"))
async def fightbig(e): await mega_anim(e, ["**⚔️ FIGHT START HONE WALI HAI...**", "**🥊 DONO SAMNE AA GAYE!**\n`🥊      🥊`", "**🥊 PEHLA PUNCH!**\n`🥊💥  🥊`", "**🥊 DUSRA PUNCH!**\n`🥊  💥🥊`", "**🥊 TEESRA PUNCH - ZOR SE!**\n`🥊💥💥🥊`", "**😵 OPPONENT GIR GAYA!**\n`🥊  😵`", "**🥊 OPPONENT UTH RAHA HAI...**\n`🥊  🧍`", "**💥 FINAL PUNCH! BOOM!**\n`🥊💥💥💥😵`", "**🏆 VILLAIN NE FIGHT JEET LI! 👑**"])
@client.on(events.NewMessage(pattern=r"\.rocket"))
async def rocket(e): await mega_anim(e, ["**🚀 ROCKET TAYAR HAI...**", "**🚀 FUEL BHAR RAHA HAI... 50%**", "**🚀 COUNTDOWN START... 5**", "**🚀 COUNTDOWN... 4**", "**🚀 COUNTDOWN... 3**", "**🚀 COUNTDOWN... 2**", "**🚀 COUNTDOWN... 1**", "**🚀🚀 ROCKET UD GAYA!**\n`🚀`", "**🚀🌌 ROCKET SPACE ME HAI!**\n`  🚀`", "**🌕 CHAND PE PAHUCH GAYA!**\n**🚀 VILLAIN ON MOON! 😎**"])
@client.on(events.NewMessage(pattern=r"\.carrace"))
async def carrace(e): await mega_anim(e, ["**🏁 RACE START HONE WALI HAI...**", "**🏎️ CAR 1 READY!**\n`🏎️___`", "**🏎️ CAR 2 READY!**\n`🏎️___\n🚗___`", "**🏁 3...2...1... GO!**", "**🏎️ CAR 1 AAGE!**\n`_🏎️__\n__🚗_`", "**🚗 CAR 2 AAGE NIKAL GAYI!**\n`__🏎️_\n_🚗__`", "**🏎️💨 VILLAIN KI CAR TEZ!**\n`___🏎️💨\n__🚗_`", "**🏎️💨💨 VILLAIN JEET GAYA!**\n`_____🏎️🏆`", "**🏆 VILLAIN IS RACE CHAMPION! 🏎️🔥**"])
@client.on(events.NewMessage(pattern=r"\.plane"))
async def plane(e): await mega_anim(e, ["**✈️ PLANE AIRPORT PE HAI...**", "**✈️ PLANE RUNWAY PE HAI...**\n`✈️____`", "**✈️ PLANE CHAL PADA!**\n`_✈️___`", "**✈️ PLANE UD RAHA HAI!**\n`__✈️__`", "**✈️☁️ PLANE BADALO ME HAI!**\n`___✈️☁️`", "**✈️🌍 PLANE DUSRE DESH JA RAHA HAI!**", "**🛬 PLANE LAND HO GAYA!**", "**✈️ VILLAIN DUBAI PAHUCH GAYA! 😎**"])
@client.on(events.NewMessage(pattern=r"\.bike"))
async def bike(e): await mega_anim(e, ["**🏍️ BIKE START HO RAHI HAI...**", "**🏍️ BIKE CHAL PADI!**\n`🏍️___`", "**🏍️ BIKE TEZ HO RAHI HAI!**\n`_🏍️__`", "**🏍️💨 BIKE FULL SPEED!**\n`__🏍️💨`", "**🏍️💨💨 BIKE UD RAHI HAI!**\n`___🏍️💨💨`", "**🏍️ WHEELIE MAR RAHA HU!**\n`🏍️⬆️`", "**🏍️💨💨💨 VILLAIN NIKAL GAYA!**", "**🏍️ VILLAIN RIDER! KING OF ROAD! 👑**"])
@client.on(events.NewMessage(pattern=r"\.cycle"))
async def cycle(e): await mega_anim(e, ["**🚲 CYCLE NIKALI...**", "**🚲 CYCLE CHAL PADI!**\n`🚲___`", "**🚲 CYCLE TEZ HO RAHI HAI!**\n`_🚲__`", "**🚲💨 CYCLE FULL SPEED!**\n`__🚲💨`", "**🚲 GIR GAYA! 😂**\n`🚲😵`", "**🚲 FIR UTHA!**\n`🚲🧍`", "**🚲 PHIR CHAL PADI!**", "**🚲 VILLAIN CYCLE CHAMPION! 😎**"])
@client.on(events.NewMessage(pattern=r"\.ship"))
async def shipanim(e): await mega_anim(e, ["**🚢 SHIP PORT PE HAI...**", "**🚢 SHIP CHAL PADA!**\n`🚢___`", "**🚢 SHIP SAMUNDAR ME HAI!**\n`_🚢🌊`", "**🚢🌊🌊 TOOFAN AA GAYA!**", "**🚢🌊 SHIP HIL RAHA HAI!**", "**🚢 TOOFAN SE BACH GAYA!**", "**🏝️ ISLAND MIL GAYA!**", "**🚢 VILLAIN KO KHAZANA MIL GAYA! 💰**"])
@client.on(events.NewMessage(pattern=r"\.runbig"))
async def runbig(e): await mega_anim(e, ["**🏃 BHAGNA START...**", "**🏃 BHAG RAHA HU!**\n`🏃___`", "**🏃‍♂️💨 TEZ BHAG RAHA HU!**\n`_🏃‍♂️💨_`", "**🏃‍♂️💨💨 FULL SPEED!**\n`__🏃‍♂️💨💨`", "**🐕 KUTTA PEECHE PAD GAYA!**\n`__🏃‍♂️💨🐕`", "**🏃‍♂️💨💨💨 AUR TEZ!**\n`___🏃‍♂️💨💨🐕`", "**🏃‍♂️ BACH GAYA!**", "**🏃 VILLAIN IS FASTEST RUNNER! 😂**"])

# ================= MOVING ANIMATION 2 - 15 NAYE =================
@client.on(events.NewMessage(pattern=r"\.bus"))
async def bus(e): await mega_anim(e, ["**🚌 BUS AA RAHI HAI...**", "**🚌 BUS STOP PE HAI...**\n`🚌___`", "**🚌 BUS CHAL PADI!**\n`_🚌__`", "**🚌💨 BUS TEZ HO RAHI HAI!**\n`__🚌💨`", "**🚌💨💨 BUS BHAG RAHI HAI!**\n`___🚌💨💨`", "**🚌 BUS PAHUCH GAYI!**", "**🚌 VILLAIN BUS ME! 😎**"])
@client.on(events.NewMessage(pattern=r"\.policechase"))
async def policechase(e): await mega_anim(e, ["**🏃 CHOR BHAG RAHA HAI!**", "**🏃‍♂️💨 CHOR BHAG RAHA HAI!**\n`🏃‍♂️___`", "**🚓 POLICE PEECHE AA GAYI!**\n`🏃‍♂️__🚓`", "**🏃‍♂️💨🚓 PEECHA CHAL RAHA HAI!**\n`_🏃‍♂️💨_🚓`", "**🏃‍♂️💨💨 CHOR TEZ!**\n`__🏃‍♂️💨🚓💨`", "**🚓 POLICE NE PAKAD LIYA!**\n`🚓😵`", "**👮 CHOR JAIL ME! 😂**", "**👮 VILLAIN POLICE! CHOR PAKDA GAYA!**"])
@client.on(events.NewMessage(pattern=r"\.cricketbig"))
async def cricketbig(e): await mega_anim(e, ["**🏏 MATCH START!**", "**🏏 BOWLER BALL DAL RAHA HAI...**\n`🏏___🏐`", "**🏏 BALL AA RAHI HAI!**\n`🏏_🏐_`", "**🏏 BATSMAN NE MARA!**\n`🏏💥🏐`", "**🏐💨 BALL UD RAHI HAI!**\n`__🏐💨`", "**🏐 BALL BOUNDARY KE BAHAR!**", "**🏏 SIX! SIX! SIX! 🎉**", "**🏆 VILLAIN NE SIX MARA! 💯**"])
@client.on(events.NewMessage(pattern=r"\.footballbig"))
async def footballbig(e): await mega_anim(e, ["**⚽ MATCH START!**", "**⚽ BALL MERE PAAS HAI...**\n`⚽___`", "**⚽ DRIBBLING KAR RAHA HU...**\n`_⚽__`", "**⚽ DEFENDER KO CHAKMA DIYA!**\n`__⚽💨`", "**⚽ GOAL KE SAMNE HU!**\n`___⚽🥅`", "**⚽💥 SHOT MARA!**\n`___💥🥅`", "**⚽ GOALLLLL! ⚽**", "**🏆 VILLAIN NE GOAL MARA! 🎉**"])
@client.on(events.NewMessage(pattern=r"\.firebig"))
async def firebig(e): await mega_anim(e, ["**🔥 AAG LAG RAHI HAI...**\n`🔥`", "**🔥♨️🔥 AAG BADH RAHI HAI!**\n`🔥♨️🔥`", "**🔥♨️🔥♨️🔥 AAG FAIL RAHI HAI!**\n`🔥🔥🔥`", "**🔥🔥🔥🔥 PURA JAL RAHA HAI!**\n`🔥🔥🔥🔥`", "**🧯 FIRE BRIGADE AA GAYI!**", "**💧 PANI DAL RAHA HU...**", "**✅ AAG BUJH GAYI!**", "**🔥 VILLAIN NE AAG BUJHA DI! 😎**"])
@client.on(events.NewMessage(pattern=r"\.rainbig"))
async def rainbig(e): await mega_anim(e, ["**☁️ BADAL AA RAHE HAI...**", "**☁️☁️ BADAL CHHA GAYE!**", "**🌧️ BARISH START!**\n`🌧️`", "**🌧️🌧️ TEZ BARISH!**\n`🌧️🌧️`", "**⛈️🌧️ TOOFAN + BARISH!**\n`⛈️🌧️🌧️`", "**☔ CHHATA KHOLA!**", "**🌈 BARISH RUK GAYI! INDRADHANUSH!**", "**🌈 VILLAIN NE BARISH ENJOY KI! ☔**"])
@client.on(events.NewMessage(pattern=r"\.snake"))
async def snake(e): await mega_anim(e, ["**🐍 SAAP AA RAHA HAI...**", "**🐍 SAAP RENG RAHA HAI...**\n`🐍___`", "**🐍 SAAP AAGE BADH RAHA HAI...**\n`_🐍__`", "**🐍 SAAP TEZ HO GAYA!**\n`__🐍💨`", "**🐍 SAAP NE KAAT LIYA!**\n`🐍💥😵`", "**😵 BANDA GIR GAYA!**", "**🏥 HOSPITAL LE JAO!**", "**🐍 VILLAIN KA SAAP! 😂**"])
@client.on(events.NewMessage(pattern=r"\.catdog"))
async def catdog(e): await mega_anim(e, ["**🐱 BILLI AA RAHI HAI...**", "**🐶 KUTTA AA RAHA HAI...**\n`🐱_🐶`", "**🐱🐶 DONO SAMNE AA GAYE!**", "**🐶 KUTTA BHONK RAHA HAI!**\n`🐱_🐶💥`", "**🐱 BILLI BHAG RAHI HAI!**\n`🐱💨_🐶`", "**🐶 KUTTA PEECHE BHAG RAHA HAI!**\n`🐱💨🐶💨`", "**🐱 BILLI PED PE CHADH GAYI!**", "**🐱🐶 DONO DOST BAN GAYE! 😂**"])
@client.on(events.NewMessage(pattern=r"\.pubg"))
async def pubg(e): await mega_anim(e, ["**🪂 PLANE SE KOOD GAYA!**", "**🪂 HAVA ME HU!**\n`🪂`", "**🪂 NEEMCHE UTAR RAHA HU!**\n`_🪂_`", "**🪂 LAND HO GAYA!**", "**🔫 GUN MIL GAYI!**", "**🔫 ENEMY AA GAYA!**\n`🔫💥😵`", "**🔫 ENEMY KO MAR DIYA!**", "**🏆 WINNER WINNER CHICKEN DINNER! 🍗**"])
@client.on(events.NewMessage(pattern=r"\.moneyfly"))
async def moneyfly(e): await mega_anim(e, ["**💰 PAISA AA RAHA HAI...**", "**💰 PAISA UDD RAHA HAI!**\n`💰___`", "**💰💰 PAISA BARAS RAHA HAI!**\n`💰💰`", "**💰💰💰 PURA PAISA HI PAISA!**\n`💰💰💰`", "**💰 PAISE PAKAD RAHA HU!**", "**💰💰💰 AMIR HO GAYA!**", "**🏎️ LAMBO KHARID LI!**", "**👑 VILLAIN CROREPATI! 😎**"])
@client.on(events.NewMessage(pattern=r"\.dancebig"))
async def dancebig(e): await mega_anim(e, ["**🎵 MUSIC START...**", "**🕺 DANCE START!**\n`🕺`", "**💃🕺 DONO DANCE KAR RAHE HAI!**\n`💃🕺`", "**🕺💃🕺 TEEN LOG DANCE!**\n`🕺💃🕺`", "**💃🕺💃🕺 FULL PARTY!**\n`💃🕺💃🕺`", "**🎉🎉 DJ BAJA RAHA HAI!**", "**🕺💃 SAB NAACH RAHE HAI!**", "**🎉 VILLAIN KI PARTY! 🔥**"])
@client.on(events.NewMessage(pattern=r"\.maggi"))
async def maggi(e): await mega_anim(e, ["**🍜 MAGGI BANANI HAI...**", "**🍜 PANI GARAM HO RAHA HAI...**", "**🍜 MAGGI DAL DI!**\n`🍜`", "**🍜 MASALA DALA!**", "**🍜 MAGGI BAN RAHI HAI... 50%**", "**🍜 MAGGI BAN GAYI!**", "**🍜 KHA RAHA HU... SO TASTY!**", "**🍜 VILLAIN KI MAGGI - 2 MINUTE! 😋**"])
@client.on(events.NewMessage(pattern=r"\.thief"))
async def thief(e): await mega_anim(e, ["**🌑 RAAT HAI... SAB SO RAHE HAI...**", "**🥷 CHOR AA GAYA!**\n`🥷___`", "**🥷 CHOR GHAR ME GHUSA!**\n`_🥷__`", "**🥷 CHOR CHORI KAR RAHA HAI!**\n`🥷💰`", "**💡 LIGHT ON HO GAYI!**", "**🥷 CHOR PAKDA GAYA!**\n`🥷😵`", "**🚓 POLICE LE GAYI!**", "**🥷 VILLAIN NE CHOR PAKDA! 😎**"])
@client.on(events.NewMessage(pattern=r"\.ghostrun"))
async def ghostrun(e): await mega_anim(e, ["**🌑 RAAT KE 12 BAJE...**", "**👻 BHOOT AA GAYA!**\n`👻___`", "**👻 BHOOT PEECHE AA RAHA HAI!**\n`🏃_👻`", "**🏃 ME BHAG RAHA HU!**\n`🏃💨_👻`", "**🏃‍♂️💨 TEZ BHAG RAHA HU!**\n`🏃‍♂️💨👻💨`", "**🏃‍♂️ GHAR PAHUCH GAYA!**", "**🚪 DARWAZA BAND KAR DIYA!**", "**😂 BHOOT BAHAR REH GAYA! VILLAIN BACH GAYA!**"])
@client.on(events.NewMessage(pattern=r"\.lovefly"))
async def lovefly(e): await mega_anim(e, ["**💌 CHITTHI LIKH RAHA HU...**", "**💌 CHITTHI UD RAHI HAI...**\n`💌___`", "**💌 CHITTHI JA RAHI HAI...**\n`_💌__`", "**💌 CHITTHI PAHUCH GAYI!**\n`__💌❤️`", "**❤️ USNE PADH LI!**", "**❤️ USNE HAAN BOL DIYA!**", "**💍 SHADI PAKKI!**", "**❤️ VILLAIN KO PYAAR MIL GAYA! 😍**"])

print("VILLAIN V19 STARTED! 🔥")
client.start()
client.run_until_disconnected()
