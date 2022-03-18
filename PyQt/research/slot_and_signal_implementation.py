from inspect import signature


class Mysignal:
    def __init__(self):
        self.slots = {}

    def connect(self, func):
        sig = signature(func)
        number_of_arguments = len(sig.parameters.values())
        self.slots[func] = number_of_arguments

    def emit(self, *args):
        for item in self.slots.items():
            number_of_arguments = item[1]
            cust_args = []
            for i in range(number_of_arguments):
                cust_args.append(args[i])
            item[0](*cust_args)


def print_something(text1):
    print(text1)

def sumation(number1, number2):
    print(number1 + number2)


signal = Mysignal()
signal.connect(print_something)
signal.connect(sumation)
signal.emit(123, 456)