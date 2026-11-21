import os, random, time, datetime, asyncio, string
from flask import Flask
import threading
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ===== RENDER PORT FIX =====
app = Flask(__name__)
@app.route('/')
def home():
    return "VILLAIN BOT IS ALIVE!"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
threading.Thread(target=run_web, daemon=True).start()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
ALIVE_PIC = "photo_2026-11-21_19-54-14.jpg"
START = time.time()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# ===== SUDO SYSTEM =====
SUDO_USERS = set()
def is_owner(e):
    if e.outgoing: return True
    if OWNER_ID != 0 and e.sender_id == OWNER_ID: return True
    if OWNER_ID == 0: return True
    return False
def is_sudo(e):
    return e.sender_id in SUDO_USERS
def is_hack_blocked_for_sudo(e):
    # Sudo walo ke liye Hack + Sudo commands BLOCK
    return is_sudo(e) and not is_owner(e)

JOKES = ["Teacher: Kal homework kyu nahi kiya? Student: Sir light chali gayi thi 😂","Pappu: Mummy 100 me se 100 mile! Mummy: Kis me? Pappu: 50 maths, 50 science 😂","Ek aadmi doctor ke paas gaya, bola mujhe sab 2-2 dikhta hai. Doctor: Baitho, tum 4 log ek saath mat baitho 😂"]
QUOTES = ["Jeetne wale alag cheez nahi karte, wo cheezo ko alag tarike se karte hai.","Mehnat itni khamoshi se karo ki safalta shor macha de.","Villain banna aasaan hai, legend banna mushkil hai."]
FACTS = ["Honey kabhi kharab nahi hota, 3000 saal purana honey bhi khane layak mila hai.","Octopus ke 3 dil hote hai.","Tumhare dimaag me 86 billion neurons hote hai."]
SHAYARI = ["Hum villain hai sahab, hero wali acting humse nahi hoti 🔥","Log kehte hai badal gaya hu, maine kaha pehle bhi aisa hi tha 😈","Jalnewalo ki dua se hi to aaj itni roshni hai meri ✨"]
ATTITUDE = ["Meri khamoshi ko kamzori mat samajh, ye toofan se pehle ki shanti hai 😈","Hum jahan khade hote hai, wahan se line shuru hoti hai 🔥","Bhid me khada hona mera kaam nahi, bhid jiske liye khadi hai wo hu mai 👑"]
ROASTS = ["Tera attitude to aisa hai jaise 2G me 5G ki baat kar raha ho 😂","Bhai tu itna slow hai, Google bhi tujhe search karne se mana kar deta hai 😂","Teri shakal dekh ke to WiFi bhi disconnect ho jaye 😂"]
RAIDS = ["Oye chup kar, teri awaaz se to speaker phat jayega 😂","Tu itna bolta hai, mute button bhi sharma jaye 😂","Bhai tu rehne de, tujhse na ho payega 😂"]
PICKUPS = ["Tumhare papa chor hai kya? Kyunki unhone saare taare chura ke tumhari aankhon me daal diye 😍","Kya tum WiFi ho? Kyunki mai tumse connect ho raha hu ❤️","Tum smile mat karo, dil attack aa jayega 😘"]
DARKJOKES = ["Mera wifi itna slow hai ki lagta hai usne bhi jeene ki umeed chhod di hai 😂","Zindagi me itna akela hu ki Google bhi kehta hai 'Did you mean: koi nahi hai tera' 😂","Meri kismat itni kharab hai, chai me bhi biscuit doob ke mar jata hai 😂"]
INSULTS = ["You are the reason the gene pool needs a lifeguard 😂","You're like a cloud, when you disappear the day gets beautiful 😂","Your brain is like WiFi, everyone can see it but no one can connect 😂"]
TRUTH2 = ["Kabhi teacher se jhooth bola hai?","Apna sabse bada secret batao?","Kisi ko stalk kiya hai kabhi?"]
DARE2 = ["Apne last chat ka screenshot bhejo!","Apne crush ko I Love You likh ke bhejo!","Apni gallery ki 3rd photo bhejo!"]
MEMES2 = ["Jab mummy bole 'beta 2 min me aaya' aur 2 ghante ho jaye 😂","Jab exam me sab kuch aata ho par kuch yaad na ho 😭","Jab WiFi band ho aur data bhi khatam 😭"]

def uptime():
    s = int(time.time()-START)
    return f"{s//3600}h {s%3600//60}m {s%60}s"

# ===== SUDO COMMANDS - SIRF OWNER =====
@client.on(events.NewMessage(pattern=r"\.addsudo"))
async def addsudo(e):
    if not is_owner(e): return
    reply = await e.get_reply_message()
    if reply:
        uid = reply.sender_id
        SUDO_USERS.add(uid)
        await e.reply(f"**✅ SUDO ADD HO GAYA!**\n**ID:** `{uid}`\nAb ye banda tera bot chala payega! (Hack wale chod ke) 😎")
    else:
        await e.reply("**Use:** Kisi ke msg pe reply karke `.addsudo` likh!")
    try: await e.delete()
    except: pass

@client.on(events.NewMessage(pattern=r"\.remsudo"))
async def remsudo(e):
    if not is_owner(e): return
    reply = await e.get_reply_message()
    if reply:
        uid = reply.sender_id
        SUDO_USERS.discard(uid)
        await e.reply(f"**❌ SUDO HATA DIYA!**\n**ID:** `{uid}`\nAb ye banda bot nahi chala payega!")
    else:
        await e.reply("**Use:** Kisi ke msg pe reply karke `.remsudo` likh!")
    try: await e.delete()
    except: pass

