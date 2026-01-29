import socket
s = socket.socket()

port = 12345
s.connect(("192.168.1.52", port))

print(s.recv(1024).decode())
s.send("Thank you too".encode())

s.close()