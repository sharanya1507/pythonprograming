import time
second = 0
minute = 0

while True:
    print( minute, ":", second)
    time.sleep(1)
    second += 1
    if second == 61:
        second = 0
        minute += 1

