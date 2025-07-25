import socket
import time
import sys

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        time.sleep(1)
        client_socket.sendall(f"Hello from server on port {port}!".encode())
        client_socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python backend_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)