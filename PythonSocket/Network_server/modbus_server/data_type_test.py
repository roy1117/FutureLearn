f = open("test.txt", "wb")
message = "hello, world"
message = message.encode()
f.write(message)
print(message)
f.close()