import os
import telebot
import fnmatch

bot = telebot.TeleBot("your token goes here", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['flac'])
def download(message):
    chat_id = message.chat.id
    songLink = message.text
    str = songLink
    if str.find("track")!=-1:
        print("is track")
        realSong = songLink.replace("/flac", "")
        bot.reply_to(message, "Fetching song...")
        DownloadSong = "bash magic.sh '{}' -f -t".format(realSong)
        os.system(DownloadSong)
        f = open("link.txt", "r")
        text = f.read()
        bot.send_message(chat_id, text)
        cleansong = "rm -rf link.txt"
        os.system(cleansong)
    else:
        bot.send_message(chat_id, "bot does not support non-track")

bot.infinity_polling()

