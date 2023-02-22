#!/bin/bash

start_time=`date +%s`
echo $start_time
docker run --name master -it --network=sysai zzanggyusik/master:1.0
docker run --name client -it --network=sysai zzanggyusik/client:1.0
docker run --name client2 -it --network=sysai zzanggyusik/client_2:1.0
end_time=`date +%s`
echo "task time = $(($end_time - $star_time))"