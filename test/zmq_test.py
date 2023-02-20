import zmq
import time
import sys

port = 5556

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

task = []
i = 0

while True:
    #  Wait for next request from client
    start_time = time.time()
    for j in range(1,100):
        message = socket.recv()
        #print ("Received request: ", message)
        #time.sleep (1)  
        socket.send_string("World from %s" % port)
    end_time = time.time()
    task.append(end_time-start_time)
    print(f'{i} task Done = {end_time - start_time}')
    
    i+= 1
    if i == 1000: break
    
total_time = sum(task)
avg_time = total_time/len(task)
print(f'total time = {total_time}\naverage time = {avg_time}')