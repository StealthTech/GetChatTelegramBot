from utils.config import Configuration

conf = Configuration('app.conf', markdown='main')

PROJECT_NAME = conf.get('GENERIC', 'project_name')
VERSION = conf.get('GENERIC', 'version') or 'Aftermath'
TELEGRAM_BOT_TOKEN = conf.get('TELEGRAM', 'token')

AUTHOR_FULLNAME = conf.get('ABOUT', 'author_fullname')
AUTHOR_TELEGRAM = conf.get('ABOUT', 'author_telegram')
