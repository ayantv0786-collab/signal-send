import os
from flask import Flask
from threading import Thread
from pyrogram import Client, filters

app = Flask('')

@app.route('/')
def home():
    return "Userbot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Aapki details fixed hain
API_ID = 24953130
API_HASH = '30512173bd0a1fdb55f85e46860a9638'
TARGET_CHANNEL = -1003964950414
SOURCE_CHANNEL = 'Avibum'

# Pyrogram session string se direct login bina kisi OTP ke
STRING_SESSION = os.environ.get('SESSION')
app_bot = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

@app_bot.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_message(client, message):
    try:
        # Message/Signal aate hi turant aapke channel me copy ho jayega
        await message.copy(TARGET_CHANNEL)
    except Exception as e:
        print(f"Forward error: {e}")

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()
    
    print("Userbot is starting on Pyrogram...")
    app_bot.run()
