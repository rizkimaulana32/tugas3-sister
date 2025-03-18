import socket

HOST = '192.168.1.16'
PORT = 4030

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    header = conn.recv(1024).decode()
    filename, file_size = header.split("|")
    file_size = int(file_size)

    print(f"Receiving file: {filename}, Size: {file_size} bytes")

    received_size = 0
    with open(f"received_{filename}", "wb") as f:
        while received_size < file_size:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
            received_size += len(data)

    print(f"File {filename} received successfully.")

    conn.sendall(b"File received successfully")

    conn.close()
