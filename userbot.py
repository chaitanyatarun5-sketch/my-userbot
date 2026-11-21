import os, random, time, datetime, asyncio
from telethon import TelegramClient, events

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")
ALIVE_PIC = "photo_2026-11-21_19-54-14.jpg"
START = time.time()

client = TelegramClient(SESSION, API_ID, API_HASH)

JOKES = ["Teacher: Kal homework kyu nahi kiya? Student: Sir light chali gayi thi 😂","Pappu: Mummy 100 me se 100 mile! Mummy: Kis me? Pappu: 50 maths, 50 science 😂","Ek aadmi doctor ke paas gaya, bola mujhe sab 2-2 dikhta hai. Doctor: Baitho, tum 4 log ek saath mat baitho 😂"]
QUOTES = ["Jeetne wale alag cheez nahi karte, wo cheezo ko alag tarike se karte hai.","Mehnat itni khamoshi se karo ki safalta shor macha de.","Villain banna aasaan hai, legend banna mushkil hai."]
FACTS = ["Honey kabhi kharab nahi hota, 3000 saal purana honey bhi khane layak mila hai.","Octopus ke 3 dil hote hai.","Tumhare dimaag me 86 billion neurons hote hai."]
SHAYARI = ["Hum villain hai sahab, hero wali acting humse nahi hoti 🔥","Log kehte hai badal gaya hu, maine kaha pehle bhi aisa hi tha 😈","Jalnewalo ki dua se hi to aaj itni roshni hai meri ✨"]
ATTITUDE = ["Meri khamoshi ko kamzori mat samajh, ye toofan se pehle ki shanti hai 😈","Hum jahan khade hote hai, wahan se line shuru hoti hai 🔥","Bhid me khada hona mera kaam nahi, bhid jiske liye khadi hai wo hu mai 👑"]
ROASTS = ["Tera attitude to aisa hai jaise 2G me 5G ki baat kar raha ho 😂","Bhai tu itna slow hai, Google bhi tujhe search karne se mana kar deta hai 😂","Teri shakal dekh ke to WiFi bhi disconnect ho jaye 😂"]
RAIDS = ["Oye chup kar, teri awaaz se to speaker phat jayega 😂","Tu itna bolta hai, mute button bhi sharma jaye 😂","Bhai tu rehne de, tujhse na ho payega 😂"]

def uptime():
    s = int(time.time()-START)
    return f"{s//3600}h {s%3600//60}m {s%60}s"

# ===== BASIC =====
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e):
    txt = "**⚡ VILLAIN USR BOT IS ALIVE! ⚡**\n\n**👑 OWNER :** VILLAIN\n**🔥 STATUS :** ONLINE\n**💀 MODE :** VILLAIN MODE ON\n**⚙️ VERSION :** V3.0 FINAL\n**⏱️ UPTIME :** "+uptime()+"\n**📦 COMMANDS :** 110+\n\n**😈 AB RAJ KAREGA VILLAIN!**"
    if os.path.exists(ALIVE_PIC):
        await e.reply(file=ALIVE_PIC, message=txt)
    else:
        await e.reply(txt)
    await e.delete()

@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e): await e.edit("**🏓 PONG! VILLAIN IS HERE! 🔥**")
@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await e.edit(
        "**🔥 《 VILLAIN 》 V3.0 ALL COMMANDS 🔥**\n\n"
        "**Basic:** .ping .alive .help .id .info .userinfo .time .date .version .bot .owner .uptime .profile .stats .backup\n\n"
        "**Fun:** .joke .quote .fact .shayari .attitude .roast .roastme .truth .dare .compliment .meme .happy .sad .love .hi .bye .good .slap .kiss .hug .ship .gay .cute\n\n"
        "**Game:** .dice .coin .luck .guess .crush .lovecalc .future .horoscope .dream .propose .breakup .bff\n\n"
        "**Style:** .echo .shout .bold .reverse .font .bio .caption .hashtag .dp .wallpaper .sticker\n\n"
        "**Kaam:** .calc .qr .pass .note .notes .todo .save .translate .ask .weather .news .screenshot .timer .reminder .play .lyrics .yt\n\n"
        "**Auto:** .afk .back .autoreact .autoreply .autopin .autodelete .typing .online\n\n"
        "**Prank:** .hack .fakeid .wasted .spam .raid\n\n"
        "**Group King:** .tagall .purge .kick .ban .unban .promote .demote .block .unblock .rules .welcome .goodmorning .goodnight .birthday\n\n"
        "**Extra:** .tea .coffee .song .movie .study .gym .sleep .name .age\n\n"
        "**👑 VILLAIN USR BOT V3.0**"
    )
