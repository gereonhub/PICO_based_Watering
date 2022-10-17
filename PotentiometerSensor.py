from Sensor import Sensor
from Activity import Activity
from Visualisation import Visualisation
import machine


'''
Used to establish and stop the connection to the ADC the ponti is connected to. 
Reads values and informs group of listeners

Implements Sensor class -> Is Subject / Observable.

Hardware:
Potentiometer

Raspberry Pi PICO's ADC is used, using 16bit as resolution.

'''

class PotentiometerSensor (Sensor):
 
    analogValuePonti = ()
    
    threshold = 0
    
    NAME = "POTENTIOMETER"
    
 
    def __init__(self):
        pass
    
    # TODO: exception handling
    def startAdcCommunication (self):
        # Initiate the analog digital converter for values provided by the potentiometer
        self.analogValuePonti = machine.ADC(27)
        
  
    def readValues (self):
        # Read value from potentiometer. 
        self.threshold = self.analogValuePonti.read_u16()
        # Trigger the Observable notify method
        self.notify()
