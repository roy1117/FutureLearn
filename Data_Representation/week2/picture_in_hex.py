def bytes_to_hex_string(bytes):
    raw_string = bytes.hex()
    counter = 0
    total_count = 0
    string = ''
    for i in raw_string:
        total_count += 1
        string = string + i
        counter += 1
        if counter == 2:
            string = string + '/'
            counter = 0
    return string, total_count

filename = 'sample_black_white.bmp'
with open(filename, 'rb') as f:
    content = f.read()
    print(type(content))
    # binary data
    print(type(content[1]))
    string, total_count = bytes_to_hex_string(content)
    print(string)
    print(total_count)

'''
a = b'\x12\x34\x33\xab'  # making bytes object by giving each byte in range from 0 to 255
b = b'123ab'  # covert string (acill) to bytes

print('bytes a : {}'.format(a))
print('bytes b : {}'.format(b))

# convert bytes to hex string
hex_a = a.hex()
hex_b = b.hex()

print('{0} is converted to {1}'.format(a, hex_a))
print('{0} is converted to {1}'.format(b, hex_b))
'''