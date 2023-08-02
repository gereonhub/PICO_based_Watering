'''
Instanciated by values of existing configuration file.
'''
class ValueManager :
    
    values = {}
    minMaxValues = {}
    typesAndModes = {}

    def __init__(self, storedConfig, minMax, typeMode, logger):
        self.values = storedConfig
        self.minMaxValues = minMax
        self.typesAndModes = typeMode
        self.logger = logger
        
    def setValue(self, currentMode, value):
        #1. check what is current mode 
        #2. check Parameter min max
        #3. adjust parameter
        self.logger.log("VM - setValue() - OldValue "+ str(self.values[currentMode]))
        self.logger.log("VM - setValue() - targetValue "+ str(value))
        try:
            if self.minMaxValues[currentMode]["MIN"] <= value and self.minMaxValues[currentMode]["MAX"]>= value:
                self.values[currentMode] = value
        except KeyError as e:
            self.logger.error("VM - Key does not exist in list. Value cannot be changed")
        self.logger.log("VM - setValue() - NewValue "+ str(self.values[currentMode]))
            
    def toggleMode (self):
        #1. check what is current mode -
        #2. toggle to next mode
        oldMode = self.values["MODE"]
        ("VM - toggleMode(): Current Mode" + oldMode)
        self.logger.log("VM - toggleMode(): Index of current Mode" + str(self.typesAndModes["MODES"].index(self.values["MODE"])))
        
        newIndex = (self.typesAndModes["MODES"].index(self.values["MODE"]) + 1) % len(self.typesAndModes["MODES"])
        
        self.logger.log("VM - toggleMode(): New Target Index (newIndex)" + str(newIndex))
        
        self.values["MODE"] = self.typesAndModes["MODES"][newIndex]
        newMode = self.values["MODE"]
        
        self.logger.log("VM - toggleMode(): New Mode " + newMode)
        if not oldMode == newMode:
            return True
        else:
            return False
            
        