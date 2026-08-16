from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext,
)

# PyModbus datastore starts at address 1
# First Holding Register = 850 -> 85.0 °C
device = ModbusDeviceContext(
    hr=ModbusSequentialDataBlock(1, [850] + [0] * 99)
)

context = ModbusServerContext(
    devices={1: device},
    single=False
)

print("Motor sensor simulator started")
print("First Holding Register = 850 (85.0 °C)")
print("Listening on TCP port 1502")

StartTcpServer(
    context=context,
    address=("0.0.0.0", 1502)
)