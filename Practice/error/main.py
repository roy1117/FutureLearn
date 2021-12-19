# syntax error
# print(3/0))

# zero division exception
# print(3/0)

# custom exception with raise
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# assert
# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."

# try and exception block
import sys
# try:
#     print(3/0)
# except:
#     print('this code dosent crash at least')
#     print('but some function will not work')
#     print('may be you can print some hint')

# try and exception block
# try:
#     print(3 / 0)
# except ZeroDivisionError as e:
#     print('this code dosent crash and outputs exception as well')
#     print(e)
#
# print('the end')

# try and exception block2
# x = 6
# try:
#     if x > 5:
#         raise Exception("not correct number")
# except AssertionError as e:
#     print(e)
#
# print('the end')

# try and exception and else
# try:
#     print(3/0)
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print('division successful')
#
# print('the end')

# try and exception and else and finally
x = 6
try:
    assert (x < 5), 'wrong number'
except AssertionError as e:
    print(e)
else:
    print('division successful')
finally:
    print('life goes on')

print('the end')