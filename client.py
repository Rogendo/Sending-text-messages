import socket



server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host="105.165.63.122"
port=7636

server.connect((host,port))
print("waiting for messages..")

while True:
    server_messg=server.recv(1024)

    print("received:",server_messg.decode())

    client_messg=input("sent:")
    server.send(client_messg.encode())
