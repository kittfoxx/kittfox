import socket 
import threading


serv = socket.socket(
		socket.AF_INET, 
		socket.SOCK_STREAM
		)

serv.bind((socket.gethostname(), 1455))
serv.listen(3)
print ("Server is listening")

users = []

def send_all(msg):
	for user in users:
		user.send(msg)

def listen_user(user):
	print ('Listening user')
	while True:
		msg = user.recv(1024)
		send_all(msg)
		print (f'User sent {msg}')


def start_serv():
	while True:
		usersocket, address = serv.accept()
		print(f"Connection from {address} has been established!")
		users.append (usersocket)
		
		listen_accepted_user= threading.Thread(target=listen_user, args=(usersocket,))
		listen_accepted_user.start()


if __name__== '__main__':
	start_serv()

