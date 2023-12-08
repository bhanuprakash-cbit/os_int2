import socket

# Create a socket object
server_socket = socket.socket()

# Bind the socket to a specific address and port
server_socket.bind(('0.0.0.0', 9000))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening for connections...")

try:
    # Your code or process that you want to run
    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Send data to the client
        client_socket.send(b"Hello, client! This is the server.")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received from client: {data.decode()}")
        
except KeyboardInterrupt:
    print("\nKeyboard interrupt received. Ending the process.")
    
finally:
    client_socket.close()
    server_socket.close()
