import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Host: {hostname}")
print(f"IP: {ip_address}")

