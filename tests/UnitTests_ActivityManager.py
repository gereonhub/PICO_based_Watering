from pumpActivity import PumpActivity
from activityManager import ActivityManager
from io_manager import io_manager

def runActivityManagerTest ():
    ioManager = io_manager()
    am = ActivityManager (ioManager.get_config_values())
    print ("am is initiated")
    am.setupActivities()
    print("activites updates")
    am.automaticPumpControl()
    am.automaticPumpControl()
if __name__ == '__main__':   # Program entrance
    runActivityManagerTest()




