import socket
server = socket.socket()
server.bind(("",5000))
server.listen()
connection,address = server.accept()
print(f"New connection from : {address}")

while True:
    recieved = connection.recv(1024).decode()
    print(f"client : {recieved}")
    message = input(">>>")
    connection.send(message.encode())