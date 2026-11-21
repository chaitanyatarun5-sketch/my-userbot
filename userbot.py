import os, time, random, datetime, string, asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID", "37781427"))
API_HASH = os.environ.get("API_HASH", "TERA_API_HASH")
SESSION = os.environ.get("SESSION", "TERA_SESSION")
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# ===== SETTINGS =====
AFK = {"on": False, "msg": "Bhai busy hu, thodi der me reply karta hu 😴"}
AUTOREACT = {"on": False}
AUTOPIN = {"on": False}
AUTODELETE = {"on": False}
NOTES = {}
START_TIME = time.time()

JOKES = ["Teacher: Homework kyu nahi kiya? Student: Light chali gayi thi, dimag ka bulb jala hi nahi 😂","Ek aadmi ne Google se pucha - Meri biwi kaha hai? Google bola - Tere ghar pe hai 😂","Padhai me man nahi lagta? Phone 2 din band kar do, fir dekho man kaise lagta hai... phone me 😂"]
QUOTES = ["Mehnat itni khamoshi se karo ki safalta shor macha de.","Sapne wo nahi jo sote waqt aate hai, sapne wo hai jo sone nahi dete.","Kal se karunga bolna band kar, aaj se kar."]
FACTS = ["Honey kabhi kharab nahi hota, 3000 saal purana honey bhi khane layak mila hai.","Tumhare dimag me 86 billion neurons hai.","Octopus ke 3 dil hote hai."]
SHAYARI = ["Teri yaad me humne chai bhi thandi pi li, tu aaye na aaye humne to aadat bana li ☕","Mohabbat me jeetne wale ko sikandar kehte hai, aur haarne wale ko shayar ❤️","Zindagi me 2 hi log khush hai, ek jo sota hai, ek jo sone nahi deta 😂"]
ATTITUDE = ["Hum badle nahi, bas samajh gaye duniya ko 🔥","Sher akela hi kaafi hai, bheed to bakriyo ki hoti hai 🦁","Apni aukat me rehna sikh lo, hum to waise bhi sabse upar hai 😎"]
ROASTS = ["Tera face dekh ke to filter bhi haar maan jaye 😂","Tu itna slow hai, Google bhi tujhe search karne me thak jaye 😂","Teri smartness dekh ke to calculator bhi confuse ho jaye 😂"]
TRUTH = ["Sabse bada jhooth kya bola hai aaj tak?","Kispe crush hai abhi? Naam bata!","Last baar kab roya tha aur kyu?"]
DARE = ["Apne crush ko 'Hi' bhej ke screenshot bhej!","Apni DP 1 ghante ke liye cartoon wali laga!","Mummy ko bol - 'Mujhe shaadi karni hai' aur reaction bhej 😂"]
COMPLIMENTS = ["Bhai tu to dil ka achha hai yaar ❤️","Teri smile pe to duniya fida hai 😊","Tu jaha jata hai waha mahol ban jata hai 🔥"]
FUTURE = ["Tera future bright hai, bas phone thoda kam chala 😂","Aane wale 1 mahine me tujhe achhi khabar milegi!","Tu ek din bahut bada aadmi banega, bas mehnat karte reh."]
HOROSCOPE = ["Aaj ka din mast hai, koi purana dost milega.","Aaj paise kharch mat karna, bach ke rehna.","Aaj kismat tere saath hai, jo kaam atka tha wo ho jayega."]
CAPTIONS = ["Smile kar, duniya waise bhi jal rahi hai 😎","No caption needed, vibe hi kaafi hai 🔥","Zindagi ek safar hai, maza lo ❤️"]
HASHTAGS = ["#vibes #instagood #trending #viral #reels","#attitude #king #swag #desi #indore","#love #life #happy #smile #photography"]

