import re
from pyrogram import filters
import random
from Mickey import Mickey

@MickeyBot.on_message(filters.command(["gn", "n", "oodnight", "ood Night", "ood night"], prefixes=["/", "g", "G"]))
async def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    
    if send_sticker:
        sticker_id = await get_random_sticker()  # Ensure this is awaited
        await nexichat.send_sticker(message.chat.id, sticker_id)  # Await send_sticker
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} 😴 **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")
    else:
        emoji = await get_random_emoji()  # Ensure this is awaited
        await Mickey.send_message(message.chat.id, emoji)  # Await send_message
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} {emoji} **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")

# Define async functions for stickers and emoji
async def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E", #sticker1
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E", #sticker2
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA", #sticker3
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)

async def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
