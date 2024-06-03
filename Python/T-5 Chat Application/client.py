import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Same port as used by the server

# Receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{message}")
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to the chat server.")
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    # Start a thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    print("Type your messages below:")

    while True:
        message = input()
        if message.lower() == 'quit':
            client_socket.close()
            break
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            client_socket.close()
            break

if __name__ == "__main__":
    start_client()
