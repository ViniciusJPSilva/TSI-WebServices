import socket

STD_SERVER_IP = "127.0.0.1"
STD_SERVER_PORT = 14000
STD_BUFFER_SIZE = 2048

class Client:
    def __init__(self, server_ip: str = STD_SERVER_IP, 
                 port: int = STD_SERVER_PORT, 
                 buffer_size: int = STD_BUFFER_SIZE):
        self.server_ip = server_ip
        self.port = port
        self.buffer_size = buffer_size
        self.client_socket = None

    def __del__(self):
        self.disconnect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.port))

    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()

    def receive(self) -> str:
        if self.client_socket:
            full_data = b""
            while True:
                data = self.client_socket.recv(self.buffer_size)
                if not data:
                    break
                full_data += data

                if len(data) < self.buffer_size:
                    break
            return full_data.decode()
        return None
    
    def send(self, data: str) -> None:
        self.client_socket.send(data.encode())

# Client
