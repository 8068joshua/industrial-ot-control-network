from pymodbus.client import ModbusTcpClient

HOST = "127.0.0.1"
PORT = 502
ADDRESS = 0       # %QW0
DEVICE_ID = 1

client = ModbusTcpClient(HOST, port=PORT)

if not client.connect():
    print("Connection failed")
    raise SystemExit

result = client.read_holding_registers(
    address=ADDRESS,
    count=1,
    device_id=DEVICE_ID
)

if result.isError():
    print("READ ERROR:", result)
else:
    value = result.registers[0]

    print("READ SUCCESS")
    print("Address :", ADDRESS)
    print("Value   :", value)

client.close()