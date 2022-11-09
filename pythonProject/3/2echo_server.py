import socket
s = socket.socket()
s.bind(('localhost', 5050))
s.listen(1)
print("socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(c.recv(1024).decode().encode())
    c.close()
    break
