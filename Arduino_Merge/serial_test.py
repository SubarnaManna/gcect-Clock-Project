import serial
ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM4'
# ser
# Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
ser.open()
ser.is_open
# True
ser.close()
ser.is_open
# False