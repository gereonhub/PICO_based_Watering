from observer import subject

class sensor (subject): #todo sensor-Klasse abstrahieren
 
    def __init__(self, sensor_type):
        self.TYPE = sensor_type            
   
    #Override
    def init_sensor_communication (self):
        pass
    
    #Override
    def read_values (self):
        #todo implmenent
        pass
    
    def get_sensor_type (self):
        return self.TYPE