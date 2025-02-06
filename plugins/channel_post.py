import re
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats', 'totalreq', 'clear_req_1', 'clear_req_2']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    # Extract file name if available
    file_name = "Unknown File"
    if message.document:
        file_name = message.document.file_name
    elif message.video:
        file_name = message.video.file_name if message.video.file_name else "Video File"
    elif message.audio:
        file_name = message.audio.file_name if message.audio.file_name else "Audio File"

    if file_name != "Unknown File":
        file_name = file_name.rsplit('.', 1)[0]  # Remove the last file extension (e.g., .mkv, .mp4)
        file_name = file_name.replace('.', ' ')  # Replace dots with spaces
        file_name = file_name.replace('_', ' ')  # Replace underscores with spaces

    chnl_reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📌 GET YOUR FILE", url=f'{link}'), 
        ],[
         InlineKeyboardButton("Copy Link", copy_text=f'{link}')]
                                        ])

    await reply_text.edit(f"<b>{file_name}</b>", reply_markup=reply_markup, disable_web_page_preview = True)
    #await message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote = True) 
    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(chnl_reply_markup)





@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
