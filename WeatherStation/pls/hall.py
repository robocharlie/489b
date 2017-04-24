#import RPi.GPIO as GPIO


# threaded callback for when mag passes over
# add time.time to list of values
# have time intervals

# a.append(time.time())
# for val in a
# if val < cutoff
# a.remove(val)
from collections import deque
import time

# a = deque([2, 3, 4, 6, 8, 9])
times = deque([])
# while a[0] < 4:
#    a.popleft()

#print(a)

def my_callback(channel):
    times.append(time.time())

# When windspeed is called it checks the current time, removing any entry that
# is not from the past minute. Counting the number of entries and dividing by 60 gives
# the rotations per second (could be multiplied by some constant to calibrate for actual
# windspeed). Secondly it looks at the difference between each entry, finding the smallest
# difference. The inverse of the differnce gives the peak windspeed over this time interval.
def windspeed():
    # set current time
    current_time = time.time()

    # remove entries that are older than a minute
    while times[0] < current_time - 60:
        times.popleft()

        
    for i in len(times):

    return len(times)/60
