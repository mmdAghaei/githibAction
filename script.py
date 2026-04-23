# from aiobale import Client, Dispatcher
# import asyncio
# from aiobale.enums import ChatType

# async def send_personal_message():
#     dp = Dispatcher()
#     client = Client(dp,session_file="session")
#     async def open_gift_handler():
#         try:
#             await client.send_message(text=f"github action is running...", chat_id="4402961702", chat_type=ChatType.GROUP)

#             print("seccus")
#         except Exception as e:
#             print(f"Error {e}")
#     await open_gift_handler()

# asyncio.run(send_personal_message())

from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=OCGGoT23kh4').streams.first().download()