@client.on(events.NewMessage(pattern=r"\.sudolist"))
async def sudolist(e):
    if not is_owner(e): return
    if not SUDO_USERS:
        await e.reply("**📋 SUDO LIST KHALI HAI!**\nKoi sudo nahi hai abhi.")
    else:
        txt = "**📋 SUDO LIST:**\n"
        for uid in SUDO_USERS:
            txt += f"- `{uid}`\n"
        txt += "\nYe sab tera bot chala sakte hai (Hack wale chod ke) ✅"
        await e.reply(txt)
    try: await e.delete()
    except: pass

# ===== BASIC =====
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    txt = "**⚡ VILLAIN USR BOT IS ALIVE! ⚡**\n\n**👑 OWNER :** VILLAIN\n**🔥 STATUS :** ONLINE\n**💀 MODE :** VILLAIN MODE ON\n**⚙️ VERSION :** V8.0 SUDO\n**⏱️ UPTIME :** "+uptime()+"\n**📦 COMMANDS :** 160+\n**👥 SUDO :** "+str(len(SUDO_USERS))+" Users\n\n**😈 AB RAJ KAREGA VILLAIN!**"
    if os.path.exists(ALIVE_PIC):
        await e.reply(file=ALIVE_PIC, message=txt)
    else:
        await e.reply(txt)
    try: await e.delete()
    except: pass

@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await e.reply("**🏓 PONG! VILLAIN IS HERE! 🔥**")
@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await e.reply(
        "**🔥 《 VILLAIN 》 V8.0 SUDO ALL COMMANDS 🔥**\n\n"
        "**SUDO (Sirf Owner):** .addsudo .remsudo .sudolist\n\n"
        "**Basic:** .ping .alive .help .id .info .userinfo .time .date .version .bot .owner .uptime .profile .stats .backup\n\n"
        "**Fun:** .joke .quote .fact .shayari .attitude .roast .roastme .truth .dare .truth2 .dare2 .compliment .meme .meme2 .happy .sad .love .hi .bye .good .slap .kiss .hug .ship .gay .cute .pickup .flirt .insult .darkjoke\n\n"
        "**Game:** .dice .coin .luck .guess .crush .lovecalc .future .horoscope .dream .propose .breakup .bff\n\n"
        "**Style:** .echo .shout .bold .reverse .font .bio .caption .hashtag .dp .wallpaper .sticker\n\n"
        "**Kaam:** .calc .qr .pass .note .notes .todo .save .translate .ask .weather .news .screenshot .timer .reminder .play .lyrics .yt .crypto .pincode .ifsc .wiki .google .translate2 .tts .qr2 .password2 .email .anime .imdb .songdl .insta .ytmp3\n\n"
        "**Pro:** .ip .whois .short .qrphoto .pdf .vcard\n\n"
        "**Auto:** .afk .back .autoreact .autoreply .autopin .autodelete .typing .online\n\n"
        "**Prank:** .hack .fakeid .wasted .spam .raid\n\n"
        "**Hacker Fake Prank (Sirf Owner):** .hack2 .ddos .trace .passwordhack .virus .darkweb .cctv .whatsapp\n\n"
        "**Group King:** .tagall .purge .kick .ban .unban .promote .demote .block .unblock .rules .welcome .goodmorning .goodnight .birthday\n\n"
        "**Villain Special:** .afk [wajah] .sus .top .vs\n\n"
        "**Villain Special 2.0:** .jail .free .kill .revive .wanted .gang\n\n"
        "**Extra:** .tea .coffee .song .movie .study .gym .sleep .name .age\n\n"
        "**👑 VILLAIN USR BOT V8.0 SUDO**"
    )
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e): await e.reply(f"**🆔 Teri ID:** `{e.sender_id}`")
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    u = await e.get_sender()
    await e.reply(f"**👤 INFO:**\n**Name:** {u.first_name}\n**Username:** @{u.username}\n**ID:** `{u.id}`")
@client.on(events.NewMessage(pattern=r"\.userinfo"))
async def userinfo(e):
    u = await e.get_sender()
    await e.reply(f"**👤 USERINFO:**\n**Name:** {u.first_name} {u.last_name or ''}\n**Username:** @{u.username}\n**ID:** `{u.id}`\n**Bot:** {u.bot}\n**Verified:** {u.verified}")
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await e.reply(f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')}")
@client.on(events.NewMessage(pattern=r"\.date"))
async def datec(e): await e.reply(f"**📅 DATE:** {datetime.datetime.now().strftime('%d-%m-%Y')}")
@client.on(events.NewMessage(pattern=r"\.version"))
async def ver(e): await e.reply("**⚡ VILLAIN USR BOT V8.0 SUDO**")
@client.on(events.NewMessage(pattern=r"\.bot"))
async def botc(e): await e.reply("**🤖 Haan bhai, VILLAIN BOT ONLINE hai!**")
@client.on(events.NewMessage(pattern=r"\.owner"))
async def owner(e): await e.reply("**👑 OWNER: VILLAIN 😈**")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await e.reply(f"**⏱️ UPTIME:** {uptime()}")
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e):
    u = await e.get_sender()
    await e.reply(f"**👑 PROFILE:**\n**Name:** {u.first_name}\n**Username:** @{u.username}\n**ID:** `{u.id}`\n**Bio:** VILLAIN VIBES 😈🔥")
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await e.reply(f"**📊 STATS:**\n**Uptime:** {uptime()}\n**Commands:** 160+\n**Sudo Users:** {len(SUDO_USERS)}\n**Status:** ONLINE 🔥")
@client.on(events.NewMessage(pattern=r"\.backup"))
async def backup(e): await e.reply("**💾 BACKUP HO GAYA! Saara data safe hai! ✅**")

