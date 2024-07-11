import socket
local_IP_address = '127.0.0.1'
local_Port = 12121

server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_sock.bind((local_IP_address,local_Port))
print("UDP Server ready to receive...")


while True:
    data,addr = server_sock.recvfrom(4096)
    message = data.decode('utf-8').upper()
    server_sock.sendto(message.encode('utf-8'),addr)