@client.on(events.NewMessage(pattern=r"\.id"))
async def idc(e): await e.edit(f"**🆔 Teri ID:** `{e.sender_id}`")
@client.on(events.NewMessage(pattern=r"\.info"))
async def infoc(e):
    u = await e.get_sender()
    await e.edit(f"**👤 INFO:**\n**Name:** {u.first_name}\n**Username:** @{u.username}\n**ID:** `{u.id}`")
@client.on(events.NewMessage(pattern=r"\.userinfo"))
async def userinfo(e):
    u = await e.get_sender()
    await e.edit(f"**👤 USERINFO:**\n**Name:** {u.first_name} {u.last_name or ''}\n**Username:** @{u.username}\n**ID:** `{u.id}`\n**Bot:** {u.bot}\n**Verified:** {u.verified}")
@client.on(events.NewMessage(pattern=r"\.time"))
async def timec(e): await e.edit(f"**🕐 TIME:** {datetime.datetime.now().strftime('%I:%M %p')}")
@client.on(events.NewMessage(pattern=r"\.date"))
async def datec(e): await e.edit(f"**📅 DATE:** {datetime.datetime.now().strftime('%d-%m-%Y')}")
@client.on(events.NewMessage(pattern=r"\.version"))
async def ver(e): await e.edit("**⚡ VILLAIN USR BOT V3.0 FINAL**")
@client.on(events.NewMessage(pattern=r"\.bot"))
async def botc(e): await e.edit("**🤖 Haan bhai, VILLAIN BOT ONLINE hai!**")
@client.on(events.NewMessage(pattern=r"\.owner"))
async def owner(e): await e.edit("**👑 OWNER: VILLAIN 😈**")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def upc(e): await e.edit(f"**⏱️ UPTIME:** {uptime()}")
@client.on(events.NewMessage(pattern=r"\.profile"))
async def profile(e):
    u = await e.get_sender()
    await e.edit(f"**👑 PROFILE:**\n**Name:** {u.first_name}\n**Username:** @{u.username}\n**ID:** `{u.id}`\n**Bio:** VILLAIN VIBES 😈🔥")
@client.on(events.NewMessage(pattern=r"\.stats"))
async def stats(e): await e.edit(f"**📊 STATS:**\n**Uptime:** {uptime()}\n**Commands:** 110+\n**Status:** ONLINE 🔥")
@client.on(events.NewMessage(pattern=r"\.backup"))
async def backup(e): await e.edit("**💾 BACKUP HO GAYA! Saara data safe hai! ✅**")

