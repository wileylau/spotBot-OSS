import os
import telebot
import fnmatch

bot = telebot.TeleBot("your token goes here", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def download(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        DownloadSong = "grab '{}'".format(songLink)
        os.system(DownloadSong)
        bot.reply_to(message, "Uploading song...")
        for flac in os.listdir('.'):
            if fnmatch.fnmatch(flac, '*.flac'):
                comp = "bash magic.sh '{}'".format(flac)
                os.system(comp)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        bot.send_message(chat_id, "bot does not support non-track")

bot.infinity_polling()

