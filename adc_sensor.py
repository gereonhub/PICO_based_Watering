import machine

from sensor import sensor
from observer import subject


class AdcSensor (Sensor, Subject):
 
    VALID_ADC_GPIO_PINS = [26,27,28] #todo this should be part of config file
 
    value = -1
    
    # First sensor values need to be ignored due to latency of the sensor
    '''
    Needs to be adjustable by button with a respective mode.
    #todo re-init of button or value manipulation should then be possible by buttonManager
    '''
    initial_ignore_values = 10
    initial_ignore_counter = 1
    
    analog_value = 0    
 
    def __init__(self, pin, sensor_type): #todo Name might be useful, too. Two sensors of one type are theoretically possible.
        try:
            if pin not in self.VALID_ADC_GPIO_PINS:
                raise Exception('GPIO pin provided for sensor (' +str(pin)+ ') is invalid!')
            self.ADC_GPIO_PIN = pin
        except ValueError as ve:
            print('ERROR: ' + repr(ve) + " - Program terminated.")
            sys.exit()
        sensor.__init__(self, sensor_type)
        subject.__init__(self)
            
    #todo check if exception handling is ok here
    def initSensorCommunication (self):
        # Initiate the analog digital converter for capacitive soil moist sensor.
        try:
            self.analog_value = machine.ADC(self.ADC_GPIO_PIN)
        except Error as E:
            print (repr(E) + "ADC could not be initialized") #todo create proper exception handling
       
    def readValues (self):
        # Read value from sensor
        temp =  self.analog_value.read_u16()
        
        # Overcome first value problem
        if self.value == -1:
            self.value = temp
            
        #Due to the sensor taking some time to adjust to real values 
        #one needs to ignore the first x values to avoid unnecessary watering
        #todo This value should be configurable by button, too. 
        if self.initial_ignore_counter <= self.initial_ignore_values:
            self.initial_ignore_counter+=1
            #print ('DEBUG - InitialIgnoreState: {0}'.format(temp)) 
            self.value = temp
            return
        
        # Get the difference between current and last measurement
        diff = self.value - temp
        print("DEBUG - Difference between current and last value: {0} - {1} = {2})".format(self.value, temp, diff))
        # Trigger the Observable notify method
        self.notify()
        # Store last value for comparison in next round
        self.value = temp
    
    def get_sensor_pin(self):
        return self.ADC_GPIO_PIN