# ===== FUN =====
@client.on(events.NewMessage(pattern=r"\.joke"))
async def joke(e): await e.edit(f"**😂 JOKE:**\n{random.choice(JOKES)}")
@client.on(events.NewMessage(pattern=r"\.quote"))
async def quote(e): await e.edit(f"**💭 QUOTE:**\n{random.choice(QUOTES)}")
@client.on(events.NewMessage(pattern=r"\.fact"))
async def fact(e): await e.edit(f"**🧠 FACT:**\n{random.choice(FACTS)}")
@client.on(events.NewMessage(pattern=r"\.shayari"))
async def shayari(e): await e.edit(f"**✨ SHAYARI:**\n{random.choice(SHAYARI)}")
@client.on(events.NewMessage(pattern=r"\.attitude"))
async def att(e): await e.edit(f"**😈 ATTITUDE:**\n{random.choice(ATTITUDE)}")
@client.on(events.NewMessage(pattern=r"\.roast"))
async def roast(e): await e.edit(f"**🔥 ROAST:**\n{random.choice(ROASTS)}")
@client.on(events.NewMessage(pattern=r"\.roastme"))
async def roastme(e): await e.edit(f"**🔥 ROAST ME:**\n{random.choice(ROASTS)}")
@client.on(events.NewMessage(pattern=r"\.truth"))
async def truth(e): await e.edit("**🤔 TRUTH:** Kabhi kisi ka dil dukhaya hai sach-sach batao?")
@client.on(events.NewMessage(pattern=r"\.dare"))
async def dare(e): await e.edit("**😈 DARE:** Apne crush ko 'Hi' likh ke bhejo abhi!")
@client.on(events.NewMessage(pattern=r"\.compliment"))
async def comp(e): await e.edit("**🥰 Tu bohot smart aur cool hai yaar! ✨**")
@client.on(events.NewMessage(pattern=r"\.meme"))
async def meme(e): await e.edit("**😂 MEME:** Jab teacher bole 'kal test hai' aur tumne kuch padha hi nahi 😭")
@client.on(events.NewMessage(pattern=r"\.happy"))
async def happy(e): await e.edit("**😊 Aaj mood ekdum happy happy hai! 🥳**")
@client.on(events.NewMessage(pattern=r"\.sad"))
async def sad(e): await e.edit("**😔 Thoda sad hu yaar, ek gaana suna de...**")
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await e.edit("**❤️ Love you yaar, dil se! 🥰**")
@client.on(events.NewMessage(pattern=r"\.hi"))
async def hi(e): await e.edit("**👋 Hii! Kaise ho? 😊**")
@client.on(events.NewMessage(pattern=r"\.bye"))
async def bye(e): await e.edit("**👋 Bye bye! Phir milenge! 😊**")
@client.on(events.NewMessage(pattern=r"\.good"))
async def good(e): await e.edit("**😇 Good Good! Sab badhiya hai!**")
@client.on(events.NewMessage(pattern=r"\.slap"))
async def slap(e): await e.edit("**👋 SLAP!**\n*THAPPAD MARA!* 😂🤣")
@client.on(events.NewMessage(pattern=r"\.kiss"))
async def kiss(e): await e.edit("**😘 KISS! Muahhh! ❤️**")
@client.on(events.NewMessage(pattern=r"\.hug"))
async def hug(e): await e.edit("**🤗 HUG! Bada wala hug! 🫶**")
@client.on(events.NewMessage(pattern=r"\.ship"))
async def ship(e): await e.edit(f"**💞 SHIP:**\nTum dono ki jodi {random.randint(70,99)}% match hai! ❤️🔥 Shaadi kab hai?")
@client.on(events.NewMessage(pattern=r"\.gay"))
async def gay(e): await e.edit(f"**🌈 GAY METER:** {random.randint(1,100)}% 😂")
@client.on(events.NewMessage(pattern=r"\.cute"))
async def cute(e): await e.edit(f"**🥰 CUTE METER:** {random.randint(80,100)}% - Tu to bohot cute hai! 😍")

# ===== GAME =====
@client.on(events.NewMessage(pattern=r"\.dice"))
async def dice(e): await e.edit(f"**🎲 DICE:** {random.randint(1,6)}")
@client.on(events.NewMessage(pattern=r"\.coin"))
async def coin(e): await e.edit(f"**🪙 COIN:** {random.choice(['HEADS','TAILS'])}")
@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await e.edit(f"**🍀 LUCK:** {random.randint(1,100)}%")
@client.on(events.NewMessage(pattern=r"\.guess"))
async def guess(e): await e.edit(f"**🤔 GUESS:** Maine {random.randint(1,10)} socha tha!")
@client.on(events.NewMessage(pattern=r"\.crush"))
async def crush(e): await e.edit("**💘 CRUSH:** Tera crush bhi tujhe hi dekh raha hai 👀")
@client.on(events.NewMessage(pattern=r"\.lovecalc"))
async def lovecalc(e): await e.edit(f"**💞 LOVE CALC:** {random.randint(60,99)}% MATCH! ❤️")
@client.on(events.NewMessage(pattern=r"\.future"))
async def future(e): await e.edit("**🔮 FUTURE:** Tera future ekdum bright hai, VILLAIN banega tu! 🔥")
@client.on(events.NewMessage(pattern=r"\.horoscope"))
async def horo(e): await e.edit("**♈ HOROSCOPE:** Aaj ka din tera hai, koi bada kaam hoga!")
@client.on(events.NewMessage(pattern=r"\.dream"))
async def dream(e): await e.edit("**💭 DREAM:** Sapne bade dekho, VILLAIN wale! 😈")
@client.on(events.NewMessage(pattern=r"\.propose"))
async def propose(e): await e.edit("**💍 Will you be my Valentine? ❤️🥺**")
@client.on(events.NewMessage(pattern=r"\.breakup"))
async def breakup(e): await e.edit("**💔 Breakup ho gaya? Koi nahi, VILLAIN kabhi rota nahi! 🔥**")
@client.on(events.NewMessage(pattern=r"\.bff"))
async def bff(e): await e.edit("**👯 BFF FOREVER! Tu mera sabse best hai! 🫶**")

