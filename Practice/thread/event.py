from threading import Thread, Event
from time import sleep


def wait_forever(e):
    print('wait forever started')
    event_is_set = e.wait()
    print('wait forever detected event set')


def wait_until_timeout(e, t):
    print('wait until timeout started')
    while not e.isSet():
        event_is_set = e.wait(t)
        if event_is_set:
            print('wait forever detected event set')
        else:
            print('timeout happened')


event = Event()
t1 = Thread(target=wait_forever, args=(event,))
t2 = Thread(target=wait_until_timeout, args=(event, 3))
t1.start()
t2.start()
sleep(5)
print('event will be set in main')
event.set()
