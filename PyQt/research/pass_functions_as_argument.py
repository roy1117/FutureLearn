def print_hi(text):
    print('hi')
    print(text)


def print_hello(text):
    print('hello')
    print(text)


# it is said that python functions are the first class object
# so functions can be stored in a variable and can also be passed as argument
# functions are instances of class 'function'
function = print_hi
function('i am newbie..')
print(type(print_hi))
print(type(print_hello))
print(type(function))


# a functions which takes function as argument is called higher-order function
def print_anything(func):
    print(func)


def make_upper_cases(text):
    return text.upper()


def make_lower_cases(text):
    return text.lower()


print_anything(make_upper_cases('What time is it'))
print_anything(make_lower_cases('What time is it'))