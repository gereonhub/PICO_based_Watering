from Observer import Observer, Subject

from adc_sensor import adc_sensor

class SensorDataManager (Observer, Subject):

    event = "" #IMPORTANT for every Manager class

    def __init__(self, values):
        self.configValues = values
        Observer.__init__(self)
        Subject.__init__(self)
    
    def setUpSensors(self):
        #todo type and PIN need to be checked here to make sure config values are valid
        self.moistureSensor = adc_sensor(self.configValues["PIN_ADC_MOISTURE_SENSOR"], "MOISTURE_SENSOR")
        self.moistureSensor.attach(self)
    
    def update(self, sensor):
        print ("SM - update(): *** SensorUpdate triggered")
        if sensor.getSensorType() == "MOISTURE_SENSOR":
            print ("SM - update(): " + sensor.getSensorType() + " has sent an update")
            self.event = self.determineEventType(sensor)
            self.notify()

    def determineEventType(self, sensor):
        if sensor.getSensorType() == "MOISTURE_SENSOR":
            return "MOISTURE_SENSOR_VALUE_EVENT"         

    def getEvent (self):
        return self.event