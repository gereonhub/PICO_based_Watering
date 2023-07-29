'''
Instanciated by values of existing configuration file.
'''
class value_manager :
    
    values = {}
    minMaxValues = {}
    typesAndModes = {}

    def __init__(self, storedConfig, minMax, typeMode):
        self.values = storedConfig
        self.minMaxValues = minMax
        self.typesAndModes = typeMode
        
    def setValue(self, currentMode, value):
        #1. check what is current mode 
        #2. check Parameter min max
        #3. adjust parameter
        print("VM - setValue() - OldValue "+ str(self.values[currentMode]))
        print("VM - setValue() - targetValue "+ str(value))
        try:
            if self.minMaxValues[currentMode]["MIN"] <= value and self.minMaxValues[currentMode]["MAX"]>= value:
                self.values[currentMode] = value
        except KeyError as e:
            print("Key does not exist in list. Value cannot be changed")
        print("VM - setValue() - NewValue "+ str(self.values[currentMode]))
            
    def toggleMode (self):
        #1. check what is current mode -
        #2. toggle to next mode
        oldMode = self.values["MODE"]
        print("VM - toggleMode(): Current Mode" + oldMode)
        print("VM - toggleMode(): Index of current Mode" + str(self.typesAndModes["MODES"].index(self.values["MODE"])))
        
        newIndex = (self.typesAndModes["MODES"].index(self.values["MODE"]) + 1) % len(self.typesAndModes["MODES"])
        
        print("VM - toggleMode(): New Target Index (newIndex)" + str(newIndex))
        
        self.values["MODE"] = self.typesAndModes["MODES"][newIndex]
        newMode = self.values["MODE"]
        
        print("VM - toggleMode(): New Mode " + newMode)
        if not oldMode == newMode:
            return True
        else:
            return False
            
        