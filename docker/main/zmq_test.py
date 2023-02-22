import zmq
import time
import sys

port = 5556

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
i = 0
while True:
    #  Wait for next request from client
    message = socket.recv()
    #print ("Received request: ", message)
    
    socket.send_string("World from %s" % port)
    i += 1
    print(f'{i} task Done')
    time.sleep (1)  
    if i == 100: break

print(f'python task done\n{time.time()}')
    