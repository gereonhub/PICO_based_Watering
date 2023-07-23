from valueManager import ValueManager
from io_manager import IOManager

if __name__ == '__main__':
    iom = IOManager()
    valueManager = ValueManager(iom.getConfigValues(),iom.getMinMaxValues(), iom.getTypesAndModes())
    print(valueManager.values["BUTTONS"])
    #valueManager.values["DEBUG"] = "VeraenderterWert"
    #print(valueManager.values["DEBUG"])
    print(valueManager.values["MOISTURE_SENSOR_SPIKE_PROTECTION"])
    valueManager.setValue("MOISTURE_SENSOR_SPIKE_PROTECTION", 15)
    print(valueManager.values["MOISTURE_SENSOR_SPIKE_PROTECTION"])
    valueManager.setValue("MOISTURE_SENSOR_SPIKE_PROTECTION", 21)
    print(valueManager.values["MOISTURE_SENSOR_SPIKE_PROTECTION"])
    iom.writeConfiguration(valueManager.values)
     
    
    
    
    '''
    "PIN_MODE_BUTTON": 4,
	"PIN_UP_BUTTON": 3,
	"PIN_DOWN_BUTTON": 2,
	"PIN_WATERING_BUTTON": 5,
	"PIN_ADC_MOISTURE_SENSOR": 26,
	"MOISTURE_SENSOR_SPIKE_PROTECTION": 0,
	"MOISTURE_SENSOR_INITIAL_IGNORE": 10,
	"PIN_PUMP_ACTIVITY": 16,
	"WATERING_TIME": 5,
	"WATERING_THRESHOLD": 3,
	"WATERING_WAIT_TIME": 120,
	"MODE": "ACTIVATE_WATERING_MODE",
	"DEBUG": "LastENTRY"
	'''
          