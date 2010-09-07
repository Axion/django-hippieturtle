import time

PRETEST_SLEEP = 2
AFTERTEST_SLEEP = 2

def start():
    global start_time
    #print "msg:pre test sleep"
    open('turtle_test_pipe', 'r+').write('msg:pre test sleep\n')
    time.sleep(PRETEST_SLEEP)
    #print "msg:testing"
    open('turtle_test_pipe', 'r+').write('msg:testing\n')
    start_time = time.time()

def stop():
    global start_time
    #print "time:",
    open('turtle_test_pipe', 'r+').write('time:%s\n' %  (time.time() - start_time))
    #print "msg:sleeping"
    open('turtle_test_pipe', 'r+').write('msg:sleeping\n')
    time.sleep(AFTERTEST_SLEEP)
    open('turtle_test_pipe', 'r+').write('msg:stop\n')
    #print "msg:stop"



INSERT_ITERATIONS = 20000
SELECT_ITERATIONS = 50000
SELECTS_ITERATIONS = 1000
SUB_SELECT_ITERATIONS = 400
