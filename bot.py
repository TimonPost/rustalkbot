#!/usr/bin/python
# -*- coding: utf-8 -*-


#=========================#
#        IMPORTS
#=========================#
from telegram.ext import (CommandHandler, Updater, Dispatcher,
                            MessageHandler, Filters)
from glob_vars import TOKEN
import logging
import datetime


#Gets logging system
logger = logging.getLogger(__name__)


def create_logfile_name():
    return "logs/" + datetime.datetime.now().strftime("%d%m%Y-%H%M%S") + ".log"


def create_logs():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        filename=create_logfile_name(),
                        filemode='w',
                        level=logging.DEBUG)


def error(bot, update, error):
    logging.warning('An update "%s" has caused an error "%s".' % update, error)


#Bot's action to the command /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi, %s!" % update.message.from_user.first_name)


def greet_newbies(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Greetings, %s!" % update.message.from_user.first_name)


def main():
    updater = Updater(TOKEN)
    create_logs()

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet_newbies))
    dp.add_error_handler(error)

    
    updater.start_polling()

    updater.idle()
    


if __name__ == '__main__':
    main()