# ===== MOOD WISE REACT LOGIC =====
MOOD_REACTS = {
    "love": ["❤️", "😍", "🥰"],
    "happy": ["😂", "🤣", "😁", "🔥"],
    "sad": ["😢", "😔", "🥺"],
    "angry": ["😡", "🤬"],
    "wow": ["😮", "😲", "🤯"],
    "ok": ["👍", "👌", "🙏"],
}
ALL_REACTS = ["❤️", "🔥", "😂", "😮", "😢", "😡", "👍", "🥰", "😍", "🤯", "👏", "🙏"]
def mood_emoji(text):
    text = text.lower()
    if any(w in text for w in ["love", "pyar", "jaan", "baby", "miss", "❤️", "bhai"]):
        return random.choice(MOOD_REACTS["love"])
    if any(w in text for w in ["haha", "lol", "hasi", "funny", "mazak", "😂", "maza"]):
        return random.choice(MOOD_REACTS["happy"])
    if any(w in text for w in ["sad", "dukhi", "ro", "alone", "😢", "tension", "bore"]):
        return random.choice(MOOD_REACTS["sad"])
    if any(w in text for w in ["gussa", "bakwas", "chup", "pagal", "😡", "hatt"]):
        return random.choice(MOOD_REACTS["angry"])
    if any(w in text for w in ["wow", "kya", "sach", "really", "amazing", "mast", "op"]):
        return random.choice(MOOD_REACTS["wow"])
    if any(w in text for w in ["ok", "thik", "haan", "done", "acha", "hmm"]):
        return random.choice(MOOD_REACTS["ok"])
    return random.choice(ALL_REACTS)

# ===== BASIC =====
@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e):
    s=time.time(); m=await e.reply("Pinging..."); await m.edit(f"Pong! `{round((time.time()-s)*1000)}ms`")
@client.on(events.NewMessage(pattern=r"\.alive"))
async def alive(e): await e.reply("✅ **Userbot Alive Hai!**\n24x7 Online | 60+ Commands 🔥")
@client.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(e):
    await e.reply("""**🔥 ALL COMMANDS:**
**Basic:** `.ping` `.alive` `.help` `.id` `.info` `.time` `.date` `.version` `.bot` `.owner` `.uptime`
**Fun:** `.joke` `.quote` `.fact` `.shayari` `.attitude` `.roast` `.truth` `.dare` `.compliment` `.roastme` `.meme` `.happy` `.sad` `.love` `.hi` `.bye` `.good`
**Game:** `.dice` `.coin` `.luck` `.rps` `.guess` `.crush` `.lovecalc` `.future` `.horoscope` `.dream` `.propose` `.breakup` `.bff`
**Style:** `.echo` `.shout` `.bold` `.reverse` `.font` `.bio` `.caption` `.hashtag` `.dp` `.wallpaper`
**Kaam:** `.calc` `.qr` `.pass` `.note` `.notes` `.todo` `.save` `.translate` `.ask`
**Auto:** `.afk` `.back` `.autoreact` `.autoreply` `.autopin` `.autodelete` `.typing` `.online`
**Prank:** `.hack` `.fakeid` `.wasted`
**Group:** `.rules` `.welcome` `.goodmorning` `.goodnight` `.birthday`
**Extra:** `.tea` `.coffee` `.song` `.movie` `.study` `.gym` `.sleep` `.name` `.age`
""")
@client.on(events.NewMessage(pattern=r"\.id"))
async def id_cmd(e): await e.reply(f"Teri ID: `{e.sender_id}`\nChat ID: `{e.chat_id}`")
@client.on(events.NewMessage(pattern=r"\.info"))
async def info_cmd(e):
    u=await e.get_sender(); await e.reply(f"**Name:** {u.first_name}\n**Username:** @{u.username}\n**ID:** `{u.id}`")
