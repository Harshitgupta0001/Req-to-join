import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7528651819:AAFZb1Ihy5tBPUNcSm3p5MjNM-VKHS9y5Xs")
API_ID = int(os.environ.get("API_ID", "25797857"))
API_HASH = os.environ.get("API_HASH", "77717127ece56fac64ebea6250db8bb7")


OWNER_ID = int(os.environ.get("OWNER_ID", "6359874284"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://harsh:gunnu@cluster0.0uqkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Movieseerabot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002370247427"))

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002237286662"))

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", "-1002237286662"))


REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "-1002496822688"))



START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/7Lwm9CG/photo-2025-02-02-07-36-38-7466722484281147420.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/2tr6wx6")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "300")) # auto delete in seconds


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

DISABLE_CHANNEL_BUTTON = False if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b>Please search your movie in <a href=https://t.me/moviesworldsupportzone>MoviesEera_Search_zone</a></b>"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>I Aᴍ Movie Bᴏᴛ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Movie/series Fɪʟᴇs Fʀᴏᴍ <a href=https://t.me/Movies_Eera>Movies_Eera</a></b>.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Movie/series/Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a >Tᴜᴛᴏʀɪᴀʟ</a></b>")

SHORTENER_API_MESSAGE = """<b>Tᴏ ᴀᴅᴅ ᴏʀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ Sʜᴏʀᴛɴᴇʀ Wᴇʙsɪᴛᴇ API, /api (ᴀᴘɪ)
            
<b>Ex: /api 𝟼LZǫ𝟾𝟻sjsjsjdjduduje

<b>Cᴜʀʀᴇɴᴛ Wᴇʙsɪᴛᴇ: {base_site}

Cᴜʀʀᴇɴᴛ Sʜᴏʀᴛᴇɴᴇʀ API:</b> `{shortener_api}`

If You Want To Remove Api Then Copy This And Send To Bot - `/api None`"""



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
    about = f"""<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/Movies_Eera>Movies_Eera</a>
‣ Owner: <a href='https://t.me/hgbotz'>HGBOTZ</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""
