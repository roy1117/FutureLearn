import queue

queue = queue.Queue()
# Number of items allowed in the queue
queue.maxsize = 3


def function_1(index=None):
    print('function_1:'.format(index))


def function_2(index=None):
    print('function_2:'.format(index))


def function_3(index=None):
    print('function_3:'.format(index))


queue.put(function_1)
queue.put(function_2)
queue.put(function_3)
# # If no free slot is immediately available, raise QueueFull.
# queue.put(function_1)
try:
    queue.put_nowait(function_1)
except Exception as e:
    print("Exception occurred. {0}".format(e))

while not queue.empty():
    print('the number of items remained : {0}'.format(queue.qsize()))
    try:
        item = queue.get_nowait()
    except Exception as e:
        print(e)
    # # If queue is empty, wait until an item is available.
    # item = queue.get()
    item()

# Return True if the queue is empty, False otherwise.
print(queue.empty())
print('The end')