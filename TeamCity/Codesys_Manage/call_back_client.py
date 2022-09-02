from call_back_server import CallbackServer

class CallbackClient:
    def __init__(self, name, server):
        self.name = name
        self.server = server

    def print1(self):
        self.server.put(self.print1, self.name)

    def print2(self):
        self.server.put(self.print2, self.name)

    def print3(self):
        self.server.put(self.print3, self.name)


if __name__ == '__main__':
    call_back_server = CallbackServer()
    call_back_server.start()
    print('hello')

    first_call_back_client = CallbackClient('First Client', call_back_server)
    second_call_back_client = CallbackClient('Second Client', call_back_server)
    first_call_back_client.print1()
    second_call_back_client.print1()
    first_call_back_client.print2()
    second_call_back_client.print1()
    first_call_back_client.print3()
    second_call_back_client.print1()
