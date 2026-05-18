import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, filters

# 1. Flask App Setup (Render ke liye Main Engine)
app = Flask('')

@app.route('/')
def home():
    return "Userbot Engine is 100% active and running!"

# 2. Config Details
API_ID = 24953130
API_HASH = '30512173bd0a1fdb55f85e46860a9638'
TARGET_CHANNEL = -1003964950414
SOURCE_CHANNEL = 'Avibum'
STRING_SESSION = "BQF8wSoAiP3lPgPqQIqD4HsT5aPg6Rie_lyuMHmi0KNFjCYwSGR6IPCvBai215an1IwOkwaY5J0juciQludMwGpbHK35DcRgZ1yhPxg5rLf6SffZ8gOsUGLA7D2MLbxCl50gIrEEc-Wuo8dJtRQm8u5yklXz0RC7nY4Ei9MaH_z6bx5R04_EDD7zDt5jYxo-GDoXk1azCdw3s3KSNlrCrtgQpqomTdROdaduuUYH0y-Xjb69tvuHlN8qQ7JMdmqEnNR0mITiGoZTPEMeime91x2qI1GV436PoILaRNj_C09zjMF-TnNRhNHKx3aTmgb5UvI8NnZTjJDayfW6bNpDRW_3-x2yGQAAAAIJT9FaAA"

# 3. Userbot Worker Setup
async def run_userbot():
    print("Initializing Pyrogram Client...")
    bot = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
    
    @bot.on_message(filters.chat(SOURCE_CHANNEL))
    async def forward_message(client, message):
        try:
            await message.copy(TARGET_CHANNEL)
            print("🟢 Signal successfully cloned to your channel!")
        except Exception as e:
            print(f"❌ Forward error: {e}")
            
    await bot.start()
    print("🟢 Userbot successfully authenticated and listening for signals!")
    while True:
        await asyncio.sleep(3600)

def start_bot_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_userbot())

# 4. Main Entry Point (Render isey run karega)
if __name__ == '__main__':
    # Userbot ko background worker thread mein bhejna
    bot_thread = Thread(target=start_bot_loop)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Main thread par Flask ko chalu rakhna taki Render active rahe
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting Web Server on port {port}...")
    app.run(host='0.0.0.0', port=port)
