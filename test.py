from telethon.sync import TelegramClient, events
import config
api_id = config.API_ID
api_hash = config.API_HASH

with TelegramClient('name', api_id, api_hash) as client:

   @client.on(events.NewMessage(from_users="lntxbot"))
   async def handler(event):
      print(await event.get_sender())
      await event.click(1)

   client.run_until_disconnected()