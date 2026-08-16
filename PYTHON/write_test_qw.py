from pymodbus.client import ModbusTcpClient

HOST = "127.0.0.1"
PORT = 502
ADDRESS = 0       # %QW0
VALUE = 1234
DEVICE_ID = 1

client = ModbusTcpClient(HOST, port=PORT)

if not client.connect():
    print("Connection failed")
    raise SystemExit

result = client.write_registers(
    address=ADDRESS,
    values=[VALUE],
    device_id=DEVICE_ID
)

if result.isError():
    print("WRITE ERROR:", result)
else:
    print("WRITE SUCCESS")
    print("Address :", ADDRESS)
    print("Value   :", VALUE)

client.close()