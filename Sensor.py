from Observer import Subject

class Sensor (Subject): #todo sensor-Klasse abstrahieren
 
    def __init__(self, sensorType, logger):
        self.TYPE = sensorType
        self.logger = logger
   
    #Override
    def initSensorCommunication (self):
        pass
    
    #Override
    def readValues (self):
        pass
    
    def getSensorType (self):
        return self.TYPE