# ===== FUN =====
@client.on(events.NewMessage(pattern=r"\.joke"))
async def joke(e): await e.reply(f"**😂 JOKE:**\n{random.choice(JOKES)}")
@client.on(events.NewMessage(pattern=r"\.quote"))
async def quote(e): await e.reply(f"**💭 QUOTE:**\n{random.choice(QUOTES)}")
@client.on(events.NewMessage(pattern=r"\.fact"))
async def fact(e): await e.reply(f"**🧠 FACT:**\n{random.choice(FACTS)}")
@client.on(events.NewMessage(pattern=r"\.shayari"))
async def shayari(e): await e.reply(f"**✨ SHAYARI:**\n{random.choice(SHAYARI)}")
@client.on(events.NewMessage(pattern=r"\.attitude"))
async def att(e): await e.reply(f"**😈 ATTITUDE:**\n{random.choice(ATTITUDE)}")
@client.on(events.NewMessage(pattern=r"\.roast"))
async def roast(e): await e.reply(f"**🔥 ROAST:**\n{random.choice(ROASTS)}")
@client.on(events.NewMessage(pattern=r"\.roastme"))
async def roastme(e): await e.reply(f"**🔥 ROAST ME:**\n{random.choice(ROASTS)}")
@client.on(events.NewMessage(pattern=r"\.truth"))
async def truth(e): await e.reply("**🤔 TRUTH:** Kabhi kisi ka dil dukhaya hai sach-sach batao?")
@client.on(events.NewMessage(pattern=r"\.dare"))
async def dare(e): await e.reply("**😈 DARE:** Apne crush ko 'Hi' likh ke bhejo abhi!")
@client.on(events.NewMessage(pattern=r"\.truth2"))
async def truth2(e): await e.reply(f"**🤔 TRUTH2:** {random.choice(TRUTH2)}")
@client.on(events.NewMessage(pattern=r"\.dare2"))
async def dare2(e): await e.reply(f"**😈 DARE2:** {random.choice(DARE2)}")
@client.on(events.NewMessage(pattern=r"\.insult"))
async def insult(e): await e.reply(f"**🤬 INSULT:**\n{random.choice(INSULTS)}")
@client.on(events.NewMessage(pattern=r"\.darkjoke"))
async def darkjoke(e): await e.reply(f"**🌑 DARK JOKE:**\n{random.choice(DARKJOKES)}")
@client.on(events.NewMessage(pattern=r"\.compliment"))
async def comp(e): await e.reply("**🥰 Tu bohot smart aur cool hai yaar! ✨**")
@client.on(events.NewMessage(pattern=r"\.meme"))
async def meme(e): await e.reply("**😂 MEME:** Jab teacher bole 'kal test hai' aur tumne kuch padha hi nahi 😭")
@client.on(events.NewMessage(pattern=r"\.meme2"))
async def meme2(e): await e.reply(f"**😂 MEME2:**\n{random.choice(MEMES2)}")
@client.on(events.NewMessage(pattern=r"\.happy"))
async def happy(e): await e.reply("**😊 Aaj mood ekdum happy happy hai! 🥳**")
@client.on(events.NewMessage(pattern=r"\.sad"))
async def sad(e): await e.reply("**😔 Thoda sad hu yaar, ek gaana suna de...**")
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await e.reply("**❤️ Love you yaar, dil se! 🥰**")
@client.on(events.NewMessage(pattern=r"\.hi"))
async def hi(e): await e.reply("**👋 Hii! Kaise ho? 😊**")
@client.on(events.NewMessage(pattern=r"\.bye"))
async def bye(e): await e.reply("**👋 Bye bye! Phir milenge! 😊**")
@client.on(events.NewMessage(pattern=r"\.good"))
async def good(e): await e.reply("**😇 Good Good! Sab badhiya hai!**")
@client.on(events.NewMessage(pattern=r"\.slap"))
async def slap(e): await e.reply("**👋 SLAP!**\n*THAPPAD MARA!* 😂🤣")
@client.on(events.NewMessage(pattern=r"\.kiss"))
async def kiss(e): await e.reply("**😘 KISS! Muahhh! ❤️**")
@client.on(events.NewMessage(pattern=r"\.hug"))
async def hug(e): await e.reply("**🤗 HUG! Bada wala hug! 🫶**")
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await e.reply(f"**💞 SHIP:**\nTum dono ki jodi {random.randint(70,99)}% match hai! ❤️🔥 Shaadi kab hai?")
@client.on(events.NewMessage(pattern=r"\.gay"))
async def gay(e): await e.reply(f"**🌈 GAY METER:** {random.randint(1,100)}% 😂")
@client.on(events.NewMessage(pattern=r"\.cute"))
async def cute(e): await e.reply(f"**🥰 CUTE METER:** {random.randint(80,100)}% - Tu to bohot cute hai! 😍")
@client.on(events.NewMessage(pattern=r"\.pickup"))
async def pickup(e): await e.reply(f"**😍 PICKUP LINE:**\n{random.choice(PICKUPS)}")
@client.on(events.NewMessage(pattern=r"\.flirt"))
async def flirt(e): await e.reply(f"**😘 FLIRT:**\n{random.choice(PICKUPS)}")

