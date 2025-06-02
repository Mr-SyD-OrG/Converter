import random
import logging
from pyrogram import Client, filters, enums
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, CallbackQuery
from helper.database import db
from config import Config, Txt
from info import AUTH_CHANNEL
from helper.utils import is_req_subscribed
import humanize
from time import sleep

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):

    if message.from_user.id in Config.BANNED_USERS:
        await message.reply_text("Sorry, You are banned.")
        return

    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            '⛅ Uᴘᴅᴀᴛᴇꜱ', url='https://t.me/Bot_Cracker'),
        InlineKeyboardButton(
            ' Sᴜᴘᴘᴏʀᴛ 🌨️', url='https://t.me/+O1mwQijo79s2MjJl')
    ], [
        InlineKeyboardButton('❄️ Δʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('βᴏᴛꜱ ⚧️', url='https://t.me/Bot_Cracker/17'),
        InlineKeyboardButton(' Hᴇʟᴩ ❗', callback_data='help')
    ], [InlineKeyboardButton('⚙️ sᴛΔᴛs ⚙️', callback_data='stats')]])
    if Config.PICS:
        await message.reply_photo(random.choice(Config.PICS), caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
        
@Client.on_message(filters.private & filters.command("season"))
async def sydson(client, message):
    mrsyd = await db.get_sydson(message.from_user.id)
    if mrsyd == "True":
        button = InlineKeyboardMarkup([[
          InlineKeyboardButton('Fᴀʟꜱᴇ ✖️', callback_data='season_false')
          ],[
          InlineKeyboardButton("✖️ Close", callback_data="close")
        ]])
    else:
        button = InlineKeyboardMarkup([[
          InlineKeyboardButton('Tʀᴜᴇ ✅', callback_data='season_true')
          ],[
          InlineKeyboardButton("✖️ Close", callback_data="close")
        ]])
    await message.reply_text(text="Sᴇᴛ ᴛʀᴜᴇ ᴏʀ ꜰᴀʟꜱᴇ, ɪꜰ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ ɪꜱ ᴛᴏ ʙᴇ ɪɴ ꜰɪʟᴇ ᴇᴠᴇʀʏᴛɪᴍᴇ (ɪꜰ ꜰɪʟᴇ ᴅᴏɴᴛ ʜᴀᴠᴇ ꜱᴇᴀꜱᴏɴ ɴᴏ. ɪᴛ ᴡɪʟʟ ʙᴇ ᴅᴇꜰᴜᴀʟᴛ ᴛᴏ 1) ᴏʀ ꜰᴀʟꜱᴇ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴇᴀꜱᴏɴ ᴛᴀɢ", reply_markup=button)   


#@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    
    if file.file_size > 2000 * 1024 * 1024:
        if not await db.is_user_bot_exist(Config.ADMIN[0]):
            return await message.reply_text("**⚠️ Sᴏʀʀy Bʀᴏ, Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ ᴩʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ 🥺..... ᴩʟᴇᴀꜱᴇ ʙᴇᴄᴀᴍᴇ..... ⚡**")

    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("✖️ CᴀɴᴄᴇL ✖️", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ 📝", callback_data="rename")],
                   [InlineKeyboardButton("✖️ CᴀɴᴄᴇL ✖️", callback_data="close")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass
@Client.on_message(filters.command("start") & filters.chat(-1002687879857))
async def sydstart(client, message):
    await message.reply_text(".")
