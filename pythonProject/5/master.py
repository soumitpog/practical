# Remote Command Execution
# Write a program to implement Remote Command Execution (RCE).

import socket

master = socket.socket()
host = "localhost"
port = 1243
master.bind((host, port))
master.listen(1)
slave, address = master.accept()
while True:
    print(">", end=" ")
    command = input()
    slave.send(command.encode())

    if command == "exit":
        break

    output = slave.recv(5000)
    print(output.decode())

master.close()