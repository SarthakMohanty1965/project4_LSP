import socket
import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def receive_file(conn, filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print(f"Received file: {filename}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5002))  
server_socket.listen(1)
print("Server ready to receive uploads...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")


filename = conn.recv(1024).decode()
conn.send("OK".encode())  # Acknowledgeing


receive_file(conn, filename)

conn.close()
server_socket.close()