@client.on(events.NewMessage(pattern=r"\.time"))
async def time_cmd(e): await e.reply(f"Time: {datetime.datetime.now().strftime('%I:%M %p')}")
@client.on(events.NewMessage(pattern=r"\.date"))
async def date_cmd(e): await e.reply(f"Date: {datetime.datetime.now().strftime('%d %B %Y')}")
@client.on(events.NewMessage(pattern=r"\.version"))
async def ver(e): await e.reply("Version: v4.0 | Mood React + Auto Pin All | 60+ Commands")
@client.on(events.NewMessage(pattern=r"\.bot"))
async def bot_cmd(e): await e.reply("Mai Telethon + Render pe chalne wala Pro Userbot hu!")
@client.on(events.NewMessage(pattern=r"\.owner"))
async def owner_cmd(e): await e.reply("Is bot ka malik mera bhai hai, Indore se! 🔥")
@client.on(events.NewMessage(pattern=r"\.uptime"))
async def uptime_cmd(e):
    sec=int(time.time()-START_TIME); await e.reply(f"Online hu pichle {sec//60} min se 🔥")
@client.on(events.NewMessage(pattern=r"\.name"))
async def name_cmd(e): await e.reply("Mera naam hai - Tera Userbot 😎")
@client.on(events.NewMessage(pattern=r"\.age"))
async def age_cmd(e): await e.reply("Mai abhi abhi paida hua hu, Render pe rehta hu 😂")

# ===== FUN =====
@client.on(events.NewMessage(pattern=r"\.joke"))
async def joke(e): await e.reply(random.choice(JOKES))
@client.on(events.NewMessage(pattern=r"\.quote"))
async def quote(e): await e.reply(random.choice(QUOTES))
@client.on(events.NewMessage(pattern=r"\.fact"))
async def fact(e): await e.reply("🧠 **Fact:** "+random.choice(FACTS))
@client.on(events.NewMessage(pattern=r"\.shayari"))
async def shayari(e): await e.reply(random.choice(SHAYARI))
@client.on(events.NewMessage(pattern=r"\.attitude"))
async def att(e): await e.reply(random.choice(ATTITUDE))
@client.on(events.NewMessage(pattern=r"\.roast"))
async def roast(e): await e.reply(random.choice(ROASTS))
@client.on(events.NewMessage(pattern=r"\.roastme"))
async def roastme(e): await e.reply("Tujhe roast karu? Tu khud hi ek roast hai bhai 😂🔥")
@client.on(events.NewMessage(pattern=r"\.truth"))
async def truth(e): await e.reply("🤔 **Truth:** "+random.choice(TRUTH))
@client.on(events.NewMessage(pattern=r"\.dare"))
async def dare(e): await e.reply("😈 **Dare:** "+random.choice(DARE))
@client.on(events.NewMessage(pattern=r"\.compliment"))
async def comp(e): await e.reply(random.choice(COMPLIMENTS))
@client.on(events.NewMessage(pattern=r"\.meme"))
async def meme(e): await e.reply(random.choice(["Jab mummy bole - Beta phone rakh de, aur tu bole - Bas 5 min 😂","Exam me - Sab aata hai, bas likhna nahi aata 😂","Paise khatam, par shauq khatam nahi 😂"]))
@client.on(events.NewMessage(pattern=r"\.(hi|hello)"))
async def hi(e): await e.reply("Hii bhai! Kaise ho? 😊")
@client.on(events.NewMessage(pattern=r"\.bye"))
async def bye(e): await e.reply("Bye bye, fir milte hai! 👋")
@client.on(events.NewMessage(pattern=r"\.good"))
async def good(e): await e.reply("Good good, sab badhiya hai! 🔥")
@client.on(events.NewMessage(pattern=r"\.love"))
async def love(e): await e.reply("Love to sab karte hai, pehle padhai kar le bhai ❤️😂")
@client.on(events.NewMessage(pattern=r"\.sad"))
async def sad(e): await e.reply("Sad mat ho yaar, ek chai pee le, sab theek ho jayega ☕")
@client.on(events.NewMessage(pattern=r"\.happy"))
async def happy(e): await e.reply("Happy rehna hi sabse badi jeet hai! 😁")
@client.on(events.NewMessage(pattern=r"\.tea"))
async def tea(e): await e.reply("Chai pee lo bhai ☕, thakan gayab!")
@client.on(events.NewMessage(pattern=r"\.coffee"))
async def coffee(e): await e.reply("Coffee aa gayi ☕, ab neend bhagao!")
@client.on(events.NewMessage(pattern=r"\.sleep"))
async def sleep(e): await e.reply("So ja bhai, raat ho gayi hai 😴")
@client.on(events.NewMessage(pattern=r"\.song"))
async def song(e): await e.reply(random.choice(["Arijit Singh - Tum Se Hi","AP Dhillon - With You","Karan Aujla - Softly","Shubh - Cheques"]))
@client.on(events.NewMessage(pattern=r"\.movie"))
async def movie(e): await e.reply(random.choice(["3 Idiots","Jawan","Animal","Pathaan","Gully Boy"]))
@client.on(events.NewMessage(pattern=r"\.study"))
async def study(e): await e.reply("Study Tip: 25 min padh, 5 min break. Phone side me rakh!")
@client.on(events.NewMessage(pattern=r"\.gym"))
async def gym(e): await e.reply("Gym Tip: Roz 30 min workout, paani zyada pee, junk kam kha 💪")

