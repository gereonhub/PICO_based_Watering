from value_manager import ValueManager
from activity_manager import ActivityManager
from button_event_manager import ButtonEventManager
from io_manager import IOManager
from sensor_data_manager import SensorDataManager
from logger import Logger

class ControlModule:
    
    def __init__(self):
       pass 
    
    def setupManagers(self):
        # Init logger class - True -> logger active, False -> logger inactive
        self.logger = Logger(False)
        # Open filestream and deserialize configValue file (JSON)
        self.ioManager = IOManager()
        # Instanciate central file manager using config values to create central value object
        self.valueManager = ValueManager(self.ioManager.getConfigValues(), self.ioManager.getMinMaxValues(), self.ioManager.getTypesAndModes(),self.logger)
        #Instanciate SensorManager providing central value object.
        self.sensorDM = SensorDataManager(self.ioManager.getConfigValues(), self.logger)
        self.sensorDM.setUpSensors()
        #Instanciate ButtonEventManager
        self.buttonEM = ButtonEventManager(self.ioManager.getConfigValues(), self.logger)
        self.buttonEM.setupButtons()       
        #Instanciate Activity Manager providing central value object
        self.activityManager = ActivityManager(self.valueManager, self.logger)
        self.activityManager.setupActivities()

    
    def establishManagerConnections(self):
        self.buttonEM.attach(self.activityManager)
        self.sensorDM.attach(self.activityManager)
        
    def startMainThread(self):
        self.sensorDM.start()
