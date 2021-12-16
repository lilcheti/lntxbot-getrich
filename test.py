from telethon.sync import TelegramClient, events
import config
api_id = config.API_ID
api_hash = config.API_HASH
coroutines = []

import asyncio

async def listen(client):
   await client.connect()
   await client.run_until_disconnected()
   @client.on(events.NewMessage(from_users="lntxbot"))
   async def handler(event):
      print(await event.get_sender())
      await event.click(1)
   

async def main():
   for i in range(config.ACC_NUMBER):
      coroutines.append(listen(TelegramClient('user'+str(i), api_id, api_hash)))
   await asyncio.gather(
        *coroutines
    )
asyncio.run(main())