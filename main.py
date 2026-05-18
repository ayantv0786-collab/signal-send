import os
from flask import Flask
from threading import Thread
import telebot

app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

BOT_TOKEN = "8613146352:AAHh2-czJhp23GlsOo0VjvZ1n2GGlsyv48I"
TARGET_CHANNEL = -1003964950414

bot = telebot.TeleBot(BOT_TOKEN)

@bot.channel_post_handler(func=lambda message: True)
def handle_post(message):
    try:
        bot.forward_message(chat_id=TARGET_CHANNEL, from_chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()
    print("Bot is starting...")
    bot.infinity_polling()
