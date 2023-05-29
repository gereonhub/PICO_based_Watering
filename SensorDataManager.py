from Observer import Observer

from SensorType import SensorType
from AdcSensor import AdcSensor

class SensorDataManager (Observer):
    
    def setUpSensors(self):
        self.moistureSensor = AdcSensor(26, SensorType().getSensorTypes()["moisture"])
        self.moistureSensor.attach(self)
    
    def update(self, sensor):
        print ("*** SensorUpdate triggered")
        if sensor.getSensorType() == SensorType().getSensorTypes()["moisture"]:
            print ("MoistureSensor has sent an update")