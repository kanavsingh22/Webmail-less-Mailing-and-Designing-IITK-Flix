import socket

server_IP = '127.0.0.1'
server_port = 13131

user_inp = input('enter the line:')
encoded_inp = user_inp.encode('utf-8')

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server_IP,server_port))

client_sock.send(encoded_inp)
output_recv = client_sock.recv(1024)
print("Received output from server:")
print(output_recv.decode('utf-8'))

client_sock.close()