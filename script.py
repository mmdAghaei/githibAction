import requests
import os
import py7zr
from balethon import Client
from balethon.conditions import private
import asyncio
bot = Client("1105125913:lDJUbNyc7yMR5TT6ccCGwf_xEyJgLoF73BU")

def download_file(url, dest_folder="."):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    local_filename = os.path.join(dest_folder, url.split('/')[-1].split('?')[0])

    print(f"🚀 در حال دانلود: {local_filename}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("✅ دانلود با موفقیت انجام شد.")
    return local_filename

def create_standard_split_archive(file_path, part_size_mb=15):
    """
    ساخت آرشیو استاندارد (7z) که با پارت‌بندی قابلیت استخراج مستقیم دارد.
    """
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    # اگر حجم فایل از 20 مگ بیشتر بود، پارت‌بندی کن
    if file_size_mb > 20:
        print(f"📦 حجم فایل ({file_size_mb:.2f} MB) زیاد است. در حال ساخت آرشیو پارت‌بندی شده...")

        # نام فایل آرشیو (بدون پسوند فعلی)
        archive_name = file_path + ".7z"

        # تبدیل مگابایت به بایت برای کتابخانه
        part_size_bytes = part_size_mb * 1024 * 1024

        # ایجاد آرشیو با قابلیت Split
        with py7zr.SevenZipFile(archive_name, 'w') as archive:
            archive.write(file_path, os.path.basename(file_path))

        # حالا برای اینکه فایل حتماً پارت شود، از قابلیت split استفاده می‌کنیم
        # اما py7zr در نسخه ساده مستقیماً split نمی‌کند، پس ما از روش استاندارد پایتون 
        # برای تقسیم فایل آرشیو شده استفاده می‌کنیم تا دقیقاً مثل WinRAR شود.

        split_archive_standard(archive_name, part_size_mb)


        # حذف فایل اصلی و فایل آرشیو بزرگ (چون پارت‌ها ساخته شدند)
        os.remove(file_path)
        if os.path.exists(archive_name):
            os.remove(archive_name)

        print(f"✨ عملیات تمام شد! پارت‌ها با پسوند .7z.{i} ساخته شدند.")
    else:
        print("ℹ️ حجم فایل کمتر از 20 مگ است. نیازی به پارت‌بندی نبود.")

def split_archive_standard(archive_path, part_size_mb):
    """تقسیم فایل آرشیو شده به پارت‌های استاندارد"""
    part_size_bytes = part_size_mb * 1024 * 1024
    file_size = os.path.getsize(archive_path)

    with open(archive_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(part_size_bytes)
            if not chunk:
                break

            # ایجاد نام پارت استاندارد: filename.7z.001, filename.7z.002 و غیره
            part_name = f"{archive_path}.{str(part_num).zfill(3)}"
            with open(part_name, 'wb') as p:
                p.write(chunk)

            print(f"   [+] پارت {part_num} ساخته شد: {part_name}")
            part_num += 1







async def list_part_files(folder_path):
    files = os.listdir(folder_path)
    
    part_files = []

    for file in files:
        if '.7z.' in file:
            if '7z' in file:
                part_files.append(file)

    return part_files

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"فایل با موفقیت پاک شد: {file_path}")
    except OSError as e:
        print(f"خطا در پاک کردن فایل {file_path}: {e}")


# @bot.on_initialize()
@bot.on_command(name="down")
async def send():
    await message.reply("pls wait for download")
    try:
        path = download_file(message.reply_to_message.text)
        create_standard_split_archive(path)
    except Exception as e:
        print(f"❌ خطا: {e}")
    await message.reply("Sending...")
    folders = await list_part_files(".")
    for file in folders:
        await bot.send_document("5039303662", f"./{file}", "Hello")
    for file in folders:
        delete_file(os.path.join(".", file))


bot.run()
