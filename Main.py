from telegram.ext import Updater, CommandHandler
from Commands import GetText
import os

def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hi {first_name}, nice to meet you! \n I am a OCR bot! \n Developer: @PratyushDev")

def help(update, context):
    update.message.reply_text("Hi there! \n Send me a image... and then reply to the message with `/textimg`! ")

def main():
    updater = Updater(os.environ['BOTTOKEN'] , use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("textimg", GetText.text))
    dispatcher.add_handler(CommandHandler("help", help))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()