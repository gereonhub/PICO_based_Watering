
class SensorType:
    
    sensorTypes = {
        "moisture":"MOISTURE_SENSOR",
        "temp":"TEMPERATURE_SENSOR",
        "none":"NONE"
        }

    def __init__ (self):
        pass
    
    def getSensorTypes (cls):
        return cls.sensorTypes