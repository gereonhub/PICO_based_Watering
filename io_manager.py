import json

'''
Purpose of the IOManager is to make sure that contents like the configuration json file can be both read and written properly.
If this does not work 
'''
class io_manager:
    
    CONFIG_FILE = "values.json"
    MIN_MAX_FILE = "minMaxValues.json"
    TYPES_AND_MODES = "typesAndModes.json"
    config_object = ()
    min_max_object = ()
    types_and_modes_object = ()
    
    def __init__(self):
        if self.check_file_exists():
            self.read_configuration()
            self.read_min_max_values()
            self.read_types_and_modes()
            
    def read_configuration(self):
        print(self.CONFIG_FILE)
        try:
            with open(self.CONFIG_FILE) as inStream:
                self.config_object = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ")                  

    def read_min_max_values(self):
        print(self.MIN_MAX_FILE)
        try:
            with open(self.MIN_MAX_FILE) as inStream:
                self.min_max_object = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ")
    
    def read_types_and_modes(self):
        print(self.TYPES_AND_MODES)
        try:
            with open(self.TYPES_AND_MODES) as inStream:
                self.types_and_modes_object = json.load(inStream)
        except ValueError:
            print ("ERROR: JSON FILE COULD NOT BE READ") 

    def write_configuration (self, jsonObject):
        try:
            with open(self.CONFIG_FILE) as outStream:
                json.dump(jsonObject, outStream)
        except Exception:
            print ("ERROR: JSON FILE COULD NOT BE WRITTEN")   
            
    def check_file_exists(self): #todo implement
        return True
    
    def get_config_values (self):
        #todo implement check, if object has in fact values. 
        return self.config_object
    
    def get_min_max_values (self):
        return self.min_max_object
    
    def get_types_and_modes (self):
        return self.types_and_modes_object
    
    
    