from telethon.sync import TelegramClient, events
import config
import asyncio
from random import randint
from time import sleep
api_id = config.API_ID
api_hash = config.API_HASH
coroutines = []

async def listen(client):

   @client.on(events.NewMessage(from_users="lntxbot"))
   async def handler(event):
      print(await event.get_sender())
      //sleep(randint(10,100))
      await event.click(1)
   await client.connect()
   await client.run_until_disconnected()

async def main():
   for i in range(config.ACC_NUMBER):
      coroutines.append(listen(TelegramClient('user'+str(i), api_id, api_hash)))
   await asyncio.gather(
        *coroutines
    )
asyncio.run(main())