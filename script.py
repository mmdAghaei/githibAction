import requests

url = "https://jitsi.pashmak.net/"

payload = b'a' * (1024 * 1024)  # 1MB

headers = {
    "Content-Type": "application/octet-stream"
}

print("hello")

# for i in range(1000):
#     r1 = requests.post(url, data=payload, headers=headers)
#     print("Request 1:", r1.status_code)
    