# ===== GAME / LOVE =====
@client.on(events.NewMessage(pattern=r"\.dice"))
async def dice(e): await e.reply(f"🎲 Dice: **{random.randint(1,6)}**")
@client.on(events.NewMessage(pattern=r"\.coin"))
async def coin(e): await e.reply(f"🪙 Aaya: **{random.choice(['Heads','Tails'])}**")
@client.on(events.NewMessage(pattern=r"\.luck"))
async def luck(e): await e.reply(f"Tera lucky number: **{random.randint(1,100)}**")
@client.on(events.NewMessage(pattern=r"\.rps (.+)"))
async def rps(e):
    u=e.pattern_match.group(1).lower(); b=random.choice(["rock","paper","scissor"]); await e.reply(f"Tu: {u}\nMai: {b}\nMaza aa gaya!")
@client.on(events.NewMessage(pattern=r"\.guess (.+)"))
async def guess(e):
    n=int(e.pattern_match.group(1)); b=random.randint(1,10); await e.reply(f"Tu bola {n}, sahi tha {b} - {'Jeet gaya! 🎉' if n==b else 'Haar gaya 😂'}")
@client.on(events.NewMessage(pattern=r"\.crush (.+)"))
async def crush(e): await e.reply(f"❤️ {e.pattern_match.group(1)} ke saath tera match: **{random.randint(50,99)}%**")
@client.on(events.NewMessage(pattern=r"\.lovecalc (.+)"))
async def lovecalc(e): await e.reply(f"💕 Love Calculator: **{random.randint(60,99)}%** Match hai!")
@client.on(events.NewMessage(pattern=r"\.future"))
async def future(e): await e.reply(random.choice(FUTURE))
@client.on(events.NewMessage(pattern=r"\.horoscope"))
async def horo(e): await e.reply(random.choice(HOROSCOPE))
@client.on(events.NewMessage(pattern=r"\.dream (.+)"))
async def dream(e): await e.reply(f"Tune sapne me {e.pattern_match.group(1)} dekha? Iska matlab achhi khabar aane wali hai! 😊")
@client.on(events.NewMessage(pattern=r"\.propose"))
async def propose(e): await e.reply("Mujhe tumse kuch kehna hai... Will you be my chai partner for life? ☕❤️")
@client.on(events.NewMessage(pattern=r"\.breakup"))
async def breakup(e): await e.reply("Breakup ho gaya? Koi nahi, chai pee le, nayi wali mil jayegi 😂☕")
@client.on(events.NewMessage(pattern=r"\.bff"))
async def bff(e): await e.reply("Dosti me doori to aati rehti hai, fir bhi sachhi dosti kabhi kam nahi hoti ❤️")

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
async def font(e):
    txt=e.pattern_match.group(1); await e.reply(f"𝓕𝓪𝓷𝓬𝔂: {txt} ✨\n𝕭𝖔𝖑𝖉: {txt} 🔥\n🅂🅃🅈🄻🄸🅂🄷: {txt}")
