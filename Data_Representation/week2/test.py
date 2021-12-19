text = 'fff000fff'

list = []
for i in range(0, len(text), 3):
    print(i)
    r, g, b = text[i:i+3]
    r = int(r, 16)
    print(r, g, b)
    tuple = (r, g, b)
    list.append(tuple)
print(list)

bytes = bytes([255, 17])
hex = bytes.hex()
print(hex)
print(bytes)
for i in bytes:
    print(i)

pixel_data = []

pixel_data.insert(0, [1, 2, 3])
pixel_data.insert(1, [4, 5, 6])
print(pixel_data)

a = 'f'
a = int(a, 16)
print(a)

a = 'smile_image.bmp'
print(a.split('.')[0])

text = '424d'
reconstruct1 = bytearray()

reconstruct2 = bytearray.fromhex(text[0:4])
reconstruct1.append(17)
reconstruct = reconstruct1 + reconstruct2
print(reconstruct.hex())
print(reconstruct)

number = 166
print(number.to_bytes(4, 'little'))
print(type(number.to_bytes(4, 'little')))
print(reconstruct + number.to_bytes(4, 'little'))