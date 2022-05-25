from time import sleep
import threading


class Counter(threading.Thread):
    def __init__(self, identifier, counter):
        super().__init__()
        self.identifier = identifier
        self.counter = counter

    def run(self):
        for i in range(self.counter):
            print('identifier : {0}, count : {1}'.format(self.identifier, i))
            print(threading.current_thread())
            sleep(1)

t1 = Counter('t1', 3)
t2 = Counter('t2', 5)
t1.start()
t2.start()
print(threading.current_thread())