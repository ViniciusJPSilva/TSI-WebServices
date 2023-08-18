import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 14000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_IP, SERVER_PORT))

    fullData = []
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        fullData.append(data)

    print(fullData[-1].decode())