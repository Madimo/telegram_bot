#!/usr/bin/env python3

import telegram
from telegram.ext import Updater, CommandHandler
from config import token

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='I am MadimoBot!')

def my_chat_id(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id, text='Your chat_id is:\n\n%s' % (chat_id))

def main():
	updater = Updater(token=token)

	dispatcher = updater.dispatcher
	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(CommandHandler('my_chat_id', my_chat_id))
		
	updater.start_polling()
	
if __name__ == '__main__':
	main()
