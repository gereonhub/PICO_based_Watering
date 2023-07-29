from sensor_data_manager import SensorDataManager
from io_manager import io_manager

def runMoistureSensorTest(testSensor):
    print(testSensor.getSensorType())
    testSensor.initSensorCommunication()
    print(str(testSensor.readValues()))
    return True


if __name__ == '__main__':   # Program entrance
    ioManager = io_manager()
    sev = SensorDataManager(ioManager.get_config_values())
    sev.setUpSensors()
    runMoistureSensorTest (sev.moistureSensor)
    sev.moistureSensor.notify()
    print("Setup passed")
    
    while (True):
        pass

   