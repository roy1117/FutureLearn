from threading import *
import time


# creating a function
def thread_1(message):
    while True :
        print(message)
        time.sleep(2)


# creating a thread T
T = Thread(target=thread_1, args = ('Hi',))
T.daemon = True
# starting of thread T
T.start()

# main thread stop execution till 5 sec.
time.sleep(5)
print('main Thread execution')