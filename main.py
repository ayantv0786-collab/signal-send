import os
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events

# Render ko active rakhne ke liye Flask Web Server
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# Aapki final details jo direct chalengi
API_ID = 24953130
API_HASH = '30512173bd0a1fdb55f85e46860a9638'
BOT_TOKEN = "8613146352:AAHh2-czJhp23GlsOo0VjvZ1n2GGlsyv48I"
TARGET_CHANNEL = -1003964950414
SOURCE_CHANNEL = 'Avibum'

# Bot client setup (Bina kisi OTP ya login ke)
bot_client = TelegramClient('bot_session_final', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        # Message/Signal aate hi turant aapke channel me forward ho jayega
        await bot_client.send_message(TARGET_CHANNEL, event.message)
        print("Signal forwarded successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Web server ko alag thread me chalana
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    print("Telethon Bot started successfully...")
    bot_client.run_until_disconnected()
