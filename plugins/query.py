import shutil
import time
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import Config, Txt
from helper.database import db
import random
import psutil
from info import AUTH_CHANNEL
from syd import is_req_subscribed
from helper.utils import humanbytes


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.START_TXT.format(query.from_user.mention),

            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    '⛅ Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/Bot_Cracker'),
                InlineKeyboardButton(
                    'Sᴜᴩᴩᴏʀᴛ ⛈️', url='https://t.me/+O1mwQijo79s2MjJl')
            ], [
                InlineKeyboardButton('❄️ Δʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('ʙΔᴄᴋ-ᴜᴩ 🗯️', url='https://t.me/+1C8Usv5MSzA3MGM1'),
                InlineKeyboardButton('Hᴇʟᴩ ❗', callback_data='help')
            ], [InlineKeyboardButton('⊛ Jᴏɪɴ ᴍᴏᴠɪєꜱ CʜᴀɴɴᴇL ⊛', url='https://t.me/Mod_Moviez_X')
            ]])
        )
        
    elif data == "help":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.HELP_TXT

            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ", callback_data="how")
            ], [
                InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="pic"),
                InlineKeyboardButton("ᴄᴀᴩᴛɪᴏɴ", callback_data="cap")
            ], [
                InlineKeyboardButton("ꜱᴜꜰꜰɪx ᴀɴᴅ ᴩʀᴇꜰɪx", callback_data="sufpre")
            ], [
                InlineKeyboardButton("ᴅᴜᴍᴩ ᴄʜᴀɴɴᴇʟ", callback_data="dump")
            ], [
                InlineKeyboardButton("ᴍᴇᴛᴀᴅᴀᴛᴀ", callback_data="meta")
            ], [
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )

    elif data == "sydcheck":
        if AUTH_CHANNEL and not await is_req_subscribed:
          await query.answer("ʀᴇQᴇᴜꜱᴛ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒 Dᴏɴᴛ ᴛʀʏ ᴛᴏ ꜱʜᴏᴡ ʏᴏᴜʀ ᴏᴠᴇʀꜱᴍᴀʀᴛɴᴇꜱꜱ ᴩʟᴢ🥲🥲", show_alert=True)
          return
        await query.message.edit_text("<b>Oᴋ✅, ʏᴏᴜ ᴄΔɴ ᴄᴏɴᴛɪɴᴜᴇ ʏᴏᴜʀ ᴩʀᴏᴄᴇꜱꜱ.... Δɴᴅ Tʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ... 🧭\nPʟᴇᴀꜱᴇ Rᴇ-Fᴏʀᴡᴀʀᴅ ʏᴏᴜʀ Ғɪʟᴇ Tᴏ ᴄᴏɴᴛɪɴᴜᴇ... 🪭</b>")


    elif data == "meta":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.META_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    elif data == "dump":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.DUMP_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    
    elif data == "cap":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.CAP_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    elif data == "how":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.HOW_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    elif data == "sufpre":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.SUFPRE_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    elif data == "pic":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.PIC_TXT,
            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )
    elif data == "about":
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.ABOUT_TXT.format(client.mention),

            ),

            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᐊ ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ✘", callback_data="close")
                
            ]])
        )

    elif data == 'stats':
        buttons = [[InlineKeyboardButton(
            '• ʙᴀᴄᴋ', callback_data='start'), InlineKeyboardButton('⟲ ʀᴇʟᴏᴀᴅ', callback_data='stats')]]
        reply_markup = InlineKeyboardMarkup(buttons)
        currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(
            time.time() - Config.BOT_UPTIME))
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        await query.message.edit_media(
            InputMediaPhoto(
                random.choice(Config.PICS),
                Txt.STATS_TXT.format(
                    currentTime, total, used, disk_usage, free, cpu_usage, ram_usage)
            ),
            reply_markup=reply_markup
        )

    elif data == "season_false":
        await db.set_sydson(user_id, "False")
        await query.message.edit_text(
            text="Sᴇᴛ ᴛʀᴜᴇ ᴏʀ ꜰᴀʟꜱᴇ, ɪꜰ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ ɪꜱ ᴛᴏ ʙᴇ ɪɴ ꜰɪʟᴇ ᴇᴠᴇʀʏᴛɪᴍᴇ (ɪꜰ ꜰɪʟᴇ ᴅᴏɴᴛ ʜᴀᴠᴇ ꜱᴇᴀꜱᴏɴ ɴᴏ. ɪᴛ ᴡɪʟʟ ʙᴇ ᴅᴇꜰᴜᴀʟᴛ ᴛᴏ 1) ᴏʀ ꜰᴀʟꜱᴇ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴇᴀꜱᴏɴ ᴛᴀɢ",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Tʀᴜᴇ ✅", callback_data="season_true")
            ],[
                InlineKeyboardButton("✖️ Close", callback_data="close")
            ]])          
        )
            
    elif data == "season_true":
        await db.set_sydson(user_id, "True")
        await query.message.edit_text(
            text="Sᴇᴛ ᴛʀᴜᴇ ᴏʀ ꜰᴀʟꜱᴇ, ɪꜰ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ ɪꜱ ᴛᴏ ʙᴇ ɪɴ ꜰɪʟᴇ ᴇᴠᴇʀʏᴛɪᴍᴇ (ɪꜰ ꜰɪʟᴇ ᴅᴏɴᴛ ʜᴀᴠᴇ ꜱᴇᴀꜱᴏɴ ɴᴏ. ɪᴛ ᴡɪʟʟ ʙᴇ ᴅᴇꜰᴜᴀʟᴛ ᴛᴏ 1) ᴏʀ ꜰᴀʟꜱᴇ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴇᴀꜱᴏɴ ᴛᴀɢ",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Fᴀʟꜱᴇ ✖️", callback_data="season_false")
            ],[
                InlineKeyboardButton("✖️ Close", callback_data="close")
            ]])          
        )

    elif data == 'userbot':
        userBot = await db.get_user_bot(query.from_user.id)

        text = f"Name: {userBot['name']}\nUserName: @{userBot['username']}\n UserId: {userBot['user_id']}"

        await query.message.edit(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('❌ ʀᴇᴍᴏᴠᴇ ❌', callback_data='rmuserbot')], [InlineKeyboardButton('✘ ᴄʟᴏsᴇ ✘', callback_data='close')]]))

    elif data == 'rmuserbot':
        try:
            await db.remove_user_bot(query.from_user.id)
            await query.message.edit(text='**User Bot Removed Successfully ✅**', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✘ ᴄʟᴏsᴇ ✘', callback_data='close')]]))
        except:
            await query.answer(f'Hey {query.from_user.first_name}\n\n You have already deleted the user')

    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()


import os
import zipfile
from tempfile import TemporaryDirectory
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query()
async def callback_hanler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    replied = callback_query.message.reply_to_message

    if not replied or not (replied.document or replied.video or replied.audio):
        return await callback_query.answer("Please reply to a valid file.", show_alert=True)

    media = replied.document or replied.video or replied.audio
    file_name = media.file_name or "file"

    # (2) Create Archive
    if data == "create_archive":
        await callback_query.answer("Creating ZIP archive...")

        with TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, file_name)

            # Download the original file
            await client.download_media(replied, file_path)

            # Create a ZIP archive
            zip_name = f"{os.path.splitext(file_name)[0]}.zip"
            zip_path = os.path.join(temp_dir, zip_name)
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, arcname=file_name)

            # Send the zipped file
            await callback_query.message.reply_document(
                document=zip_path,
                caption=f"`{file_name}` has been archived into `{zip_name}`.",
            )

    elif data == "extract_archive":
        await callback_query.answer("Extracting ZIP archive...")

        # Check extension
        if not file_name.lower().endswith(".zip"):
            return await callback_query.message.reply(
                "❌ Only `.zip` files are supported for extraction."
            )

        with TemporaryDirectory() as temp_dir:
            zip_path = os.path.join(temp_dir, file_name)
            await client.download_media(replied, zip_path)

            extract_dir = os.path.join(temp_dir, "extracted")
            os.makedirs(extract_dir, exist_ok=True)

            try:
                with zipfile.ZipFile(zip_path, "r") as zipf:
                    zipf.extractall(extract_dir)
            except zipfile.BadZipFile:
                return await callback_query.message.reply("❌ Invalid or corrupted ZIP file.")

            file_list = os.listdir(extract_dir)
            if not file_list:
                return await callback_query.message.reply("⚠️ ZIP file was empty.")

            for extracted_file in file_list:
                full_path = os.path.join(extract_dir, extracted_file)
                if os.path.isfile(full_path):
                    await callback_query.message.reply_document(
                        document=full_path,
                        caption=f"Extracted: `{extracted_file}`",
                    )
     
    elif data == "remove_audio":
        await callback_query.answer("Removing audio from video...")

        with TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, file_name)
            await client.download_media(replied, file_path)

            output_path = os.path.join(temp_dir, f"{base_name}_noaudio{ext}")

            # Run ffmpeg to remove audio
            cmd = ["ffmpeg", "-i", file_path, "-c", "copy", "-an", output_path]
            try:
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                # Send the audio-less video
                await callback_query.message.reply_document(
                    document=output_path,
                    caption=f"`{file_name}` with audio removed.",
                )
            except subprocess.CalledProcessError as e:
                await callback_query.message.reply(
                    f"❌ Failed to remove audio.\nError: `{e}`"
                )
