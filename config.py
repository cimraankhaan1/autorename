import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    STRING_SESSION = "1AZWarzcBuwwbs6gs9lNA6uVW1g1BZkZnxKLZp2gwSJ-HKV2niepAY3SQGFpNis65WKljBhWyWC_nIt_hx7UFkB1PBnY7VY6V9h5FOiaQse3UPGtC2pMJkZORxqKjjk49TEj3GhnqJJ3GlKDRSz8L9DQ8Aj8gvPs-QmW1c8CutwaqX76fducbGLwJ5myImTJGKb83rnqksTF7TGAZS3RD9SJhAnqlM3pdFCvLndsJle_PXJ5cpZFQHfmpDbpByPYDnnuA4hZ_ul4F0nTs5p__hgPypvLTk4b_eiwsIEYEHViKZ3eKhAlbY5gnVczCWFOEuAv77dB048X1tj2ZFfFvqgna5wOgB7s="

    # pyro client config
    API_ID    = os.environ.get("API_ID", "27672739")
    API_HASH  = os.environ.get("API_HASH", "f48d0da94f2622364ab24eb0d911903c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8088534251:AAFwOd8-S6NCucBb-unMGh4QZKYabU3Sq7g") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","khaanbarwaani")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5069198943').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', '-1002434765617').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002318997215"))
    PORT = int(os.environ.get("PORT", "8040"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @LKD_AK</b>

<b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @LKD_AK</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/LKD_AK'>PandaWep</a>
    
<b>♻️ Bot Made By :</b> @LKD_AK"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @LKD_AK
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - LKD_AK@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @LKD_AK To Help """





