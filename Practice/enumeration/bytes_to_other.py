# bytes is encoded data
var_bytes = b'abcde'
print(type(var_bytes))
for i in var_bytes:
    print(i)
    print(bin(i))

var_str = 'abcde'
str_to_bytes = var_str.encode('ascii')
print(type(str_to_bytes))
print(str_to_bytes)
print(var_bytes == str_to_bytes)

