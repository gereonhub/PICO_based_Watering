from buttonType import ButtonType
from SensorType import SensorType
from modeType import ModeType

'''
Instanciated by values of existing configuration file.
'''
class ValueManager :
    
    values = {}
    minMaxValues = {}
    typesAndModes = {}

    def __init__(self, storedConfig, minMax, typeMode):
        self.values = storedConfig
        self.minMaxValues = minMax
        self.typesAndModes = typeMode
        
    def setValue(self, category, value):
        try:
            if self.minMaxValues[category]["MIN"] <= value and self.minMaxValues[category]["MAX"]>= value:
                self.values[category] = value
        except KeyError as e:
            print("Key does not exist in list. Value cannot be changed")
            
    def setMode (self, category, value):
        pass
            
        