from Observer import Subject
from SensorType import SensorType

class Sensor (Subject): #todo sensor-Klasse abstrahieren
 
    def __init__(self, sensorType):
        try:
            if sensorType in SensorType().getSensorTypes().values():
                self.TYPE = sensorType
            else:
                raise Exception('Name provided for sensor(' +str(btnType)+ ') is not a valid sensorType name!')
        except ValueError as ve:
            print('ERROR: ' + repr(ve) + " - Program terminated.")
            sys.exit()
   
    #Override
    def initSensorCommunication (self):
        pass
    
    #Override
    def readValues (self):
        pass
    
    def getSensorType (self):
        return self.TYPE