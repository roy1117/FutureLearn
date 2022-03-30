# !/bin/python
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

from random import uniform

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 503, no_block=True)

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
        print(str(state))
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")

