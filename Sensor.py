from Observer import Subject

class Sensor (Subject): #todo sensor-Klasse abstrahieren
 
    def __init__(self, sensorType):
        self.TYPE = sensorType            
   
    #Override
    def initSensorCommunication (self):
        pass
    
    #Override
    def readValues (self):
        pass
    
    def getSensorType (self):
        return self.TYPE