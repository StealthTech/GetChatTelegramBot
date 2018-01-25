from telegram import ParseMode


def cmd_start(bot, update):
    chat_id = update.message.chat_id
    text = '*Available commands*\n /getchat - Shows current chat ID'
    bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)
