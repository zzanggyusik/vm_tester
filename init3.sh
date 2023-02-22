#!/bin/bash

for var in {1..30}
do
    docker rm master client client2 master2 client21 master3
    docker network rm sysai
    start_time=`python3 -c 'import time; print((time.time()))'`
    echo $start_time

    docker run --name master3 -d master3
    docker exec -it master3 python3 zmq_test_client_2.py

    end_time=`python3 -c 'import time; print((time.time()))'`
    echo $end_time

    #time=$(($end_time - $start_time))
    ft=$(echo "scale=16; $end_time - $start_time" | bc)
    #ft=$(($time / 1000))

    echo $ft > $var
done