# ______________________  ***** Day_2 *****    ______________________
import socket
import os

def list_files():
    files = os.listdir("shared")
    return "\n".join(files)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',8888))
server_socket.listen(1)

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

#data = conn.recv(1024).decode()
#print("Client says:", data)

conn.send("Hello from server!".encode())

conn.close()
server_socket.close()  c 206
