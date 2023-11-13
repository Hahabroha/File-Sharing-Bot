#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : @Badal6667Rai! 👑</a>\n○ Language : <code>Python 3</code>\n○ Channel : <a href='https://t.me/+cv6nIOANnYQ2MzY1'>Anime Channel</a>\n○ Source Code : <a href='https://t.me/sourcebotcode/2'> HERE WE GO ✅</a>\n○ Admin : @AbhishekOP0 👑\n○</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
