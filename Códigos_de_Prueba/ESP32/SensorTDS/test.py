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

def getMedianNum(bArray, iFilterLen):
    bTab = bArray.copy()
    for i in range(iFilterLen):
        for j in range((iFilterLen-i-1)):
            if (bTab[j] > bTab[j + 1]):
                bTem = bTab[j]
                bTab[j] = bTab[j + 1]
                bTab[i + 1] = bTem
    return bTab[(iFilterLen - 1) / 2] if ((iFilterLen & 1) > 0) else (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2

def readTDSValue():
    if (SCOUNT >= 0):
        slms(40)
        analogBuffer.append(sensTDS.read())
        SCOUNT -= 1
        # ? Return analogBuffer to empty after SCOUNT equal to 0
        if (SCOUNT == 0):
            SCOUNT = 30

    for i in analogBuffer:
        averageVoltage = getMedianNum(analogBuffer,SCOUNT) * float(VREF) / float(4096.0);
        # ! The optimal operating value for the sensor is 25 °,
        # ! If the temperature value is greater or lower, it must be adjusted to compensate for the sensor
        compensationCoefficient = 1+float(0.02*(temp-25));
        compensationVoltage = averageVoltage/compensationCoefficient
        tdsValue=(133.42*compensationVoltage*compensationVoltage*compensationVoltage - 255.86*compensationVoltage*compensationVoltage + 857.39*compensationVoltage)*0.5;
        # * Additionally you can return averageVoltage to have a reference
        return tdsValue # or {averageVoltage, tdsValue}

readTDSValue()