@client.on(events.NewMessage(pattern=r"\.bio"))
async def bio(e): await e.reply(random.choice(["😎 Attitude mera, duniya meri fan","☕ Chai lover | 😴 Neend lover","🔥 Born to be different"]))
@client.on(events.NewMessage(pattern=r"\.caption"))
async def caption(e): await e.reply(random.choice(CAPTIONS))
@client.on(events.NewMessage(pattern=r"\.hashtag"))
async def hashtag(e): await e.reply(random.choice(HASHTAGS))
@client.on(events.NewMessage(pattern=r"\.dp"))
async def dp(e): await e.reply("DP ke liye best hai - Black background + Attitude pose 😎")
@client.on(events.NewMessage(pattern=r"\.wallpaper"))
async def wall(e): await e.reply("Wallpaper idea: Mountain + Sunset + Tera naam 🔥")

# ===== KAAM =====
@client.on(events.NewMessage(pattern=r"\.calc (.+)"))
async def calc(e):
    try: await e.reply(f"= **{eval(e.pattern_match.group(1))}**")
    except: await e.reply("Galat calculation hai bhai!")
@client.on(events.NewMessage(pattern=r"\.qr (.+)"))
async def qr(e): await e.reply(f"QR bana diya is text ka: {e.pattern_match.group(1)} - Google me 'QR generator' me daal ke bana le!")
@client.on(events.NewMessage(pattern=r"\.pass"))
async def passwd(e):
    p=''.join(random.choice(string.ascii_letters+string.digits+"@#$") for _ in range(10)); await e.reply(f"Tera strong password: `{p}`")
@client.on(events.NewMessage(pattern=r"\.note (.+)"))
async def note(e):
    t=e.pattern_match.group(1); NOTES[str(e.chat_id)]=t; await e.reply(f"Note save ho gaya: {t}")
@client.on(events.NewMessage(pattern=r"\.notes"))
async def notes(e): await e.reply(f"Tera note: {NOTES.get(str(e.chat_id),'Koi note nahi hai')}")
@client.on(events.NewMessage(pattern=r"\.todo (.+)"))
async def todo(e): await e.reply(f"✅ Todo add: {e.pattern_match.group(1)} - Yaad rahega!")
@client.on(events.NewMessage(pattern=r"\.save"))
async def save(e):
    if e.is_reply:
        m=await e.get_reply_message(); await m.forward_to(e.sender_id); await e.reply("Save ho gaya Saved Messages me!")
    else: await e.reply("Kisi msg pe reply karke `.save` likh!")
@client.on(events.NewMessage(pattern=r"\.translate (.+)"))
async def trans(e): await e.reply(f"English me: {e.pattern_match.group(1)}")
@client.on(events.NewMessage(pattern=r"\.ask (.+)"))
async def ask(e): await e.reply(f"Sawal: {e.pattern_match.group(1)}\nJawab: Bhai ye to mast sawal hai, iska jawab hai - Haan, ho jayega! 😎")

# ===== AUTO TOGGLES =====
@client.on(events.NewMessage(pattern=r"\.afk ?(.*)"))
async def afk(e):
    AFK["on"]=True; AFK["msg"]=e.pattern_match.group(1) or AFK["msg"]; await e.reply(f"AFK On! Ab koi msg karega to ye jayega: {AFK['msg']}")
@client.on(events.NewMessage(pattern=r"\.back"))
async def back(e): AFK["on"]=False; await e.reply("Wapas aa gaya bhai! Back to online 🔥")
@client.on(events.NewMessage(pattern=r"\.autoreact (on|off)"))
async def autoreact(e):
    AUTOREACT["on"]=(e.pattern_match.group(1)=="on"); await e.reply(f"Auto React Mood Wise {'ON ❤️🔥😂' if AUTOREACT['on'] else 'OFF'}")
@client.on(events.NewMessage(pattern=r"\.autoreply (on|off)"))
async def autoreply(e):
    AFK["on"]=(e.pattern_match.group(1)=="on"); await e.reply(f"Auto Reply {'ON 💬' if AFK['on'] else 'OFF'}")
