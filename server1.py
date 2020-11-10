# import socket programming library
import socket
import threading
from unittestdemo import *
# import thread module
from _thread import *
print_lock = threading.Lock()
Compare_list = []
# thread function
def threaded(c):
    while True:
		# data received from client
        data = c.recv(1024)
    if not data:
        print('Bye')
			# lock released on exit
    print_lock.release()
    break
		#checking the brand name or phone name  is present in our data or not
		#print(data.decode("utf-8"))
    for i in range(0, len(your_list)):
        if data.decode("utf-8") in your_list[i]:
            print(your_list[i])
		#print(Compare_list)
		# send back reversed string to client
            c.send(data)
	# connection closed
            c.close()
def main():
    host = ""
	# reverse a port on your computer
	# in our case it is 12345 but it
	# can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
	# put the socket into listening mode
    s.listen(5)
    print("socket is listening")
	# a forever loop until client wants to exit
    while True:
		# establish connection with client
        c, addr = s.accept()
		# lock acquired by client
        print_lock.acquire()
    print('Connected to :', addr[0], ':', addr[1])
		# Start a new thread and return its identifier
    start_new_thread(threaded, (c,))
    s.close()
if __name__ == '__main__':
    main()
