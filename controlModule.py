from valueManager import ValueManager
from activityManager import ActivityManager
from ButtonEventManager import ButtonEventManager
from ioManager import IOManager
from SensorDataManager import SensorDataManager

class ControlModule:
    
    def __init__(self):
       pass 
    
    def setupManagers(self):
        # Open filestream and deserialize configValue file (JSON)
        self.ioManager = IOManager()
        # Instanciate central file manager using config values to create central value object
        self.valueManager = ValueManager(self.ioManager.getConfigObject())
        #Instanciate SensorManager providing central value object.
        ###self.sensorDM = SensorDataManager(self.valueManager.values)
        #Instanciate ButtonEventManager
        self.buttonEM = ButtonEventManager()
        self.buttonEM.setupButtons()       
        #Instanciate Activity Manager providing central value object
        self.activityManager = ActivityManager(self.valueManager.values)
        self.activityManager.setupActivities()
        

    
    def establishManagerConnections(self):
        self.buttonEM.attach(self.activityManager)    
    
    