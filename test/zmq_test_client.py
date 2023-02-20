import zmq
import sys

port = 5556
    
context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://main_container:%s" % port)

i = 0
while True:
#  Do 10 requests, waiting each time for a response
    for request in range (1,10):
        #print ("Sending request ", request,"...")
        socket.send_string ("Hello")
        #  Get the reply.
        message = socket.recv()
        #print ("Received reply ", request, "[", message, "]")
    i += 1
    
    print(f'{i} task done')
    if i == 1000 : break