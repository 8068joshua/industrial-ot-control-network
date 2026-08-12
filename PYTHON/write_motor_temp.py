from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)

if not client.connect():
    print("Connection failed")
    raise SystemExit

before = client.read_holding_registers(
    address=1024,
    count=1,
    device_id=1
)
print("BEFORE :", before.registers)

wr = client.write_registers(
    address=1024,
    values=[850],
    device_id=1
)
print("WRITE  :", wr)

after = client.read_holding_registers(
    address=1024,
    count=1,
    device_id=1
)
print("AFTER  :", after.registers)

client.close()