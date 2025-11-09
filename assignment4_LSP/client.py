
import socket
import os

filename = input("Enter filename to upload: ")
if not os.path.exists(filename):
    print("File not found.")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5002))  


client_socket.send(os.path.basename(filename).encode())
status = client_socket.recv(1024).decode()
if status != "OK":
    print("Server error:", status)
    client_socket.close()
    exit()


with open(filename, "rb") as f:
    while chunk := f.read(1024):
        client_socket.send(chunk)

print(f"File '{filename}' uploaded successfully.")
client_socket.close()
