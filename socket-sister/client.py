import socket
import time
import os

SERVER_IP = '127.0.0.1'
PORT = 12345

def send_file(filename):
    file_size = os.path.getsize(filename)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))

    header = f"{filename}|{file_size}"
    client_socket.sendall(header.encode())

    time.sleep(0.1)  

    start_time = time.time()
    with open(filename, "rb") as f:
        while (chunk := f.read(4096)):
            client_socket.sendall(chunk)
    
    confirmation = client_socket.recv(1024).decode()
    end_time = time.time()

    print(f"File {filename} sent successfully in {end_time - start_time:.4f} seconds")
    print(f"Server confirmation: {confirmation}\n")

    client_socket.close()

# Kirim berbagai ukuran file teks dan catat waktu pengiriman
for size in [1, 10, 100, 1024]:  # KB
    filename = f"test_{size}KB.txt"
    with open(filename, "wb") as f:
        f.write(b"A" * size * 1024)  # Isi file dengan huruf 'A'

    send_file(filename)
    
send_file("video1949257301.mp4")
