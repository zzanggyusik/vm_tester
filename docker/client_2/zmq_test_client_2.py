import zmq
import sys, time

port = 5557
    
context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
#socket.connect ("tcp://client:%s" % port)
socket.connect ("tcp://localhost:%s" % port)

#  Do 10 requests, waiting each time for a response
for request in range (1,100):
    print ("Sending request ", request,"...")
    socket.send_string ("Hello")
    #  Get the reply.
    message = socket.recv()
    print ("Received reply ", request, "[", message, "]")
   
    print(f'{request} Send')
    time.sleep(1)
print(f'python task done\n{time.time()}')