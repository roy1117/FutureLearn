import struct

# Defining binary data
birary_data = b'\x00\x02\x00\x01'
python_variable = struct.unpack('>HH', birary_data)
# we get unpacked data as tuple containing python variables
print(python_variable)
print(type(python_variable))
print(type(python_variable[0]))

# To get variables directly from the tuple, we can use this kind of syntax
(first_variable, second_variable) = struct.unpack('>HH', birary_data)
print(first_variable, second_variable)
