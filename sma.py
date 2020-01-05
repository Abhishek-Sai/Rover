import datetime
import time

now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(seconds=10)
print("Current Time =", now)
print("Next Time =", now_plus_10)
while True:
    if datetime.datetime.now() <= now_plus_10:
        c = datetime.datetime.now()
        print(c)
        print("1")
    else:
        now_plus_10 = datetime.datetime.now() + datetime.timedelta(seconds=10)
        c = datetime.datetime.now()
        print(c)
        print("2")
    print("HI")
    time.sleep(5)