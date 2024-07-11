import socket

local_IP = '127.0.0.1'
local_port = 13131

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((local_IP,local_port))
server_sock.listen(10)

while True:
    print("Server waiting for connection...")
    while True:
        client_sock,addr = server_sock.accept()
        print("Client connected from",addr)
        input_recv = client_sock.recv(1024)
        if not input_recv or input_recv.decode('utf-8')=='END': 
            break
        print("Input recieved: %s" %input_recv.decode('utf-8'))
        output = input_recv.decode('utf-8').upper()
        client_sock.send(output.encode('utf-8'))
        client_sock.close()
server_sock.close()