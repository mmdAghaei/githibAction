import requests

url = "https://jitsi.pashmak.net/"

payload = b'a' * (1024 * 1024)  # 1MB

headers = {
    "Content-Type": "application/octet-stream"
}

# ارسال درخواست اول
r1 = requests.post(url, data=payload, headers=headers)
print("Request 1:", r1.status_code)

# ارسال درخواست دوم
r2 = requests.post(url, data=payload, headers=headers)
print("Request 2:", r2.status_code)
