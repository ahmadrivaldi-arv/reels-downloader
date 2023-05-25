import telebot
from selenium.common.exceptions import TimeoutException
from lib.reel import is_instagram_reels_url, download_reels

bot = telebot.TeleBot("6058290476:AAFHT6fpeYuYwlQP46TNhtKuuOsorAYQ1Zs", parse_mode=None)


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    if not is_instagram_reels_url(message.text):

        bot.reply_to(message, "The given url is not valid")

    else:

        bot.send_message(message.chat.id, "Please wait! Processing a video...")

        bot.send_chat_action(message.chat.id, action="upload_video")

        try:
            bot.send_video(message.chat.id, download_reels(message.text))
        except TimeoutException:
            bot.send_message(message.chat.id, "Unable to download the video\n\nMake sure the given url is valid")


bot.infinity_polling()
