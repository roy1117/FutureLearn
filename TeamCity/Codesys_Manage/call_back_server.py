import time
from threading import Thread

class CallbackServer(Thread):
    def __init__(self):
        super().__init__()
        self.call_back_queue = []
        self.daemon = True

    def run(self):
        if self.call_back_queue == []:
            print('queue is in waiting')
            time.sleep(1)
        else:
            callback, arg = self.call_back_queue[0]
            callback(arg)
            self.call_back_queue.remove(callback)
            print('A task completed')
            time.sleep(1)

    def put(self, callback, name):
        self.call_back_queue.append((callback, name))

    def get_hander(self):
        return self

    def print1(self, client):
        time.sleep(1)
        print('{0} : 1'.format(client))

    def print2(self, client):
        time.sleep(2)
        print('{0} : 2'.format(client))

    def print3(self, client):
        time.sleep(3)
        print('{0} : 3'.format(client))



