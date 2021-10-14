from PIL import Image
import pickle
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# image = Image.open("/Users/choetaehyeon/Desktop/screen_shot/image.png")
SERVER_ADDRESS = ('0.0.0.0', 20001)
# width, height = image.size
# print(width, height)
pos = (3, 8)
rgba = (255, 255, 255 ,255)
message = (pos, rgba)
message = pickle.dumps(message)
client_socket.sendto(message, SERVER_ADDRESS)
# for y in range(int(height/10)):
#     for x in range(width):
#         pos = (x, y)
#         rgba = image.getpixel(pos)
#         message = (pos, rgba)
#         message = pickle.dumps(message)
#         client_socket.sendto(message, SERVER_ADDRESS)

