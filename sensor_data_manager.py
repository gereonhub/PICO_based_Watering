from utime import sleep_ms

from Observer import Observer, Subject
from logger import Logger
from adc_sensor import AdcSensor

class SensorDataManager (Observer, Subject):

    event = "" #IMPORTANT for every Manager class

    def __init__(self, values, logger):
        self.values = values
        self.logger = logger
        Observer.__init__(self)
        Subject.__init__(self)
    
    def setUpSensors(self):
        #todo type and PIN need to be checked here to make sure config values are valid
        self.moistureSensor = AdcSensor(self.values["PIN_ADC_MOISTURE_SENSOR"], "MOISTURE_SENSOR", self.logger)
        self.moistureSensor.initSensorCommunication()
        self.moistureSensor.attach(self)
    
    def update(self, sensor):
        self.logger.log("SM - update(): *** SensorUpdate triggered")
        if sensor.getSensorType() == "MOISTURE_SENSOR":
            self.logger.log ("SM - update(): " + sensor.getSensorType() + " has sent an update")
            self.event = self.determineEventType(sensor)
            self.values["CURRENT_SENSOR_VALUE"] = sensor.value
            self.notify()

    def determineEventType(self, sensor):
        if sensor.getSensorType() == "MOISTURE_SENSOR":
            return "MOISTURE_SENSOR_VALUE_EVENT"         

    def getEvent (self):
        return self.event
    
    def start (self):
        while True:
            self.moistureSensor.readValues()
            sleep_ms(1000)
            