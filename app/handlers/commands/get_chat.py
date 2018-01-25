from telegram import ParseMode


def cmd_get_chat(bot, update):
    chat_id = update.message.chat_id
    text = '*Current chat description*\n\n*Chat ID:* {}'.format(chat_id)
    bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)
