import os
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.43.165"
port=7636

client.bind((host,port))
client.listen(2)
print("waiting for connection:")

con,addr=client.accept()
print("connected with:",addr)

while True:
    messg=input("send :")
    con.send(messg.encode())
    client_messg=con.recv(1024)
    print("received :",client_messg.decode())