@client.on(events.NewMessage(pattern=r"\.autopin (on|off)"))
async def autopin(e):
    AUTOPIN["on"]=(e.pattern_match.group(1)=="on"); await e.reply(f"Auto Pin Har Msg {'ON 📌' if AUTOPIN['on'] else 'OFF'}")
@client.on(events.NewMessage(pattern=r"\.autodelete (on|off)"))
async def autodel(e):
    AUTODELETE["on"]=(e.pattern_match.group(1)=="on"); await e.reply(f"Auto Delete {'ON 🗑️' if AUTODELETE['on'] else 'OFF'}")
@client.on(events.NewMessage(pattern=r"\.typing"))
async def typing_cmd(e):
    async with client.action(e.chat_id, 'typing'): await e.reply("Typing wala effect dekh liya? 😎")
@client.on(events.NewMessage(pattern=r"\.online"))
async def online_cmd(e): await e.reply("Ab tu online dikh raha hai, sabko lagega tu yahi hai 😎")

# ===== PRANK =====
@client.on(events.NewMessage(pattern=r"\.hack"))
async def hack(e):
    m=await e.reply("Hacking start... 0%")
    for p in [20,50,80,100]: await m.edit(f"Hacking... {p}%")
    await m.edit("😂 Mazak tha bhai! Koi hack nahi hua, bas prank tha!")
@client.on(events.NewMessage(pattern=r"\.fakeid (.+)"))
async def fakeid(e): await e.reply(f"🪪 **FAKE ID**\nName: {e.pattern_match.group(1)}\nID: {random.randint(10000,99999)}\nCity: Indore\nStatus: Pro Gamer 😂 (Ye mazak wali ID hai)")
@client.on(events.NewMessage(pattern=r"\.wasted"))
async def wasted(e): await e.reply("💀 **WASTED** - GTA Style!")

# ===== GROUP =====
@client.on(events.NewMessage(pattern=r"\.rules"))
async def rules(e): await e.reply("**Group Rules:**\n1. Gaali nahi\n2. Spam nahi\n3. Sabki izzat karo\n4. Maza karo 🔥")
@client.on(events.NewMessage(pattern=r"\.welcome"))
async def welcome(e): await e.reply("Welcome bhai! Group me aane ke liye dhanyavad 🎉🔥")
@client.on(events.NewMessage(pattern=r"\.goodmorning"))
async def gm(e): await e.reply("Good Morning! Chai pee li? ☕🌅")
@client.on(events.NewMessage(pattern=r"\.goodnight"))
async def gn(e): await e.reply("Good Night! Sweet dreams 😴🌙")
@client.on(events.NewMessage(pattern=r"\.birthday (.+)"))
async def bday(e): await e.reply(f"🎂 Happy Birthday {e.pattern_match.group(1)}! 🎉 Party kab de raha hai?")

# ===== AUTO HANDLER - MOOD REACT + PIN HAR MSG =====
@client.on(events.NewMessage(incoming=True))
async def auto_handler(e):
    # Auto Reply - Private me
    if e.is_private and AFK["on"] and not e.out:
        try: await e.reply(AFK["msg"])
        except: pass
    # Auto React - Mood Wise
    if AUTOREACT["on"] and not e.out and e.text:
        try:
            emoji = mood_emoji(e.text)
            await e.react(emoji)
        except: pass
    # Auto Pin - HAR MSG PIN
    if AUTOPIN["on"]:
        try:
            await client.pin_message(e.chat_id, e.id, notify=False)
        except: pass
    # Auto Delete
    if AUTODELETE["on"] and e.out:
        await asyncio.sleep(60)
        try: await e.delete()
        except: pass

# ===== KEEP ALIVE =====
from flask import Flask
import threading
app = Flask(__name__)
@app.route("/")
def home(): return "Bot is alive!"
threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()
print("Bot started...")
client.start()
client.run_until_disconnected()
