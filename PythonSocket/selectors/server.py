import selectors
import socket
import time
sel = selectors.DefaultSelector()


def accept_wrapper(key, mask):
    conn, _ = key.fileobj.accept()
    print('a client is accepted')
    data = ' '
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, service_connection)


def service_connection(key, mask):
    message = key.fileobj.recv(1024)
    message = message.decode()
    print('message : {0}'.format(message))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
print('a server opened')
server.listen()
sel.register(server, selectors.EVENT_READ, data=accept_wrapper)
server.setblocking(False)
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        callback = key.data
        callback(key, mask)

