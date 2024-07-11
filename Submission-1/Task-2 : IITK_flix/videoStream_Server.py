import socket,struct,imutils,cv2,pickle

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '127.0.0.1'
port = 12121
socketAdd = (server_ip,port)

server_socket.bind(socketAdd)

server_socket.listen(2)
print("server listening:",socketAdd)

while True:
	client_socket,addr = server_socket.accept()
	print('connected to:',addr)
	if client_socket:
		video = cv2.VideoCapture(0)
		
		while(video.isOpened()):
			img,frame = video.read()
			frame = imutils.resize(frame,width=640)
			message = struct.pack("Q",len(pickle.dumps(frame)))+pickle.dumps(frame)
			client_socket.sendall(message)
			
			cv2.imshow('Input from webcam',frame)
			key1 = cv2.waitKey(1) & 0xFF
			if key1 == ord('q'):
				client_socket.close()