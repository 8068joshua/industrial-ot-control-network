from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=1502)

if not client.connect():
    print("Connection failed")
    raise SystemExit

result = client.read_holding_registers(
    address=0,
    count=1,
    device_id=1
)

print(result.registers if not result.isError() else result)

client.close()