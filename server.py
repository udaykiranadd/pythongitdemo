import socket

s = socket.socket()
print("Socket created")

s.bind(("127.0.0.1", 9999))

s.listen(3)
print("Waiting for connections")

while True:
    conn, addr = s.accept()
    name = conn.recv(1024).decode()
    print("Connected with ", addr, name)

    conn.send(bytes("Welcome to Addepalli","utf-8"))
    conn.close()
