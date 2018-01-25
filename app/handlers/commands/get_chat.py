def cmd_get_chat(bot, update):
    chat_id = update.message.chat_id
    text = 'Current chat ID: {}'.format(chat_id)
    bot.send_message(chat_id, text)
