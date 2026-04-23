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

import requests

# آیدی افزونه
extension_id = "cclelndahbckbenkjhflpdbgdldlbecc"

# لینک رسمی دانلود فایل CRX از سرور گوگل
url = f"https://clients2.google.com/service/update2/crx?response=redirect&prodversion=114.0.5735.199&x=id%3D{extension_id}%26installsource%3Dondemand%26uc"

# مسیر ذخیره فایل روی سیستم
output_file = f"{extension_id}.crx"

# دانلود فایل
resp = requests.get(url, allow_redirects=True)

if resp.status_code == 200:
    with open(output_file, "wb") as f:
        f.write(resp.content)
    print(f"✅ اکستنشن با موفقیت دانلود شد: {output_file}")
else:
    print(f"❌ خطا در دانلود (کد وضعیت: {resp.status_code})")
