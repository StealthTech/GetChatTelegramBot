import settings
from telegram import ParseMode


def cmd_about(bot, update):
    chat_id = update.message.chat_id
    text = 'Simple chat bot for getting chat ids.\n\n*Author:* {} {}\n*Version:* {}' \
           ''.format(settings.AUTHOR_FULLNAME, settings.AUTHOR_TELEGRAM, settings.VERSION)
    bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)
