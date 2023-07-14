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
        self.valueManager = ValueManager(self.ioManager.getConfigValues(), self.ioManager.getMinMaxValues(), self.ioManager.getTypesAndModes())
        #Instanciate SensorManager providing central value object.
        self.sensorDM = SensorDataManager(self.ioManager.getConfigValues())
        self.sensorDM.setUpSensors()
        #Instanciate ButtonEventManager
        self.buttonEM = ButtonEventManager(self.ioManager.getConfigValues())
        self.buttonEM.setupButtons()       
        #Instanciate Activity Manager providing central value object
        self.activityManager = ActivityManager(self.valueManager)
        self.activityManager.setupActivities()
        

    
    def establishManagerConnections(self):
        self.buttonEM.attach(self.activityManager)
        self.sensorDM.attach(self.activityManager)
    
    