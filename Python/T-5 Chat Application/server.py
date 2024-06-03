import socket
import threading

# Server configuration
HOST = '127.0.0.1'  #Localhost
PORT = 65432        #Arbitrary non-privileged port

# List to keep track of connected clients
clients = []

# Broadcast message to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                client.close()
                clients.remove(client)

# Handle client connection
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received message: {message.decode()}")
                broadcast(message, client_socket)
            else:
                client_socket.close()
                clients.remove(client_socket)
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            clients.remove(client_socket)
            break

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server started on {HOST}:{PORT}")
    except Exception as e:
        print(f"Server started on {HOST}:{PORT}")
        return
    
    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"New connection from {client_address}")
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
        except Exception as e:
            print(f"Error accepting new connection: {e}")

if __name__ == "__main__":
    start_server()
