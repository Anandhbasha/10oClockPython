import socket

server  = socket.socket()

server.bind(("localhost",4796))

server.listen(1)

print("Server is Waiting... ")

client_socket,addr = server.accept()
print("Connected",addr)

message = client_socket.recv(1024).decode()

print("Client Says:",message)

client_socket.send("message recevied".encode())

client_socket.close()