from SensorDataManager import SensorDataManager
from ioManager import IOManager

def runMoistureSensorTest(testSensor):
    print(testSensor.getSensorType())
    testSensor.initSensorCommunication()
    print(str(testSensor.readValues()))
    return True


if __name__ == '__main__':   # Program entrance
    ioManager = IOManager()
    sev = SensorDataManager(ioManager.getConfigValues())
    sev.setUpSensors()
    runMoistureSensorTest (sev.moistureSensor)
    sev.moistureSensor.notify()
    print("Setup passed")
    
    while (True):
        pass

   