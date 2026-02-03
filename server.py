import socket

s = socket.socket()
print("Socket succesfully created")

port = 12345

s.bind(('', port))
print(f"socket binded to {port}")

s.listen(5)
print("socket is listening")

while True:
    
    c, addr = s.accept()
    print("Got connection from", addr)
    
    c.send('Thank you for connecting'.encode())
    print(c.recv(1024).decode())
    
    c.close()
    
