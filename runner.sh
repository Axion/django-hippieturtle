#!/bin/bash
$1 > turtle_test_pipe &
PID=$!

while [ 1 ]; do
    sleep $2;
    MEM=`ps -eo pid,pcpu,rss|grep -i $PID|awk '{print $3}'`;
    if [ "$MEM" == "" ]; then
        break
    fi
    echo "mem:$MEM";
done
