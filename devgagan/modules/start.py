from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ᴍʏ ᴀʟʟ sᴇʀᴠɪᴄᴇs", url="https://t.me/+r5vH1CeRVzU5OTY1")],
        [InlineKeyboardButton("ᴍʏ ғʀᴇᴇ sᴇʀᴠɪᴄᴇs", url="https://t.me/+2HQSwat0STY4YmM9")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://graph.org/file/a06275c5b4e838e2df0e5-664ae5f4d543dfd30d.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
