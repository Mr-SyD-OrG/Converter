from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message



@Client.on_message(filters.document)
async def handle_file(client: Client, message: Message):
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Create Archive", callback_data="create_archive")]
        ]
    )
    await message.reply(
        "What would you like to do with this file?",
        reply_markup=buttons,
        quote=True  # ensures it replies directly to the media message
    )
