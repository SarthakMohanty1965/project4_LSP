#  ______________________  ***** Day_1 *****    ______________________

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

client_socket.send("Hello from client!".encode())

data = client_socket.recv(1024).decode()
print("Server says:", data)

client_socket.close()

