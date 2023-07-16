import json

'''
Purpose of the IOManager is to make sure that contents like the configuration json file can be both read and written properly.
If this does not work 
'''
class IOManager:
    
    CONFIG_FILE = "values.json"
    MIN_MAX_FILE = "minMaxValues.json"
    TYPES_AND_MODES = "typesAndModes.json"
    configObject = ()
    minMaxObject = ()
    typesAndModesObject = ()
    
    def __init__(self):
        if self.checkFileExists():
            self.readConfiguration()
            self.readMinMaxValues()
            self.readTypesAndModes()
            
    def readConfiguration(self):
        print(self.CONFIG_FILE)
        try:
            with open(self.CONFIG_FILE) as inStream:
                self.configObject = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ")                  

    def readMinMaxValues(self):
        print(self.MIN_MAX_FILE)
        try:
            with open(self.MIN_MAX_FILE) as inStream:
                self.minMaxObject = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ")
    
    def readTypesAndModes(self):
        print(self.TYPES_AND_MODES)
        try:
            with open(self.TYPES_AND_MODES) as inStream:
                self.typesAndModesObject = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ") 

    def writeConfiguration (self, jsonObject):
        try:
            with open(self.CONFIG_FILE) as outStream:
                json.dump(jsonObject, outStream)
        except Exception:
            print ("ERROR: JSON FILE COULD NOT BE WRITTEN")   
            
    def checkFileExists(self): #todo implement
        return True
    
    def getConfigValues (self):
        #todo implement check, if object has in fact values. 
        return self.configObject
    
    def getMinMaxValues (self):
        return self.minMaxObject
    
    def getTypesAndModes (self):
        return self.typesAndModesObject
    
    
    