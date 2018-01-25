from telegram.ext import CommandHandler
from .get_chat import cmd_get_chat
from .start import cmd_start
from .about import cmd_about


__handler_map = {
    'start': cmd_start,
    'getchat': cmd_get_chat,
    'about': cmd_about,
}


def init_command_handlers(dispatcher):
    for k, v in __handler_map.items():
        handler = CommandHandler(k, v)
        dispatcher.add_handler(handler)