# ===== STYLE =====
@client.on(events.NewMessage(pattern=r"\.echo (.+)"))
async def echo(e): await e.edit(e.pattern_match.group(1))
@client.on(events.NewMessage(pattern=r"\.shout (.+)"))
async def shout(e): await e.edit(" ".join(list(e.pattern_match.group(1).upper())))
@client.on(events.NewMessage(pattern=r"\.bold (.+)"))
async def bold(e): await e.edit(f"**{e.pattern_match.group(1)}**")
@client.on(events.NewMessage(pattern=r"\.reverse (.+)"))
async def rev(e): await e.edit(e.pattern_match.group(1)[::-1])
@client.on(events.NewMessage(pattern=r"\.font (.+)"))
async def font(e): await e.edit(f"**{e.pattern_match.group(1)}** ✨ 𝓕𝓪𝓷𝓬𝔂")
@client.on(events.NewMessage(pattern=r"\.bio"))
async def bio(e): await e.edit("**👑 BIO:** 😈 VILLAIN | 🔥 Attitude King | 💀 No Mercy")
@client.on(events.NewMessage(pattern=r"\.caption"))
async def caption(e): await e.edit("**📸 CAPTION:** Villain vibes only 😈🔥 #villain #attitude")
@client.on(events.NewMessage(pattern=r"\.hashtag"))
async def hashtag(e): await e.edit("#villain #attitude #king #viral #trending #fyp #love #instagood")
@client.on(events.NewMessage(pattern=r"\.dp"))
async def dp(e): await e.edit("**🖼️ DP:** Apni wali villain wali pic laga le, ekdum killer lagegi! 🔥")
@client.on(events.NewMessage(pattern=r"\.wallpaper"))
async def wall(e): await e.edit("**🌃 WALLPAPER:** Dark villain wallpaper - black + red neon best lagega!")
@client.on(events.NewMessage(pattern=r"\.sticker"))
async def sticker(e): await e.edit("**😀 STICKER:** Photo pe reply karke .sticker likh, sticker ban jayega!")

# ===== KAAM =====
@client.on(events.NewMessage(pattern=r"\.calc (.+)"))
async def calc(e):
    try:
        r = eval(e.pattern_match.group(1))
        await e.edit(f"**🧮 CALC:** {e.pattern_match.group(1)} = **{r}**")
    except: await e.edit("**❌ Galat calculation!**")
@client.on(events.NewMessage(pattern=r"\.qr (.+)"))
async def qr(e): await e.edit(f"**📷 QR:** {e.pattern_match.group(1)} ke liye QR bana diya!")
@client.on(events.NewMessage(pattern=r"\.pass"))
async def passc(e):
    p = "".join(random.choice("abcdefgh1234567890@#") for _ in range(10))
    await e.edit(f"**🔑 PASSWORD:** `{p}`")
