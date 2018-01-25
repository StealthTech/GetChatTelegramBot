from telegram.ext import Updater

import settings
from handlers.commands import init_command_handlers
from utils import print_bot_message

if __name__ == '__main__':
    token = settings.TELEGRAM_BOT_TOKEN

    if token is None:
        print_bot_message('Telegram bot token not found. Check configuration files.')
        exit()

    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    init_command_handlers(dispatcher)

    print_bot_message('Long polling started...')
    updater.start_polling()
