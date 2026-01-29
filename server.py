import socket

s = socket.socket()

port = 12345

s.bind("", port)
s.listen(5)

while True:
    
    c, addr = s.accep()
    c.send("Thank you for connecting from", addr)
    c.send("Thank you for connecting".encode())
    
    c.close()
    break
