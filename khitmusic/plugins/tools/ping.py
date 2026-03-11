
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from khitmusic import app
from khitmusic.core.call import SANYA
from khitmusic.utils import bot_sys_stats
from khitmusic.utils.decorators.language import language
from khitmusic.utils.inline import supp_markup
from config import BANNED_USERS
import random

STARK_IMG = [
"https://files.catbox.moe/lsbtud.jpg",
"https://files.catbox.moe/stqxy1.jpg",
"https://files.catbox.moe/wz4ndo.jpg",
"https://files.catbox.moe/02yas7.jpg",
"https://files.catbox.moe/9qi4ot.jpg",
"https://files.catbox.moe/e813zc.jpg",
"https://files.catbox.moe/cdc5cz.jpg",
"https://files.catbox.moe/83zj85.jpg"
]


@app.on_message(filters.command("ping", prefixes=["/", ""]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        random.choice(STARK_IMG),
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await SANYA.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
