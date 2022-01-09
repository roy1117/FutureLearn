import os
print('----------------bytearray------------------------')
a_string = "abc"
print('a_string : {0}'.format(a_string))
a_byte_array = bytearray(a_string, "utf8")
print('a_byte_array : {0}'.format(a_byte_array))
print('a_byte_array type is : {0}'.format(type(a_byte_array)))

byte_list = []
print('print each component of a_byte_array')
for byte in a_byte_array:
    print('value : {0}, type : {1}, binary foramt : {2}'.format(byte, type(byte), bin(byte)))

print('----------------byte------------------------')
print('a_string : {0}'.format(a_string))
a_byte = a_string.encode('ascii')
print('a_byte: {0}'.format(a_byte))
print('a_byte type is : {0}'.format(type(a_byte)))

print('print each component of a_byte')
for byte in a_byte:
    print('value : {0}, type : {1}, binary foramt : {2}'.format(byte, type(byte), bin(byte)))

print('byte is immutable')
try:
    a_byte[0] = 65
except:
    pass
print('byte array is mutable')
try:
    a_byte_array[0] = 65
except:
    pass
print(a_byte)
print(a_byte_array)
