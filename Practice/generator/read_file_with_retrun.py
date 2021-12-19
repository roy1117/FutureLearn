# import resource
import sys
from memory_profiler import profile

FILE_NAME = 'greeting.txt'
@profile
def read_file(file_name):
    text_file = open(file_name, 'r')
    line_list = text_file.readlines()
    text_file.close()
    return line_list

for i in sys.argv:
    print(i)

file_lines = read_file(sys.argv[1])

print(type(file_lines))
print(len(file_lines))

for line in file_lines:
    print(line, end="")

# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)

