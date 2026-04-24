from pywebcopy import save_website

save_website(
    url='https://google.com',            # آدرس سایت
    project_folder='saved_site',          # پوشه‌ای که فایل‌ها توش ذخیره می‌شن
    project_name='example_copy',          # اسم پروژه
    bypass_robots=True,                   # نادیده‌گرفتن محدودیت robots.txt
    debug=True,
)
