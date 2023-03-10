from ControlClass import Controller
from PumpActivity import PumpActivity
from MoistureSensor import MoistureSensor
from PotentiometerSensor import PotentiometerSensor
from Visualisation import Visualisation
import _thread
   
   

if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    sensors = list()
    activities = list()
    try:
        # Create run time objects of all relevant classes
        moistureSensor = MoistureSensor()
        potentiometerSensor = PotentiometerSensor()
        pumpActivity = PumpActivity()
        visualisation = Visualisation() 
               
        # Activities are registered at the sonsors subscription list. Part of the observer pattern.
        moistureSensor.attach(pumpActivity)
        moistureSensor.attach(visualisation)
        potentiometerSensor.attach(pumpActivity)
        potentiometerSensor.attach(visualisation)
        
        activities.append(pumpActivity)    
        sensors.append(moistureSensor)
        sensors.append(potentiometerSensor)
        
        print ("Type and number of activites in activity list: " + str(type(activities))  + "   " + str(len(activities)))
        print ("Type and number of sensors in sensor list: " + str(type(sensors))  + "   " + str(len(sensors)))
        
        cc = Controller(sensors,activities,visualisation)
        moistureSensor.startAdcCommunication()
        potentiometerSensor.startAdcCommunication()
        cc.setupActivities()
        try:
            thread2 = _thread.start_new_thread(cc.manualButtonListener, ())
            cc.operate()
        except:
            print("Exception!!!")
    
        
    except KeyboardInterrupt: # Press ctrl-c to end the program.#
        cc.run = False
        cc.destroy()
