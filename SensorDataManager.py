from Observer import Observer

from SensorType import SensorType
from AdcSensor import AdcSensor

class SensorDataManager (Observer):
    
    def __init__(self, storedConfig):
        self.configValues = storedConfig
        super().__init__()
    
    def setUpSensors(self):
        self.moistureSensor = AdcSensor(self.configValues["PIN_ADC_MOISTURE_SENSOR"], SensorType().getSensorTypes()["moisture"])
        self.moistureSensor.attach(self)
    
    def update(self, sensor):
        print ("*** SensorUpdate triggered")
        if sensor.getSensorType() == SensorType().getSensorTypes()["moisture"]:
            print ("MoistureSensor has sent an update")