from valueManager import ValueManager
from pumpActivity import PumpActivity
from activityManager import ActivityManager

def runActivityManagerTest ():
    values = ValueManager()
    print(values.PIN_MODE_BUTTON)
    am = ActivityManager (values)
    print ("am is initiated")
    am.setupActivities()
    print("activites updates")
    am.automaticPumpControl()
    am.automaticPumpControl()
if __name__ == '__main__':   # Program entrance
    runActivityManagerTest()