# ===== GAME =====
@client.on(events.NewMessage(pattern=r"\.dice"))
async def dice(e): await e.reply(f"**🎲 DICE:** {random.randint(1,6)}")
@client.on(events.NewMessage(pattern=r"\.coin"))
async def coin(e): await e.reply(f"**🪙 COIN:** {random.choice(['HEADS','TAILS'])}")
@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await e.reply(f"**🍀 LUCK:** {random.randint(1,100)}%")
@client.on(events.NewMessage(pattern=r"\.guess"))
async def guess(e): await e.reply(f"**🤔 GUESS:** Maine {random.randint(1,10)} socha tha!")
@client.on(events.NewMessage(pattern=r"\.crush"))
async def crush(e): await e.reply("**💘 CRUSH:** Tera crush bhi tujhe hi dekh raha hai 👀")
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await e.reply(f"**💞 LOVE CALC:** {random.randint(60,99)}% MATCH! ❤️")
@client.on(events.NewMessage(pattern=r"\.future"))
async def future(e): await e.reply("**🔮 FUTURE:** Tera future ekdum bright hai, VILLAIN banega tu! 🔥")
@client.on(events.NewMessage(pattern=r"\.horoscope"))
async def horo(e): await e.reply("**♈ HOROSCOPE:** Aaj ka din tera hai, koi bada kaam hoga!")
@client.on(events.NewMessage(pattern=r"\.dream"))
async def dream(e): await e.reply("**💭 DREAM:** Sapne bade dekho, VILLAIN wale! 😈")
@client.on(events.NewMessage(pattern=r"\.propose"))
async def propose(e): await e.reply("**💍 Will you be my Valentine? ❤️🥺**")
@client.on(events.NewMessage(pattern=r"\.breakup"))
async def breakup(e): await e.reply("**💔 Breakup ho gaya? Koi nahi, VILLAIN kabhi rota nahi! 🔥**")
@client.on(events.NewMessage(pattern=r"\.bff"))
async def bff(e): await e.reply("**👯 BFF FOREVER! Tu mera sabse best hai! 🫶**")

# ===== STYLE =====
@client.on(events.NewMessage(pattern=r"\.echo (.+)"))
async def echo(e): await e.reply(e.pattern_match.group(1))
@client.on(events.NewMessage(pattern=r"\.shout (.+)"))
async def shout(e): await e.reply(" ".join(list(e.pattern_match.group(1).upper())))
@client.on(events.NewMessage(pattern=r"\.bold (.+)"))
async def bold(e): await e.reply(f"**{e.pattern_match.group(1)}**")
@client.on(events.NewMessage(pattern=r"\.reverse (.+)"))
async def rev(e): await e.reply(e.pattern_match.group(1)[::-1])
@client.on(events.NewMessage(pattern=r"\.font (.+)"))
async def font(e): await e.reply(f"**{e.pattern_match.group(1)}** ✨ 𝓕𝓪𝓷𝓬𝔂")
@client.on(events.NewMessage(pattern=r"\.bio"))
async def bio(e): await e.reply("**👑 BIO:** 😈 VILLAIN | 🔥 Attitude King | 💀 No Mercy")
@client.on(events.NewMessage(pattern=r"\.caption"))
async def caption(e): await e.reply("**📸 CAPTION:** Villain vibes only 😈🔥 #villain #attitude")
@client.on(events.NewMessage(pattern=r"\.hashtag"))
async def hashtag(e): await e.reply("#villain #attitude #king #viral #trending #fyp #love #instagood")
@client.on(events.NewMessage(pattern=r"\.dp"))
async def dp(e): await e.reply("**🖼️ DP:** Apni wali villain wali pic laga le, ekdum killer lagegi! 🔥")
@client.on(events.NewMessage(pattern=r"\.wallpaper"))
async def wall(e): await e.reply("**🌃 WALLPAPER:** Dark villain wallpaper - black + red neon best lagega!")
@client.on(events.NewMessage(pattern=r"\.sticker"))
async def sticker(e): await e.reply("**😀 STICKER:** Photo pe reply karke .sticker likh, sticker ban jayega!")

# ===== KAAM =====
@client.on(events.NewMessage(pattern=r"\.calc (.+)"))
async def calc(e):
    try:
        r = eval(e.pattern_match.group(1))
        await e.reply(f"**🧮 CALC:** {e.pattern_match.group(1)} = **{r}**")
    except: await e.reply("**❌ Galat calculation!**")
@client.on(events.NewMessage(pattern=r"\.qr (.+)"))
async def qr(e): await e.reply(f"**📷 QR:** {e.pattern_match.group(1)} ke liye QR bana diya!")
@client.on(events.NewMessage(pattern=r"\.pass"))
async def passc(e):
    p = "".join(random.choice("abcdefgh1234567890@#") for _ in range(10))
    await e.reply(f"**🔑 PASSWORD:** `{p}`")
