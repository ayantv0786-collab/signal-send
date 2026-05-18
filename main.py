import asyncio
from pyrogram import Client, filters

# Aapki fixed details
API_ID = 24953130
API_HASH = '30512173bd0a1fdb55f85e46860a9638'
TARGET_CHANNEL = -1003964950414
SOURCE_CHANNEL = 'Avibum'

# Direct chabi se connect karna
STRING_SESSION = "BQF8wSoAiP3lPgPqQIqD4HsT5aPg6Rie_lyuMHmi0KNFjCYwSGR6IPCvBai215an1IwOkwaY5J0juciQludMwGpbHK35DcRgZ1yhPxg5rLf6SffZ8gOsUGLA7D2MLbxCl50gIrEEc-Wuo8dJtRQm8u5yklXz0RC7nY4Ei9MaH_z6bx5R04_EDD7zDt5jYxo-GDoXk1azCdw3s3KSNlrCrtgQpqomTdROdaduuUYH0y-Xjb69tvuHlN8qQ7JMdmqEnNR0mITiGoZTPEMeime91x2qI1GV436PoILaRNj_C09zjMF-TnNRhNHKx3aTmgb5UvI8NnZTjJDayfW6bNpDRW_3-x2yGQAAAAIJT9FaAA"

app_bot = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

@app_bot.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_message(client, message):
    try:
        # Signal aate hi turant copy karega
        await message.copy(TARGET_CHANNEL)
        print("Signal copied successfully!")
    except Exception as e:
        print(f"Forward error: {e}")

if __name__ == '__main__':
    print("Userbot is starting on Pyrogram...")
    app_bot.run()
