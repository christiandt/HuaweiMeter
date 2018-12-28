#!/usr/bin/python

from gigreader import GigReader
import time
import sys

gig_reader = GigReader("192.168.1.1")

try:
    SLEEP_TIME = float(sys.argv[1])
except:
    SLEEP_TIME = 10

while True:
    gig_reader.get_cookie()
    gig_reader.update_usage()
    gig_reader.print_progress()
    time.sleep(SLEEP_TIME)
