import threading 
import socket

host_ip=input('host ip:')
host_port=input('host port number:')
app_ip=input('mobile ip:')
app_port=input('mobile port number:')

server_sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind((host_ip,int(host_port)))

mobileAddr = (app_ip,int(app_port))

def receiveData():
    while True:
        data =server_sock.recv(1024)
        string =data.decode()
        print("\nMobile User:{}".format(string))
        
        
def sendData():
    while True:
        string=input('\nServer:')
        server_sock.sendto(bytes(string,'utf-8'),mobileAddr)
        
thread_rec =threading.Thread(target=receiveData)
thread_send =threading.Thread(target=sendData)
print("Wait for connection from mobile user...")
print("Connected successfully...")
thread_rec.start()
thread_send.start()