@client.on(events.NewMessage(pattern=r"\.note (.+)"))
async def note(e): await e.reply(f"**📝 NOTE SAVE HO GAYA:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.notes"))
async def notes(e): await e.reply("**📝 NOTES:** Teri saari notes safe hai!")
@client.on(events.NewMessage(pattern=r"\.todo (.+)"))
async def todo(e): await e.reply(f"**✅ TODO ADD:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.save (.+)"))
async def save(e): await e.reply(f"**💾 SAVE HO GAYA:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.translate (.+)"))
async def trans(e): await e.reply(f"**🌍 TRANSLATE:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.ask (.+)"))
async def ask(e): await e.reply(f"**🤖 ASK:** {e.pattern_match.group(1)} ka jawab hai - Haan, bilkul ho jayega! 🔥")
@client.on(events.NewMessage(pattern=r"\.weather (.+)"))
async def weather(e): await e.reply(f"**🌤️ WEATHER - {e.pattern_match.group(1)}:**\n**Temp:** {random.randint(22,35)}°C\n**Mausam:** Clear, thandi hawa chal rahi hai! 😎")
@client.on(events.NewMessage(pattern=r"\.weather"))
async def weather2(e): await e.reply("**🌤️ WEATHER:** City ka naam bhi likh! Jaise `.weather Indore`")
@client.on(events.NewMessage(pattern=r"\.news"))
async def news(e): await e.reply("**📰 AAJ KI KHABAR:**\n1. VILLAIN BOT V8.0 launch ho gaya! 🔥\n2. Aaj mausam badhiya hai!\n3. Tu bohot aage jayega! 😎")
@client.on(events.NewMessage(pattern=r"\.screenshot (.+)"))
async def ss(e): await e.reply(f"**📸 SCREENSHOT:** {e.pattern_match.group(1)} ka screenshot le liya!")
@client.on(events.NewMessage(pattern=r"\.timer (.+)"))
async def timer(e): await e.reply(f"**⏰ TIMER:** {e.pattern_match.group(1)} second ka timer lag gaya! ⏳")
@client.on(events.NewMessage(pattern=r"\.reminder (.+)"))
async def rem(e): await e.reply(f"**🔔 REMINDER SET:** {e.pattern_match.group(1)} - Mai yaad dila dunga!")
@client.on(events.NewMessage(pattern=r"\.play (.+)"))
async def play(e): await e.reply(f"**🎵 PLAYING:** {e.pattern_match.group(1)} 🎶\nVolume badha de! 🔊")
@client.on(events.NewMessage(pattern=r"\.lyrics (.+)"))
async def lyrics(e): await e.reply(f"**🎤 LYRICS - {e.pattern_match.group(1)}:**\nTeri yaadon me khoya hu, tu hi mera jahaan... 🎵")
@client.on(events.NewMessage(pattern=r"\.yt (.+)"))
async def yt(e): await e.reply(f"**▶️ YOUTUBE SEARCH:** {e.pattern_match.group(1)} - Top video mil gayi! 🔥")
@client.on(events.NewMessage(pattern=r"\.crypto"))
async def crypto(e): await e.reply(f"**💰 CRYPTO LIVE:**\n**Bitcoin:** ${random.randint(90000,110000)}\n**Ethereum:** ${random.randint(3000,4000)}\n**Dogecoin:** ${random.uniform(0.1,0.3):.2f}\n**Trend:** 📈 UP JA RAHA HAI!")
@client.on(events.NewMessage(pattern=r"\.pincode (.+)"))
async def pincode(e): await e.reply(f"**📍 PINCODE {e.pattern_match.group(1)}:**\n**City:** Indore, MP\n**Area:** Vijay Nagar\n**State:** Madhya Pradesh ✅")
@client.on(events.NewMessage(pattern=r"\.pincode"))
async def pincode2(e): await e.reply("**📍 Use:** `.pincode 452010`")
@client.on(events.NewMessage(pattern=r"\.ifsc (.+)"))
async def ifsc(e): await e.reply(f"**🏦 IFSC {e.pattern_match.group(1)}:**\n**Bank:** HDFC Bank\n**Branch:** Indore\n**City:** Indore, MP ✅")
@client.on(events.NewMessage(pattern=r"\.ifsc"))
async def ifsc2(e): await e.reply("**🏦 Use:** `.ifsc HDFC0001234`")
@client.on(events.NewMessage(pattern=r"\.wiki (.+)"))
async def wiki(e): await e.reply(f"**📚 WIKIPEDIA - {e.pattern_match.group(1)}:**\nYe ek bohot famous cheez hai, iske baare me poori duniya jaanti hai. Google pe search karne pe full detail mil jayegi! 🔥")
@client.on(events.NewMessage(pattern=r"\.google (.+)"))
async def google(e): await e.reply(f"**🔍 GOOGLE SEARCH:** {e.pattern_match.group(1)}\nTop result mil gaya! Link: google.com/search?q={e.pattern_match.group(1).replace(' ','+')}")
@client.on(events.NewMessage(pattern=r"\.translate2 (.+)"))
async def translate2(e): await e.reply(f"**🌍 TRANSLATE2:**\n**Hindi:** {e.pattern_match.group(1)}\n**English:** {e.pattern_match.group(1)} (Translated) ✅")
@client.on(events.NewMessage(pattern=r"\.tts (.+)"))
async def tts(e): await e.reply(f"**🔊 TTS:**\n`{e.pattern_match.group(1)}` ko awaaz me bol diya! 🔊🎙️")
@client.on(events.NewMessage(pattern=r"\.qr2"))
async def qr2(e): await e.reply("**📷 QR2:** QR wali photo pe reply karke `.qr2` likh, mai padh ke bata dunga!")
@client.on(events.NewMessage(pattern=r"\.password2"))
async def password2(e):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    p = "".join(random.choice(chars) for _ in range(16))
    await e.reply(f"**🔐 STRONG PASSWORD:**\n`{p}`\nKisi ko mat batana! 😎")
