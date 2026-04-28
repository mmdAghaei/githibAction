import requests
import time

url = "https://jitsi.pashmak.net"
payload = b'a' * (1024 * 1024)

def send_packet(n):
    start = time.time()
    r = requests.post(url, data=payload)
    end = time.time()
    print(f"Packet {n} | Status: {r.status_code} | RTT: {(end - start)*1000:.2f} ms")

for i in range(10):
    send_packet(i)
