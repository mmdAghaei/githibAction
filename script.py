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


import yt_dlp

url = 'https://www.youtube.com/watch?v=OCGGoT23kh4'

# تنظیمات برای دانلود (می‌توانی تنظیمات بیشتری هم اضافه کنی)
ydl_opts = {
    'format': 'best',  # بهترین کیفیت موجود را انتخاب می‌کند
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("دانلود با موفقیت انجام شد! 🎉")
except Exception as e:
    print(f"متأسفانه خطایی رخ داد: {e}")
