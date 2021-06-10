from pyrogram import Client, filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"])& filters.private)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
                                            "Support Group", url="https://t.me/Musicwold20210"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/Godzilla_bots")
                                    ],[
                                      InlineKeyboardButton(
                                            "Admin S E N U L A™ ✔️", url="https://t.me/Senulatr")]
    ])
    welcomed = f"හායි <b>{message.from_user.first_name}</b>\n/help වැඩි විස්තර සඳහා"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
