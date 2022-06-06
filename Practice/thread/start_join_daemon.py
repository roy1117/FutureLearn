import threading
from time import sleep


def print_hi(identifier, count):
    for i in range(count):
        print('identifier : {0}, count : {1}'.format(identifier, i))
        print(threading.current_thread())
        sleep(1)

# Create threads and pass arguments
t1 = threading.Thread(target=print_hi, args=('t1', 3))
t2 = threading.Thread(target=print_hi, args=('t2', 5))
# Setting daemon flags
# daemon threads exist only as long as there is main threads
# daemon thread has a possibility to terminate abruptly
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
# .join() method blocks main thread until the target thread ends
t1.join()
print(threading.current_thread())
sleep(10)


