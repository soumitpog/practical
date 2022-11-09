import socket
c = socket.socket()
c.connect(('localhost', 5050))
data = input()
c.send(data.encode())
print(c.recv(1024).decode())
c.close()