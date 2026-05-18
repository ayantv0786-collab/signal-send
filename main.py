import os
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events

# Render ko active rakhne ke liye Web Server
app = Flask('')

@app.route('/')
def home():
    return "Userbot is running 24/7!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Aapki actual details jo maine set kar di hain
API_ID = 24953130
API_HASH = '30512173bd0a1fdb55f85e46860a9638'
TARGET_CHANNEL = -1003964950414
SOURCE_CHANNEL = 'Avibum'

# Client setup (Aapke session ko persistent rakhne ke liye base directory use karega)
client = TelegramClient('/opt/render/project/src/session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def my_event_handler(event):
    try:
        # Signal aate hi turant forward karega
        await client.send_message(TARGET_CHANNEL, event.message)
    except Exception as e:
        print(f"Forwarding error: {e}")

if __name__ == '__main__':
    # Web server start karna
    t = Thread(target=run_flask)
    t.start()
    
    print("Userbot starting...")
    client.start()
    client.run_until_disconnected()
