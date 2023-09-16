import serial
import time

global ser

def EstablishConnection():
    try : 
        ser = serial.Serial('COM4', 9600, timeout=0.5)
        print('COM4 is open at 9600 baud rate => ',ser.is_open())
        return ser.is_open()
    except:
        nser = serial.Serial('COM4', 115200)
        if not nser.is_open():
            nser.open()
            print('com4 is open => ', nser.is_open())
            return nser.is_open()
        

def SendSerialData(data):
    conn = EstablishConnection()
    if conn == True :
        ser.write(bytes('L', 'UTF-8'))
    print(data)
    