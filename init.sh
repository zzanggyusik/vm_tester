#!/bin/bash

for var in {1..30}
do
    docker rm master client client2
    docker network rm sysai
    start_time=`python3 -c 'import time; print((time.time()))'`
    echo $start_time

    docker network create sysai
    docker run --name master -d --network=sysai master
    docker run --name client -d --network=sysai client
    docker run --name client2 -it --network=sysai client2

    end_time=`python3 -c 'import time; print((time.time()))'`
    echo $end_time

    #time=$(($end_time - $start_time))
    ft=$(echo "scale=16; $end_time - $start_time" | bc)
    #ft=$(($time / 1000))

    echo $ft > $var
done


# docker rm master client client2
# docker network rm sysai
# start_time=`python3 -c 'import time; print((time.time()))'`
# echo $start_time

# docker network create sysai
# docker run --name master -d --network=sysai master
# docker run --name client -d --network=sysai client
# docker run --name client2 -it --network=sysai client2

# end_time=`python3 -c 'import time; print((time.time()))'`
# echo $start_time

# time=$(($end_time-$start_time))

# echo $time > $start_time
