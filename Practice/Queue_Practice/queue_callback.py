import queue

queue = queue.Queue()

def function1(name):
    def function1_callback():
        print("function1 : {0}".format(name))
    queue.put(function1_callback)


function1("Roy")
item = queue.get()
item()