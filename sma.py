import datetime
import time


def th():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    # print(str(now))
    # print(str(now)+'output.avi')
    # print("Current Time =", now)
    # print("Next Time =", now_plus_10)
    return now


print(str(th()))