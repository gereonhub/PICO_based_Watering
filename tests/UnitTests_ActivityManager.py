from pump_activity import PumpActivity
from activity_manager import ActivityManager
from io_manager import IOManager

def runActivityManagerTest ():
    ioManager = IOManager()
    am = ActivityManager (ioManager.getConfigValues())
    print ("am is initiated")
    am.setupActivities()
    print("activites updates")
    am.automaticPumpControl()
    am.automaticPumpControl()
if __name__ == '__main__':   # Program entrance
    runActivityManagerTest()




