import zmq
import sys, time

port = 5556
    
context = zmq.Context()
print ("Connecting to server...")


ss = context.socket(zmq.REP)
ss.bind("tcp://*:5557")
i = 0

while True:
    message = ss.recv()
    #print ("Received request: ", message)
    if message is not []:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        #socket.connect ("tcp://master:%s" % port)
        socket.connect ("tcp://localhost:%s" % port)
        socket.send_string("World from %s" % port)
        
        message = socket.recv()
        #print ("Received reply from Main ", "[", message, "]")
        
        ss.send_string("World from %s" % 5557)
        i += 1
        print(f'{i} task Done')
        time.sleep(1)
        if i == 100: break
print(f'python task done\n{time.time()}')