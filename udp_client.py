#!/usr/bin/python3
import socket

target_host = "127.0.0.1"
target_port = 500

#Create the socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send data
client.sendto(b"AAABBBCCC",(target_host,target_port))

#Receive Data
data, addr = client.recvfrom(4096)

#Print Data
print(data.decode())
client.close