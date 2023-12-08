import socket

# Create a socket object
client_socket = socket.socket()

# Connect to the server
client_socket.connect(('172.17.180.136', 9000))

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Send data to the server
client_socket.send(b"Hello, server! This is the client.")

# Close the socket
client_socket.close()
