# import resource
import sys
from memory_profiler import profile

FILE_NAME = 'greeting.txt'

class read_file():
    def __init__(self, file_name):
        self.file = open(file_name, 'r')

    @profile
    def read(self):
        while True:
            line_list = self.file.readline()
            if line_list != "":
                yield line_list
            else:
                break

for i in sys.argv:
    print(i)

file = read_file(sys.argv[1])
file_lines = file.read()

for line in file_lines:
    print(line, end="")

# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)

