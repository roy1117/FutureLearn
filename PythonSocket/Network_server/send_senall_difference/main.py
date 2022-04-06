import socket
from threading import Thread
import time


class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.buffer = ''
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8082))
        self.message = None
        print("connected")

    def run(self):
        while True:
            message = '1'
            for i in range(10):
                message = message + message
            message = message + '\n'
            message = message.replace('\\n', '\n')
            print(message)
            while True:
                length = self.send_data(message)
                print(length)
                time.sleep(0.1)
                if length is not len(message):
                    break
        print('Prgramme stop')

    def send_data(self, message):
        result = self.client_socket.send(message.encode())
        return result


try:
    client = Client()
    client.start()
except:
    client.close()