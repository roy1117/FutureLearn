from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from threading import Thread


def run_modbus_server(server):
    try:
        print("Start server...")
        server.start()
        print("Server is online")
        state = [0]
        count = 1
        while True:
            count = count + 1
            if count == 100:
                count = 1
            DataBank.set_words(0, [count, 2, 3, 4, 5])
            state = DataBank.get_words(0, 10)
            # print(str(state))
            sleep(0.5)

    except:
        print("Shutdown server ...")
        server.stop()
        print("Server is offline")


server = ModbusServer("127.0.0.1", 503, no_block=True)
t1 = Thread(target=run_modbus_server, args=(server,))
t1.start()

shutdown = input('type a to shutdown')
if shutdown is 'a':
    server.stop()

close = input('type a to close')
if close is 'a':
    pass


