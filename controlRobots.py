import urllib3
import time

http = urllib3.PoolManager()

robotBlue = '192.168.0.22'
robotYellow = '192.168.0.23'
robotGreen = '192.168.0.18'




def forward(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=70&right=100')

def backward(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=110&right=80')

def stop(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=90&right=90')


i = 0

while (i < 10) :

    i+=1
    forward(robotBlue)
    forward(robotYellow)
    forward(robotGreen)
    time.sleep(1)
    stop(robotBlue);
    stop(robotYellow);
    stop(robotGreen);
    time.sleep(1)
    backward(robotBlue)
    backward(robotYellow)
    backward(robotGreen)
    time.sleep(1)
    stop(robotBlue);
    stop(robotYellow);
    stop(robotGreen);
    time.sleep(1)

