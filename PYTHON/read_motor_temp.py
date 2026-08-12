from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)

if not client.connect():
    print("Connection failed")
    raise SystemExit

result = client.read_holding_registers(
    address=1024,
    count=1,
    device_id=1
)

print("Raw response:", result)

if result.isError():
    print("READ ERROR:", result)
else:
    print("Registers:", result.registers)

    raw = result.registers[0]

    print("MOTOR_TEMP_RAW =", raw)
    print("MOTOR_TEMP =", raw / 10.0, "°C")

client.close()