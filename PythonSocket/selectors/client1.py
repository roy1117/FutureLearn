import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
userInput = input('press a to connect')
if userInput == 'a':
    client.connect(('127.0.0.1', 9999))
print('connected successfully')
userInput = input('enter message to send')
while userInput != 'break':
    message = userInput
    client.send(message.encode())
    userInput = input('enter message to send')