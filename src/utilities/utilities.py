'''
Created on Jun 21, 2013

@author: jacoberg2
'''
from datetime import datetime
from datetime import time
from datetime import timedelta

def get_time_difference (time1 = datetime.now(), time2 = datetime.now()):
    td = time1 - time2
    return td.total_seconds()

def parse_time_string (str):
    return datetime.strptime(str, '%H:%M:%S')