from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (ධාවන ලැයිස්තුව නොවේ) Just Send Youtube Url"
    await message.reply_text(helptxt)
