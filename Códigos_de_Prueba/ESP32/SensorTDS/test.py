from machine import Pin, ADC
from time import sleep_ms as slms

pinSensorTDS = 39
analogBuffer = []
bTem = 0
sensTDS = ADC(Pin(pinSensorTDS))
sensTDS.atten(ADC.ATTN_0DB)
sensTDS.atten(ADC.WIDTH_12BIT)
temp = 25
SCOUNT = 30
VREF = 3.3

def getMedianNum(bArray):
    bArray.sort()
    return bArray[len(bArray)//2] + bArray[~len(bArray)//2]/2

def readTDSValue():
    if (SCOUNT >= 0):
        slms(40)
        analogBuffer.append(sensTDS.read())
        SCOUNT -= 1
        # ? Return analogBuffer to empty after SCOUNT equal to 0
        if (SCOUNT == 0):
            SCOUNT = 30

    for i in analogBuffer:
        averageVoltage = getMedianNum(analogBuffer) * float(VREF) / float(4096.0);
        # ! The optimal operating value for the sensor is 25 °,
        # ! If the temperature value is greater or lower, it must be adjusted to compensate for the sensor
        compensationCoefficient = 1+float(0.02*(temp-25));
        compensationVoltage = averageVoltage/compensationCoefficient
        tdsValue=(133.42*compensationVoltage*compensationVoltage*compensationVoltage - 255.86*compensationVoltage*compensationVoltage + 857.39*compensationVoltage)*0.5;
        # * Additionally you can return averageVoltage to have a reference
        return tdsValue # or {averageVoltage, tdsValue}

readTDSValue()