# Create a countdown timer that start at a user define number of seconds.

import datetime as dt

import time

start_time = int(input('Please Enter Start Time: '))

count_time = dt.timedelta(seconds=start_time)


while start_time != 0:
    count_time = count_time - dt.timedelta(seconds=1)
    time.sleep(1)
    start_time = start_time - 1
else:
    print("Times\'s up!")