@client.on(events.NewMessage(pattern=r"\.email"))
async def email(e):
    names = ["villain","king","rockstar","badboy","hero"]
    await e.reply(f"**📧 FAKE EMAIL:**\n`{random.choice(names)}{random.randint(100,999)}@gmail.com`")
@client.on(events.NewMessage(pattern=r"\.anime (.+)"))
async def anime(e): await e.reply(f"**🎌 ANIME - {e.pattern_match.group(1)}:**\n**Rating:** {random.randint(8,10)}/10 ⭐\n**Episodes:** {random.randint(12,100)}\n**Genre:** Action / Adventure\n**Status:** Ekdum mast anime hai, dekh le! 🔥")
@client.on(events.NewMessage(pattern=r"\.imdb (.+)"))
async def imdb(e): await e.reply(f"**🎬 IMDB - {e.pattern_match.group(1)}:**\n**Rating:** {random.randint(7,9)}.5/10 ⭐\n**Year:** 2024\n**Genre:** Action / Drama\n**Story:** Ek villain ki kahani jo hero se zyada famous ho gaya! 🔥")
@client.on(events.NewMessage(pattern=r"\.songdl (.+)"))
async def songdl(e): await e.reply(f"**🎵 SONG DOWNLOAD:** {e.pattern_match.group(1)}\nDownloading... 100% ✅\nHo gaya download! 🔊")
@client.on(events.NewMessage(pattern=r"\.insta (.+)"))
async def insta(e): await e.reply(f"**📸 INSTA - @{e.pattern_match.group(1)}:**\n**Followers:** {random.randint(1000,100000)}\n**Following:** {random.randint(100,1000)}\n**Posts:** {random.randint(10,500)}\n**Bio:** VILLAIN VIBES 😈")
@client.on(events.NewMessage(pattern=r"\.ytmp3 (.+)"))
async def ytmp3(e): await e.reply(f"**🎧 YTMP3:** {e.pattern_match.group(1)}\nConverting to MP3... 100% ✅\nMP3 ready hai! 🔊")

# ===== PRO =====
@client.on(events.NewMessage(pattern=r"\.ip (.+)"))
async def ip(e): await e.reply(f"**🌐 IP - {e.pattern_match.group(1)}:**\n**IP:** 104.21.{random.randint(10,99)}.{random.randint(10,99)}\n**Location:** USA\n**Ping:** {random.randint(20,100)}ms ✅")
@client.on(events.NewMessage(pattern=r"\.whois (.+)"))
async def whois(e): await e.reply(f"**🔍 WHOIS - {e.pattern_match.group(1)}:**\n**Domain:** {e.pattern_match.group(1)}\n**Owner:** Privacy Protected\n**Created:** 2015\n**Server:** Cloudflare ✅")
@client.on(events.NewMessage(pattern=r"\.short (.+)"))
async def short(e): await e.reply(f"**🔗 SHORT LINK:**\n**Old:** {e.pattern_match.group(1)}\n**New:** bit.ly/villain{random.randint(1000,9999)} ✅")
@client.on(events.NewMessage(pattern=r"\.qrphoto"))
async def qrphoto(e): await e.reply("**📷 QRPHOTO:** Photo pe reply karke `.qrphoto` likh, uska QR bana dunga!")
@client.on(events.NewMessage(pattern=r"\.pdf (.+)"))
async def pdf(e): await e.reply(f"**📄 PDF BAN GAYA:** {e.pattern_match.group(1)}\nPDF ready hai, download kar le! ✅")
@client.on(events.NewMessage(pattern=r"\.vcard"))
async def vcard(e): await e.reply("**👤 VCARD:**\n**Name:** VILLAIN\n**Phone:** +91 98XXX XXXXX\n**Email:** villain@gmail.com\nContact card ban gaya! ✅")

# ===== AUTO =====
@client.on(events.NewMessage(pattern=r"\.afk (.+)"))
async def afk_reason(e): await e.reply(f"**😴 AFK HU!**\n**Wajah:** {e.pattern_match.group(1)}\nBaad me baat karte hai!")
@client.on(events.NewMessage(pattern=r"\.afk"))
async def afk(e): await e.reply("**😴 AFK HU, BAAD ME BAAT KARTE HAI!**")
@client.on(events.NewMessage(pattern=r"\.back"))
async def back(e): await e.reply("**😎 I'M BACK! VILLAIN AA GAYA! 🔥**")
@client.on(events.NewMessage(pattern=r"\.autoreact"))
async def ar(e): await e.reply("**❤️ AUTO REACT ON!**")
@client.on(events.NewMessage(pattern=r"\.autoreply"))
async def arp(e): await e.reply("**💬 AUTO REPLY ON!**")
@client.on(events.NewMessage(pattern=r"\.autopin"))
async def ap(e): await e.reply("**📌 AUTO PIN ON!**")
@client.on(events.NewMessage(pattern=r"\.autodelete"))
async def ad(e): await e.reply("**🗑️ AUTO DELETE ON!**")
@client.on(events.NewMessage(pattern=r"\.typing"))
async def typing(e): await e.reply("**⌨️ Typing...**")
@client.on(events.NewMessage(pattern=r"\.online"))
async def online(e): await e.reply("**🟢 ONLINE HU!**")

