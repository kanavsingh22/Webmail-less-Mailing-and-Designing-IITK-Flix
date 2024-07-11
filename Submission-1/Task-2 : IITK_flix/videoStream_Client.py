import socket,struct,cv2,pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '127.0.0.1' 
port = 12121
serverAdd = (server_ip,port)
client_socket.connect(serverAdd) 
inp = b""
payloadSize = struct.calcsize("Q")
while True:
	while len(inp) < payloadSize:
		packet = client_socket.recv(4096) 
		if not packet:
			break
		inp+=packet
	packedMessageSize = inp[:payloadSize]
	inp = inp[payloadSize:]
	messageSize = struct.unpack("Q",packedMessageSize)[0]
	
	while len(inp) < messageSize:
		inp += client_socket.recv(4096)
	frame_data = inp[:messageSize]
	inp = inp[messageSize:] 
	cv2.imshow("Video Stream",pickle.loads(frame_data))
	key = cv2.waitKey(1) & 0xFF
	if key  == ord('q'):
		break
client_socket.close()