from buttonType import ButtonType
from SensorType import SensorType
from modeType import ModeType

'''
Instanciated by values of existing configuration file.
If no configuration file can be loaded the standard contructor provides a set of standard values
'''
class ValueManager :
    
    values = {}


    def __init__(self):     
        #Buttons
        self.values["PIN_MODE_BUTTON"] = 4
        self.values["PIN_UP_BUTTON"] = 3
        self.values["PIN_DOWN_BUTTON"] = 2
        self.values["PIN_WATERING_BUTTON"] = 5
        
        #Moisture Sensor
        self.values["PIN_ADC_MOISTURE_SENSOR"] = 26
        self.values["MOISTURE_SENSOR_SPIKE_PROTECTION"] = 0 #todo only for debugging reaons. Should be at least 4
        self.values["MOISTURE_SENSOR_INITIAL_IGNORE"] = 10
        
        #Pump activity
        self.values["PIN_PUMP_ACTIVITY"] = 16
        self.values["WATERING_TIME"] = 5 #sec
        self.values["WATERING_THRESHOLD"] = 3 #todo only for debugging reasons. Should be > 25000
        self.values["WATERING_WAIT_TIME"] = 120 #sec
        self.values["MODE"] = "ACTIVATE_WATERING_MODE" #self.MODE = ModeType().getModeTypes().values()["none"]       #todo: fix TypeError: 'dict_view' object isn't subscriptable
    
    def __init__(self, storedConfig):
        self.values = storedConfig
        