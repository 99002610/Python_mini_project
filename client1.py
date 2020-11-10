"""Import socket module"""
import socket
def main():
	# local host IP '127.0.0.1'
    host = '127.0.0.1'
    print(host.__doc__)
	# Define the port on which you want to connect
    port = 12345
    print(port.__doc__)
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# connect to server on local computer
    _s.connect((host, port))
    print(_s.__doc__)
    print(_s.connect.__doc__)
    print(socket.socket.__doc__)
    while True:
		# message you send to server
        message = input()
        print(message.__doc__)
		# message sent to server
        _s.send(message.encode('ascii'))
        print(_s.send.__doc__)
		# messaga received from server
        data = _s.recv(1024)
        print(data.__doc__)
		# print the received message
		# here it would be a reverse of sent message
        print('Received from the server :', str(data.decode('ascii')))
		# ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        print(ans.__doc__)
        if ans == 'y':
            continue
	# close the connection
    _s.close()
    print(_s.close.__doc__)
print(main.__doc__)
if __name__ == '__main__':
    main()
