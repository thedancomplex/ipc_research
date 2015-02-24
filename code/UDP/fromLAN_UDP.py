import socket

REC_IP = "192.168.1.245"
#REC_IP = "127.0.0.1"
SEND_IP = "127.0.0.1"
REC_PORT = 5005
SEND_PORT = 5006

receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from process over lan
send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP to 2nd internal process

receive.bind((REC_IP, REC_PORT))

while True:
	data, addr = receive.recvfrom(1024) # buffer size is 1024 bytes
	send.sendto(data, (SEND_IP, SEND_PORT))
	print data




