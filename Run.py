from ControlClass import Controller
from PumpActivity import PumpActivity
from MoistureSensor import MoistureSensor
from Visualisation import Visualisation
import _thread
   
   

if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    sensors = list()
    activities = list()
    try:
        moistureSensor = MoistureSensor("Moisty")
        pumpActivity = PumpActivity()
        visualisation = Visualisation() 
               
        #Activity is registered at the subject's activity list
        moistureSensor.attach(pumpActivity)
        moistureSensor.attach(visualisation)
        
        activities.append(pumpActivity)    
        sensors.append(moistureSensor)
        
        print ("Type and number of activites in activity list: " + str(type(activities))  + "   " + str(len(activities)))
        print ("Type and number of sensors in sensor list: " + str(type(sensors))  + "   " + str(len(sensors)))
        
        cc = Controller(sensors,activities,visualisation)
        moistureSensor.startAdcCommunication()
        cc.setupActivities()
        try:
            thread2 = _thread.start_new_thread(cc.manualButtonListener, ())
            cc.operate()
        except:
            print("Exception!!!")
    
        
    except KeyboardInterrupt: # Press ctrl-c to end the program.#
        cc.run = False
        cc.destroy()
