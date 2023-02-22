#!/bin/bash

start_time=`date +%s`
echo docker run a
echo docker run b
echo docker run c
end_time=`date +%s`
time=($start_time-$end_time)
echo $time
