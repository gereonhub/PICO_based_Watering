from SensorDataManager import SensorDataManager

def runMoistureSensorTest(testSensor):
    print(testSensor.getSensorType())
    testSensor.initSensorCommunication()
    '''
    try:
        print(str(testSensor.readValues()))
    except:
        print("readValues from Sensor failed")
    '''
    print(str(testSensor.readValues()))
    return True


if __name__ == '__main__':   # Program entrance
    
    sev = SensorDataManager()
    sev.setUpSensors()
    runMoistureSensorTest (sev.moistureSensor)
    sev.moistureSensor.notify()
    
    while (True):
        pass

   