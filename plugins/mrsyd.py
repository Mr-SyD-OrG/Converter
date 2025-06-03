from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.document)
async def handle_fle(client: Client, message: Message):
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Create Archive", callback_data="create_archive")],
            [InlineKeyboardButton("➕ Extract Archive", callback_data="extract_archive")],
            [InlineKeyboardButton("➕ remove Audion ", callback_data="remove_audio")],
            [InlineKeyboardButton("➕ Create Archive", callback_data="create_archive")],
            [InlineKeyboardButton("➕ Create Archive", callback_data="create_archive")],
            [InlineKeyboardButton("➕ Create Archive", callback_data="create_archive")]
        ]
    )
    await message.reply(
        "What would you like to do with this file?",
        reply_markup=buttons,
        quote=True  # ensures it replies directly to the media message
    )
