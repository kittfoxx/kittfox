import socket 
import threading

client = socket.socket(
		socket.AF_INET, 
		socket.SOCK_STREAM
		)

client.connect((socket.gethostname(), 1455))

def listen_server():
	while True:
		msg = client.recv(1024)
		print (msg.decode('utf-8'))


def client_start ():

	listen_thread = threading.Thread(target = listen_server)
	listen_thread.start()

	while True:
		client.send(
			input('type:').encode('utf-8')
				)

if __name__=='__main__':
	client_start()