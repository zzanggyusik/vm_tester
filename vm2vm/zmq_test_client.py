import zmq
import sys, time

port = 5556
    
context = zmq.Context()
print ("Connecting to server...")


ss = context.socket(zmq.REP)
ss.bind("tcp://*:5557")


while True:
    message = ss.recv()
    print ("Received request: ", message)
    if message is not []:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://localhost:%s" % port)
        socket.send_string("World from %s" % port)
        time.sleep(1)
        message = socket.recv()
        print ("Received reply from Main ", "[", message, "]")
        
        ss.send_string("World from %s" % 5557)
