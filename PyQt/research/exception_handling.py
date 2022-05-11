# This code has possibility to halt according to parameter
# We don't want to stop the programme, we instead want to get proper parameter again
def divide(number):
    try:
        return number[0]/number[1]
    except ZeroDivisionError:
        print('you passed zero as parameter')
    except IndexError:
        print('check you gave us two numbers')

while True:
    number = map(int(input('give me a number')), int(input('give me a number')))
    print(divide(number))
