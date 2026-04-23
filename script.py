import requests

extension_id = "cclelndahbckbenkjhflpdbgdldlbecc"
version = "122.0.6261.111"  # نسخه واقعی کروم یا هر نسخه جدیدی

url = (
    "https://clients2.google.com/service/update2/crx?"
    f"response=redirect&prodversion={version}&x=id%3D{extension_id}%26installsource%3Dondemand%26uc"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.6261.111 Safari/537.36",
}

resp = requests.get(url, headers=headers, allow_redirects=True)

if resp.status_code == 200 and resp.content:
    with open(f"{extension_id}.crx", "wb") as f:
        f.write(resp.content)
    print(f"✅ افزونه با موفقیت دانلود شد: {extension_id}.crx")
else:
    print(f"❌ دانلود ناموفق! کد وضعیت: {resp.status_code} / طول محتوا: {len(resp.content)} بایت")
