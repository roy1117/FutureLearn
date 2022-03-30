from  pyModbusTCP.client import ModbusClient

client = ModbusClient(host="127.0.0.1", port=503)
client.open()
print(client.read_holding_registers(0, 4))