Windows Runtime v4 test
- PLC build/upload/run: PASS
- Modbus TCP server port 502: PASS
- %MW0 Modbus read: PASS
- %QX0.0 coil read with Force: PASS
- PLC temperature alarm logic: PASS
- Modbus FC6/FC16 write persistence: FAIL
  - Server returned successful write response
  - Immediate read returned 0
- Next: reproduce write test on Docker/Linux Runtime
