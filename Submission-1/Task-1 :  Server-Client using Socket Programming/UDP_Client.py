import socket

inp_user = input('enter the line:')
encoded_inp = str.encode(inp_user)

server_IP = '127.0.0.1'
server_Port = 12121

server_addr_port = (server_IP,server_Port)

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client_sock.sendto(encoded_inp,server_addr_port)   

data,addr = client_sock.recvfrom(4096)             
print("Output received from server:")
print(str(data))
client_sock.close()