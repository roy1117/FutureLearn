import socket
from threading import Thread
import time


class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.buffer = ''
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8082))
        print("connected")

    def run(self):
        while True:
            self.receive_message()

    def send_message(self):
        message = input("enter some message>>") + '\n'
        message =  message.replace('\\n', '\n')
        data = message.encode()
        self.client_socket.send(data)

    def receive_message(self):
        # recv takes integer which is maximum number of bytes
        # recv takes integer which is maximum number of bytes
        data = self.client_socket.recv(10)
        self.buffer = self.buffer + data.decode()
        terminate_pos = self.buffer.find('\n')
        while terminate_pos > -1:
            message = self.buffer[:terminate_pos]
            self.buffer = self.buffer[terminate_pos+1:]
            print(message)
            terminate_pos = self.buffer.find('\n')

if __name__ == "__main__":
    try:
        my_client = Client()
        my_client.start()
        while True:
            my_client.send_message()
    except:
        try:
            my_client.close()
            print("client closed due to exception")
        except NameError:
            print("client is not even made")



