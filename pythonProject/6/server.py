# Create a socket (UDP)
# Write a program to implement simple client-server application using UDP

import socket

host = "127.0.0.1"
port = 4455

""" Creating the UDP socket """
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

""" Bind the host address with the port """
server.bind((host, port))

while True:
    data, addr = server.recvfrom(1024)
    data = data.decode("utf-8")
    print(data)

    if data == "!EXIT":
        print("Client disconnected.")
        break

    print(f"Client: {data}")

    data = data.upper()
    data = data.encode("utf-8")
    server.sendto(data, addr)