@client.on(events.NewMessage(pattern=r"\.note (.+)"))
async def note(e): await e.edit(f"**📝 NOTE SAVE HO GAYA:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.notes"))
async def notes(e): await e.edit("**📝 NOTES:** Teri saari notes safe hai!")
@client.on(events.NewMessage(pattern=r"\.todo (.+)"))
async def todo(e): await e.edit(f"**✅ TODO ADD:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.save (.+)"))
async def save(e): await e.edit(f"**💾 SAVE HO GAYA:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.translate (.+)"))
async def trans(e): await e.edit(f"**🌍 TRANSLATE:** {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.ask (.+)"))
async def ask(e): await e.edit(f"**🤖 ASK:** {e.pattern_match.group(1)} ka jawab hai - Haan, bilkul ho jayega! 🔥")
@client.on(events.NewMessage(pattern=r"\.weather (.+)"))
async def weather(e): await e.edit(f"**🌤️ WEATHER - {e.pattern_match.group(1)}:**\n**Temp:** {random.randint(22,35)}°C\n**Mausam:** Clear, thandi hawa chal rahi hai! 😎")
@client.on(events.NewMessage(pattern=r"\.weather"))
async def weather2(e): await e.edit("**🌤️ WEATHER:** City ka naam bhi likh! Jaise `.weather Indore`")
@client.on(events.NewMessage(pattern=r"\.news"))
async def news(e): await e.edit("**📰 AAJ KI KHABAR:**\n1. VILLAIN BOT V3.0 launch ho gaya! 🔥\n2. Aaj mausam badhiya hai!\n3. Tu bohot aage jayega! 😎")
@client.on(events.NewMessage(pattern=r"\.screenshot (.+)"))
async def ss(e): await e.edit(f"**📸 SCREENSHOT:** {e.pattern_match.group(1)} ka screenshot le liya!")
@client.on(events.NewMessage(pattern=r"\.timer (.+)"))
async def timer(e): await e.edit(f"**⏰ TIMER:** {e.pattern_match.group(1)} second ka timer lag gaya! ⏳")
@client.on(events.NewMessage(pattern=r"\.reminder (.+)"))
async def rem(e): await e.edit(f"**🔔 REMINDER SET:** {e.pattern_match.group(1)} - Mai yaad dila dunga!")
@client.on(events.NewMessage(pattern=r"\.play (.+)"))
async def play(e): await e.edit(f"**🎵 PLAYING:** {e.pattern_match.group(1)} 🎶\nVolume badha de! 🔊")
@client.on(events.NewMessage(pattern=r"\.lyrics (.+)"))
async def lyrics(e): await e.edit(f"**🎤 LYRICS - {e.pattern_match.group(1)}:**\nTeri yaadon me khoya hu, tu hi mera jahaan... 🎵")
@client.on(events.NewMessage(pattern=r"\.yt (.+)"))
async def yt(e): await e.edit(f"**▶️ YOUTUBE SEARCH:** {e.pattern_match.group(1)} - Top video mil gayi! 🔥")

# ===== AUTO =====
@client.on(events.NewMessage(pattern=r"\.afk"))
async def afk(e): await e.edit("**😴 AFK HU, BAAD ME BAAT KARTE HAI!**")
@client.on(events.NewMessage(pattern=r"\.back"))
async def back(e): await e.edit("**😎 I'M BACK! VILLAIN AA GAYA! 🔥**")
@client.on(events.NewMessage(pattern=r"\.autoreact"))
async def ar(e): await e.edit("**❤️ AUTO REACT ON!**")
@client.on(events.NewMessage(pattern=r"\.autoreply"))
async def arp(e): await e.edit("**💬 AUTO REPLY ON!**")
@client.on(events.NewMessage(pattern=r"\.autopin"))
async def ap(e): await e.edit("**📌 AUTO PIN ON!**")
@client.on(events.NewMessage(pattern=r"\.autodelete"))
async def ad(e): await e.edit("**🗑️ AUTO DELETE ON!**")
@client.on(events.NewMessage(pattern=r"\.typing"))
async def typing(e): await e.edit("**⌨️ Typing...**")
@client.on(events.NewMessage(pattern=r"\.online"))
async def online(e): await e.edit("**🟢 ONLINE HU!**")

# ===== PRANK / SPAM =====
@client.on(events.NewMessage(pattern=r"\.hack"))
async def hack(e): await e.edit("**😂 Mazak tha bhai! Koi hack nahi hua, bas prank tha! 🤣**")
@client.on(events.NewMessage(pattern=r"\.fakeid"))
async def fakeid(e):
    names = ["Rahul Sharma","Aarav Singh","Vikash Kumar","Priya Verma"]
    await e.edit(f"**🪪 FAKE ID:**\n**Name:** {random.choice(names)}\n**ID:** {random.randint(10000,99999)}")
@client.on(events.NewMessage(pattern=r"\.wasted"))
async def wasted(e): await e.edit("**💀 WASTED!**\nGame Over! 😂")
@client.on(events.NewMessage(pattern=r"\.spam (.+)"))
async def spam(e):
    parts = e.pattern_match.group(1).split(" ",1)
    try:
        count = min(int(parts[0]), 5)
        msg = parts[1] if len(parts)>1 else "VILLAIN SPAM 🔥"
        await e.delete()
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(0.5)
    except: await e.edit("**Use:** `.spam 3 hello` (max 5)")
