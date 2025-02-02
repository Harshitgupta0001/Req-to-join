import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7528651819:AAFZb1Ihy5tBPUNcSm3p5MjNM-VKHS9y5Xs")
API_ID = int(os.environ.get("API_ID", "25797857"))
API_HASH = os.environ.get("API_HASH", "77717127ece56fac64ebea6250db8bb7")


OWNER_ID = int(os.environ.get("OWNER_ID", "6359874284"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Venkat3823:Venkat3823@cluster0.ig0oc9y.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Naruto_TAF")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002093054178"))

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", "-1002333230282"))


REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "-1002388961956"))



START_PIC = os.environ.get("START_PIC", "https://4kwallpapers.com/images/wallpapers/naruto-uzumaki-3840x2160-18710.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/2tr6wx6")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8040")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6299192020]
    for x in (os.environ.get("ADMINS", "6359874284").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>I Aᴍ Aɴɪᴍᴇ Bᴏᴛ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Aɴɪᴍᴇ Fɪʟᴇs Fʀᴏᴍ <a href=https://t.me/Tamil_Anime_Files>Tᴀᴍɪʟ Aɴɪᴍᴇ Fɪʟᴇs</a></b>.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Tamil_Anime_Files/893>Tᴜᴛᴏʀɪᴀʟ</a></b>")




ADMINS.append(OWNER_ID)
ADMINS.append(6299192020)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href='https://t.me/Occoccicfx_bot'>[AW] File store bot 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Anime_Warrior_Tamil'>AWT BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+NITVxLchQhYzNGZl'>AWT Developer</a>
    
<b>😈 Bot Made By :</b> @AWT_Bot_Developer"""
