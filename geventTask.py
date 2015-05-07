__author__ = 'nimish'

#!/usr/bin/env python

# import modules used here
import sys
import gevent
import random
from datetime import datetime

def timeCollector1():
    print('time 1')
    gevent.sleep(random.randint(1,10))
    print('time 1 again')
    t1 = datetime.now()
    t1 = str(t1.strftime("%H:%M:%S.%f"))
    return t1

def timeCollector2():
    print('time 2')
    gevent.sleep(random.randint(1,10))
    print('time 2 again')
    t2 = datetime.now()
    t2 = str(t2.strftime("%H:%M:%S.%f"))
    return t2

def timeCollector3():
    print('time 3')
    gevent.sleep(random.randint(1,10))
    print('time 3 again')
    t3 = datetime.now()
    t3 = str(t3.strftime("%H:%M:%S.%f"))
    return t3

# Gather our code in a main() function
def main():

	print "spawning 3 time collectors"
	time1 = gevent.spawn(timeCollector1)
	time2 = gevent.spawn(timeCollector2)
	time3 = gevent.spawn(timeCollector3)
	gevent.joinall([time1,time2,time3,])
	timeList = []
	timeList.append(time1.value) 
	timeList.append(time2.value)
	timeList.append(time3.value)
	print timeList
	print 'end of main function'

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()