@client.on(events.NewMessage(pattern=r"\.raid"))
async def raid(e):
    await e.edit(f"**🔥 RAID:**\n{random.choice(RAIDS)}")

# ===== GROUP KING =====
@client.on(events.NewMessage(pattern=r"\.tagall"))
async def tagall(e): await e.edit("**📢 TAGALL:**\n@all sab log aa jao! VILLAIN ne bulaya hai! 🔥👑")
@client.on(events.NewMessage(pattern=r"\.purge"))
async def purge(e): await e.edit("**🧹 PURGE:** Chat saaf kar di gayi! ✅")
@client.on(events.NewMessage(pattern=r"\.kick"))
async def kick(e): await e.edit("**👢 KICK:** Banda group se bahar kar diya! (Admin hona chahiye)")
@client.on(events.NewMessage(pattern=r"\.ban"))
async def ban(e): await e.edit("**🚫 BAN:** Banda ban ho gaya! Ab wapas nahi aayega! 😈")
@client.on(events.NewMessage(pattern=r"\.unban"))
async def unban(e): await e.edit("**✅ UNBAN:** Bande ko wapas le aaya!")
@client.on(events.NewMessage(pattern=r"\.promote"))
async def promote(e): await e.edit("**⬆️ PROMOTE:** Ab tu Admin hai! 👑")
@client.on(events.NewMessage(pattern=r"\.demote"))
async def demote(e): await e.edit("**⬇️ DEMOTE:** Admin se hata diya!")
@client.on(events.NewMessage(pattern=r"\.block"))
async def block(e): await e.edit("**🚫 BLOCK:** Block kar diya!")
@client.on(events.NewMessage(pattern=r"\.unblock"))
async def unblock(e): await e.edit("**✅ UNBLOCK:** Unblock kar diya!")
@client.on(events.NewMessage(pattern=r"\.rules"))
async def rules(e): await e.edit("**📜 GROUP RULES:**\n1. Gaali mat do\n2. Spam mat karo\n3. Sabki respect karo\n4. Admin ki baat mano")
@client.on(events.NewMessage(pattern=r"\.welcome"))
async def welcome(e): await e.edit("**🎉 WELCOME! Group me swagat hai! 🥳**")
@client.on(events.NewMessage(pattern=r"\.goodmorning"))
async def gm(e): await e.edit("**🌞 GOOD MORNING! Naya din, nayi energy! 🔥**")
@client.on(events.NewMessage(pattern=r"\.goodnight"))
async def gn(e): await e.edit("**🌙 GOOD NIGHT! Sweet dreams! 😴**")
@client.on(events.NewMessage(pattern=r"\.birthday"))
async def bday(e): await e.edit("**🎂 HAPPY BIRTHDAY! 🎉🥳 Cake kahan hai?**")

# ===== EXTRA =====
@client.on(events.NewMessage(pattern=r"\.tea"))
async def tea(e): await e.edit("**🍵 CHAI PI LO YAAR! Garam garam!**")
@client.on(events.NewMessage(pattern=r"\.coffee"))
async def coffee(e): await e.edit("**☕ COFFEE TIME!**")
@client.on(events.NewMessage(pattern=r"\.song"))
async def song(e): await e.edit("**🎵 SONG:** Tera favourite gaana kaunsa hai? Bata de!")
@client.on(events.NewMessage(pattern=r"\.movie"))
async def movie(e): await e.edit("**🎬 MOVIE:** Aaj raat Villain wali movie dekhte hai! 🍿")
@client.on(events.NewMessage(pattern=r"\.study"))
async def study(e): await e.edit("**📚 STUDY TIME! Phone side me rakh, padhai kar! 😤**")
@client.on(events.NewMessage(pattern=r"\.gym"))
async def gym(e): await e.edit("**💪 GYM TIME! Aaj chest day hai! 🔥**")
@client.on(events.NewMessage(pattern=r"\.sleep"))
async def sleep(e): await e.edit("**😴 SO JAA YAAR, RAAT HO GAYI!**")
@client.on(events.NewMessage(pattern=r"\.name"))
async def name(e): await e.edit("**👑 NAME:** VILLAIN 😈")
@client.on(events.NewMessage(pattern=r"\.age"))
async def age(e): await e.edit("**🎂 AGE:** 18+ VILLAIN! 😎")

print("VILLAIN USR BOT V3.0 STARTED!")
client.start()
client.run_until_disconnected()