# ===== PRANK - HACK WALA BLOCK FOR SUDO =====
@client.on(events.NewMessage(pattern=r"\.hack$"))
async def hack(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**😂 PRANK! Mazak tha bhai!**")
@client.on(events.NewMessage(pattern=r"\.fakeid"))
async def fakeid(e):
    names = ["Rahul Sharma","Aarav Singh","Vikash Kumar","Priya Verma"]
    await e.reply(f"**🪪 FAKE ID:**\n**Name:** {random.choice(names)}\n**ID:** {random.randint(10000,99999)}")
@client.on(events.NewMessage(pattern=r"\.wasted"))
async def wasted(e): await e.reply("**💀 WASTED!**\nGame Over! 😂")
@client.on(events.NewMessage(pattern=r"\.spam (.+)"))
async def spam(e):
    parts = e.pattern_match.group(1).split(" ",1)
    try:
        count = min(int(parts[0]), 5)
        msg = parts[1] if len(parts)>1 else "VILLAIN SPAM 🔥"
        for i in range(count):
            await e.reply(msg)
            await asyncio.sleep(0.5)
    except: await e.reply("**Use:** `.spam 3 hello` (max 5)")
@client.on(events.NewMessage(pattern=r"\.raid"))
async def raid(e):
    await e.reply(f"**🔥 RAID:**\n{random.choice(RAIDS)}")

# ===== HACKER FAKE PRANK - SIRF OWNER =====
@client.on(events.NewMessage(pattern=r"\.hack2"))
async def hack2(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    m = await e.reply("**💻 HACKING...**\n`[■□□□□] 10%`")
    await asyncio.sleep(0.7)
    await m.edit("**💻 HACKING...**\n`[■■■□□] 50%`\n[✓] Target Found...\n[✓] IP Traced...")
    await asyncio.sleep(0.7)
    await m.edit("**✅ HACK SUCCESSFUL!**\n[✓] Password Bypassed\n[✓] ACCESS GRANTED! 😈\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.ddos"))
async def ddos(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    m = await e.reply("**⚠️ DDOS ATTACK STARTED...**\nTarget Server Pinging...")
    await asyncio.sleep(0.8)
    await m.edit("**💥 SERVER CRASHED!**\nPing: 9999ms\nServer: 100% DOWN!\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.trace"))
async def trace(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply(f"**📍 LOCATION FOUND!**\n**City:** Indore\n**Device:** Android\n**IP:** 192.168.1.{random.randint(10,99)}\n**Last Seen:** 2 min ago\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.passwordhack"))
async def passwordhack(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**✅ PASSWORD FOUND!**\nPassword: `****1234`\n**HACK SUCCESSFUL!**\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.virus"))
async def virus(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**🦠 PHONE HACKED!**\nSab data chala gaya! 😱\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.darkweb"))
async def darkweb(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**🌑 ENTERING DARK WEB...**\nAccess Granted to Secret Files...\nWelcome Hacker VILLAIN! 😈\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.cctv"))
async def cctv(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**📹 CCTV HACKED!**\nCamera 1: LIVE 🟢\nCamera 2: LIVE 🟢\nSab dikh raha hai! 👀\n\n😂 PRANK")
@client.on(events.NewMessage(pattern=r"\.whatsapp"))
async def whatsapp(e):
    if is_hack_blocked_for_sudo(e):
        await e.reply("**❌ Ye HACK command sirf OWNER chala sakta hai! 😈**"); return
    await e.reply("**💬 WHATSAPP HACKING...**\nMessages Loading...\nLast Chat: `Hii jaan` 😂\n\n😂 PRANK")

# ===== GROUP KING =====
@client.on(events.NewMessage(pattern=r"\.tagall"))
async def tagall(e): await e.reply("**📢 TAGALL:**\n@all sab log aa jao! VILLAIN ne bulaya hai! 🔥👑")
@client.on(events.NewMessage(pattern=r"\.purge"))
async def purge(e): await e.reply("**🧹 PURGE:** Chat saaf kar di gayi! ✅")
@client.on(events.NewMessage(pattern=r"\.kick"))
async def kick(e): await e.reply("**👢 KICK:** Banda group se bahar kar diya! (Admin hona chahiye)")
@client.on(events.NewMessage(pattern=r"\.ban"))
async def ban(e): await e.reply("**🚫 BAN:** Banda ban ho gaya! Ab wapas nahi aayega! 😈")
@client.on(events.NewMessage(pattern=r"\.unban"))
async def unban(e): await e.reply("**✅ UNBAN:** Bande ko wapas le aaya!")
@client.on(events.NewMessage(pattern=r"\.promote"))
async def promote(e): await e.reply("**⬆️ PROMOTE:** Ab tu Admin hai! 👑")
@client.on(events.NewMessage(pattern=r"\.demote"))
async def demote(e): await e.reply("**⬇️ DEMOTE:** Admin se hata diya!")
@client.on(events.NewMessage(pattern=r"\.block"))
async def block(e): await e.reply("**🚫 BLOCK:** Block kar diya!")
@client.on(events.NewMessage(pattern=r"\.unblock"))
async def unblock(e): await e.reply("**✅ UNBLOCK:** Unblock kar diya!")
@client.on(events.NewMessage(pattern=r"\.rules"))
async def rules(e): await e.reply("**📜 GROUP RULES:**\n1. Gaali mat do\n2. Spam mat karo\n3. Sabki respect karo\n4. Admin ki baat mano")
@client.on(events.NewMessage(pattern=r"\.welcome"))
async def welcome(e): await e.reply("**🎉 WELCOME! Group me swagat hai! 🥳**")
@client.on(events.NewMessage(pattern=r"\.goodmorning"))
async def gm(e): await e.reply("**🌞 GOOD MORNING! Naya din, nayi energy! 🔥**")
@client.on(events.NewMessage(pattern=r"\.goodnight"))
async def gn(e): await e.reply("**🌙 GOOD NIGHT! Sweet dreams! 😴**")
@client.on(events.NewMessage(pattern=r"\.birthday"))
async def bday(e): await e.reply("**🎂 HAPPY BIRTHDAY! 🎉🥳 Cake kahan hai?**")

# ===== VILLAIN SPECIAL =====
@client.on(events.NewMessage(pattern=r"\.sus"))
async def sus(e): await e.reply(f"**🕵️ SUS METER:** {random.randint(1,100)}% SUS! 😂\nTu to bohot shakki lag raha hai!")
@client.on(events.NewMessage(pattern=r"\.top"))
async def top(e): await e.reply("**🏆 TOP BANDA:**\n**#1** VILLAIN 👑\n**#2** Tu 😎\n**#3** Tera Best Friend 🫶")
@client.on(events.NewMessage(pattern=r"\.vs (.+)"))
async def vs(e):
    opp = e.pattern_match.group(1)
    await e.reply(f"**⚔️ 1 VS 1 FIGHT!**\n**VILLAIN** VS **{opp}**\n\n**WINNER:** VILLAIN! 😈🔥\n{opp} haar gaya! 😂")

# ===== VILLAIN SPECIAL 2.0 =====
@client.on(events.NewMessage(pattern=r"\.jail"))
async def jail(e): await e.reply("**🚔 JAIL ME DAAL DIYA!**\nBanda ab jail me hai! 🔒😂\nSaza: 24 ghante no chat!")
@client.on(events.NewMessage(pattern=r"\.free"))
async def free(e): await e.reply("**🔓 FREE HO GAYA!**\nBanda jail se bahar aa gaya! 🎉")
@client.on(events.NewMessage(pattern=r"\.kill"))
async def kill(e): await e.reply("**🔫 KILL! (GAME ME)**\nHeadshot! 💥\nBanda khatam! 😂 Game wala hai, real nahi!")
@client.on(events.NewMessage(pattern=r"\.revive"))
async def revive(e): await e.reply("**💉 REVIVE!**\nBanda wapas zinda ho gaya! 🫡")
@client.on(events.NewMessage(pattern=r"\.wanted"))
async def wanted(e): await e.reply(f"**🤠 WANTED POSTER!**\n**NAME:** VILLAIN\n**REWARD:** ₹{random.randint(10000,100000)}\n**CRIME:** Bohot zyada handsome hona! 😎🔥")
@client.on(events.NewMessage(pattern=r"\.gang"))
async def gang(e): await e.reply("**😈 VILLAIN GANG!**\n**Leader:** VILLAIN 👑\n**Members:** Tu, Tera BFF, Aur Poora Group!\n**Motto:** Darna Mana Hai! 🔥")

# ===== EXTRA =====
@client.on(events.NewMessage(pattern=r"\.tea"))
async def tea(e): await e.reply("**🍵 CHAI PI LO YAAR! Garam garam!**")
@client.on(events.NewMessage(pattern=r"\.coffee"))
async def coffee(e): await e.reply("**☕ COFFEE TIME!**")
@client.on(events.NewMessage(pattern=r"\.song"))
async def song(e): await e.reply("**🎵 SONG:** Tera favourite gaana kaunsa hai? Bata de!")
@client.on(events.NewMessage(pattern=r"\.movie"))
async def movie(e): await e.reply("**🎬 MOVIE:** Aaj raat Villain wali movie dekhte hai! 🍿")
@client.on(events.NewMessage(pattern=r"\.study"))
async def study(e): await e.reply("**📚 STUDY TIME! Phone side me rakh, padhai kar! 😤**")
@client.on(events.NewMessage(pattern=r"\.gym"))
async def gym(e): await e.reply("**💪 GYM TIME! Aaj chest day hai! 🔥**")
@client.on(events.NewMessage(pattern=r"\.sleep"))
async def sleep(e): await e.reply("**😴 SO JAA YAAR, RAAT HO GAYI!**")
@client.on(events.NewMessage(pattern=r"\.name"))
async def name(e): await e.reply("**👑 NAME:** VILLAIN 😈")
@client.on(events.NewMessage(pattern=r"\.age"))
async def age(e): await e.reply("**🎂 AGE:** 18+ VILLAIN! 😎")

print("VILLAIN USR BOT V8.0 SUDO STARTED!")
client.start()
client.run_until_disconnected()
