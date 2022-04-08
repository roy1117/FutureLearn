import socket
import time

'''This is to demonstrate that a receiver dosen't have any info of how long a message length is
It just reads specific amount of message from the buffer'''
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", 8000))
message1 = "Hellow, world"
message1 = message1.encode()
message2 = "Hope you can find"
message2 = message2.encode()

socket.send(message1)
socket.send(message2)
print("I sent all")

