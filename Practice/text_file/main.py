import os


FILE_NAME = 'test.txt'
PATH = r'C:\Users\taehy\Desktop\Code\Pycharm\Practice\text_file'
ABS_PATH = os.path.join(PATH, FILE_NAME)

TEST_FILE_NAME = 'hello.txt'
PATH1 = r'C:/'
PATH2 = 'Users'
PATH3 = 'taehy'
TEST_PATH = os.path.join(PATH1, PATH2, PATH3, TEST_FILE_NAME)
print('TEST_PATH : {}'.format(TEST_PATH))
print('ABS_PATH : {}'.format(ABS_PATH))

a = open(ABS_PATH, 'r')
lines = a.readlines()
for i in lines:
    print(i, end="")
a.close()

with open(ABS_PATH, 'r') as a:
    lines = a.readlines()
    for i in lines:
        print(i, end="")

with open(ABS_PATH, 'r') as a:
    for i in range(10):
        lines = a.readline()
        print(lines, end="")
        if lines == "":
            print('true')