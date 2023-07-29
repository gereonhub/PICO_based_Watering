from value_manager import value_manager
from activity_manager import activity_manager
from button_event_manager import button_event_manager
from io_manager import io_manager
from sensor_data_manager import SensorDataManager

class control_module:
    
    def __init__(self):
       pass 
    
    def setup_managers(self):
        # Open filestream and deserialize configValue file (JSON)
        self.ioManager = io_manager()
        # Instanciate central file manager using config values to create central value object
        self.valueManager = ValueManager(self.ioManager.get_config_values(), self.ioManager.get_min_max_values(), self.ioManager.get_types_and_modes())
        #Instanciate SensorManager providing central value object.
        self.sensorDM = SensorDataManager(self.ioManager.get_config_values())
        self.sensorDM.setUpSensors()
        #Instanciate ButtonEventManager
        self.buttonEM = button_event_manager(self.ioManager.get_config_values())
        self.buttonEM.setup_buttons()       
        #Instanciate Activity Manager providing central value object
        self.activityManager = ActivityManager(self.valueManager)
        self.activityManager.setupActivities()

    
    def establish_manager_connections(self):
        self.buttonEM.attach(self.activityManager)
        self.sensorDM.attach(self.activityManager)
