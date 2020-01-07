# Python program to illustrate the concept 
# of threading 
import threading
import os
import datetime


def task1():
    now = datetime.datetime.now()
    print("Current Time =", now)


def task2():
    now_plus_10 = datetime.datetime.now() + datetime.timedelta(seconds=10)
    print(now_plus_10)



if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
