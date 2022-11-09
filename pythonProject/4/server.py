# File transfer
# Write a program to Perform File Transfer in Client & Server Using TCP/IP

import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

print("[STARTING] server is staring")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[LISTENING] server is listning")

while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "w")
    conn.send("Filename received.".encode(FORMAT))
    data = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    conn.send("File data received".encode(FORMAT))
    file.close()
    conn.close()
