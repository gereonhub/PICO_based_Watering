import json

'''
Purpose of the IOManager is to make sure that contents like the configuration json file can be both read and written properly.
If this does not work 
'''
class IOManager:
    
    CONFIG_FILE = "values.json"
    configObject = ()
    
    def __init__(self):
        if self.checkFileExists():
            self.readConfiguration()
    
    def readConfiguration(self):
        print(self.CONFIG_FILE)
        try:
            with open(self.CONFIG_FILE) as inStream:
                self.configObject = json.load(inStream)
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
    
    def getConfigObject (self):
        #todo implement check, if object has in fact values. 
        return self.configObject
    

    