from PIL import Image
import pickle
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
image = Image.open("/Users/choetaehyeon/Desktop/screen_shot/image.png")
SERVER_ADDRESS = ('0.0.0.0', 20001)
width, height = image.size
print(width, height)
counter = 0
lost_data = 0
sent_data = 0
for y in range(int(height/10)):
    for x in range(width):
        counter += 1
        if counter == 9:
            counter = 0
            lost_data += 1
            continue
        pos = (x, y)
        rgba = image.getpixel(pos)
        message = (pos, rgba)
        message = pickle.dumps(message)
        client_socket.sendto(message, SERVER_ADDRESS)
        time.sleep(0.0001)
        sent_data += 1

print('lost data : {0}'.format(lost_data))
print('sent data : {0}'.format(sent_data))