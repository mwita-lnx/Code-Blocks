import serial
import time

arduino = serial.Serial(port='/dev/ttyACM1', baudrate=115200, timeout=.1)


def write_read():    
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    value = str(write_read())
    lst = value.split(',')
    cl = lst[0].replace("b'","")
    try:
        if lst[0] and lst[1] and lst[2] and lst[3]:
            data = {
                "deg":cl,
                "far":lst[1],
                "hum":lst[2],
                "lig":lst[3]

            }
            print(data)
            
    except:
        pass