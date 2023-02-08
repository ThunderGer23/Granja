import socket, network, time
from machine import Pin, ADC
from machine.ADC import ATTN_11DB, WIDTH_12BIT
from time import sleep_ms as slms
from alerts.messages import MessageAlertValues
from access.keys import passwordESPServ as passw
from access.keys import nameModule as mod
from access.connectTo import internet

# Setting the pins for the sensors.
pinSensorTDS = 39
pinSensorTUB = 36

# Creating an empty list for the readSensor.
analogBuffer = []

# Setting up the ADC for the pins.
sensTDS = ADC(Pin(pinSensorTDS))
sensTDS.atten(ATTN_11DB)
sensTDS.atten(WIDTH_12BIT)
sensTUB = ADC(Pin(pinSensorTUB))
sensTUB.atten(ATTN_11DB)
sensTUB.atten(WIDTH_12BIT)

# These are just variables that are used in the code.
bTem = 0
TEMP = 25
SCOUNT = 30
VREF = 3.3
SENSE_RATE = 40 #ms

# A lambda function that is used to read the value of the Turbidity sensor.
readSenseTUB = lambda : sensTUB.read() * 0.000855

def getMedianNum(bArray, iFilterLen):
    """
    It sorts the array and returns the middle value
    
    :param bArray: the array of numbers to be filtered
    :param iFilterLen: The length of the filter
    :return: The median value of the array.
    """
    bTab = bArray.copy()
    for i in range(iFilterLen):
        for j in range((iFilterLen-i-1)):
            if (bTab[j] > bTab[j + 1]):
                bTem = bTab[j]
                bTab[j] = bTab[j + 1]
                bTab[i + 1] = bTem
    return bTab[(iFilterLen - 1) / 2] if ((iFilterLen & 1) > 0) else (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2

def readTDSValue():
    """
    > The function reads the analog value of the sensor, converts it to a voltage value, and then
    converts it to a TDS value
    :return: The TDS value is being returned.
    """
    if (SCOUNT >= 0):
        slms(SENSE_RATE)
        analogBuffer.append(sensTDS.read())
        SCOUNT -= 1
        # ? Return analogBuffer to empty after SCOUNT equal to 0
        if (SCOUNT == 0):
            SCOUNT = 30

    for i in analogBuffer:
        averageVoltage = float(getMedianNum(analogBuffer,SCOUNT) * VREF / 4095);
        # ! The optimal operating value for the sensor is 25 °,
        # ! If the temperature value is greater or lower, it must be adjusted to compensate for the sensor
        compensationCoefficient = 1+float(0.02*(TEMP-25));
        compensationVoltage = averageVoltage/compensationCoefficient
        tdsValue=(133.42*(compensationVoltage**3) - 255.86*(compensationVoltage**2) + 857.39*compensationVoltage)*0.5;
        # * Additionally you can return averageVoltage to have a reference
        return tdsValue # or {averageVoltage, tdsValue}

def initSensors():
    #TODO: Evaluate the return values based on the parameters that we require to
    #TODO: Promote the life of marine species and if those values get out of rank
    #TODO: Execute While

    # ? A while loop that is used to connect to the server and send a message to it.
    # * while(True):
    # *     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    # *      addr = ("192.168.4.1",80)
    # *      s.connect(addr)
    # *      message = bytes(input('Message: '),'utf-8')
    # *      s.sendall(message)
    # *      print(str(s.recv(4096),'utf-8'))
    # *      s.close()
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        addr = ("192.168.4.1",80)
        sensTDS = readTDSValue()
        sensTUB = readSenseTUB()
        slms(SENSE_RATE)
        # TODO: Here the conditional to evaluate the values and if we meet the connection
        s.connect(addr)
        message = bytes(f'"MAV":"{MessageAlertValues}",  "sensTDS":"{str(sensTDS)}",  "sensTUB":"{str(sensTUB)}"','utf-8')
        s.sendall(message)
    except Exception as e:
        print(e,'!!!')
        pass
        # TODO: Here you could also validate whether the message is sent correctly asking
        # TODO: for the value of return of str(s.recv(4096),'utf-8'), if the message is not
        # TODO: make success to repeat data 3 times
    finally:
        s.close()
    return

internet(mod, passw)
initSensors()