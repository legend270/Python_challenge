#Day 15 of the 90 days python challenge. 


import socket
import threading

def handle_client(connection, client_address):
    try:
        print(f"Connection from {client_address}")
        
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            connection.sendall(b"Message received")
            
    finally:
        connection.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server listening on {server_address[0]}:{server_address[1]}")
    
    while True:
        connection, client_address = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client,
            args=(connection, client_address)
        client_thread.start()

if __name__ == "__main__":
    start_server()