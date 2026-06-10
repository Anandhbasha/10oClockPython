import socket

client = socket.socket()
client.connect(("localhost",4796))

client.send("Hello Server".encode())

message = client.recv(1024).decode()
print("server says:",message)
client.close()