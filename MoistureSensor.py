from Observer import Observer
from Activity import Activity
from Visualisation import Visualisation
import machine


'''
Used to establish and stop the connection to the ADC the sensor is connected to. 
Reads values and informs group of listeners

Implements Sensor class -> Is Subject / Observable.

Hardware:
Device used is a capacitive soil moisture sensor v2.0.
Takes up to 5,5V as input and outputs 0 ~ 3V

Raspberry Pi PICO's ADC is used, using 16bit as resolution.

'''

class MoistureSensor (Observer):
 
    value = -1
    
    # First sensor values need to be ignored due to latency of the sensor
    initialIgnoreValues = 10
    initialIgnoreCounter = 1
    
    analogValue = 0
    
    NAME = "MOISTURESENSOR"
    
 
    def __init__(self):
        pass
    
    # TODO: exception handling
    def startAdcCommunication (self):
        # Initiate the analog digital converter for capacitive soil moist sensor.
        self.analogValue = machine.ADC(26)
   
    def readValues (self):
        
        # Read value from sensor
        temp =  self.analogValue.read_u16()
        
        # Overcome first value problem
        if self.value == -1:
            self.value = temp
            
        #Due to the sensor taking some time to adjust to real values 
        #one needs to ignore the first x values to avoid unnecessary watering
        if self.initialIgnoreCounter <= self.initialIgnoreValues:
            self.initialIgnoreCounter+=1
            print ('DEBUG - InitialIgnoreState: {0}'.format(temp)) 
            self.value = temp
            return
        
        # Get the difference between current and last measurement
        diff = self.value - temp
        print("DEBUG - Difference between current and last value: {0} - {1} = {2})".format(self.value, temp, diff))
        # Trigger the Observable notify method
        self.notify()
        # Store last value for comparison in next round
        self.value = temp
