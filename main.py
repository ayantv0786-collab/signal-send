import os
import asyncio
from flask import Flask
from threading import Thread
from telethon import TelegramClient

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

# Render se environment variables uthana
PHONE = os.environ.get('PHONE')
CODE = os.environ.get('CODE')

async def main():
    client = TelegramClient('/opt/render/project/src/session_name', API_ID, API_HASH)
    
    print("Connecting to Telegram...")
    await client.connect()
    
    if not await client.is_user_authorized():
        if not CODE:
            # Agar code abhi tak Render me nahi dala hai, toh pehle phone number bhejega
            print(f"Sending code request to {PHONE}...")
            await client.send_code_request(PHONE)
            print("🔴 STEP A COMPLETED: Ab Render me jaakar CODE variable daliye!")
            return
        else:
            # Agar code mil gaya hai, toh login complete karega
            try:
                print("Attempting to sign in with code...")
                await client.sign_in(PHONE, CODE)
                print("🟢 LOGIN SUCCESSFUL!")
            except Exception as e:
                print(f"Login error: {e}")
                return

    print("Userbot started and monitoring channel...")
    from telethon import events
    
    @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        try:
            await client.send_message(TARGET_CHANNEL, event.message)
        except Exception as e:
            print(f"Forward error: {e}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()
    asyncio.run(main())
