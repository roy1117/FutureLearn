queue = []


def function_1(index):
    def function_1_call_back():
        print('1:'.format(index))
    queue.append(function_1_call_back)


def function_2(index):
    def function_2_call_back():
        print('2:'.format(index))
    queue.append(function_2_call_back)


def function_3(index):
    def function_3_call_back():
        print('3:'.format(index))
    queue.append(function_3_call_back)


function_1(1)
function_2(2)
function_3(3)

for item in queue:
    item()