import utime

from Observer import Observer, Subject
from pumpActivity import PumpActivity

'''
Responsible to instanciate and control the Activities
'''
class ActivityManager (Observer, Subject) :
    
    lastWateringActivity = 0
    
    #MoistureSensor -> mose
    moseData = 5 # todo 5 only for debug reason. should be 0
    moseSpikeProtectionCounter = 0 
    
    '''
    ConfigValues is the reference to the valueManager object #todo should be a singleton
    '''    
    def __init__(self, valuesOfvalueManager):
        self.configValues = valuesOfvalueManager
        Observer.__init__(self)
        Subject.__init__(self)
    
    def setupActivities(self):
        # Pump
        self.pumpActivityObject = PumpActivity(self.configValues["PIN_PUMP_ACTIVITY"])
        self.pumpActivityObject.initializePinObject()
        #todo LCD
        
        #todo Communication
    
    def update (self, data):
        if data.getEvent() == "DECREASE_EVENT":     
            print ("Runter")
            #todo Implement action
        elif data.getEvent() == "INCREASE_EVENT":
            print ("Hoch")
            #todo Implement action
        elif data.getEvent() == "MODE_CHANGE_EVENT":
            print ("Modus")
            #todo Implement action
        elif data.getEvent() == "WATERING_EVENT":
            print ("Watering")
            self.manualPumpControl()
        elif data.getEvent() == "MOISTURE_SENSOR_VALUE_EVENT":
            print ("SensorUpdate")
            self.automaticPumpControl()
        else:
            print ("NONE")#todo Implement action
        
        
    #-----------------------------------------------------------------------------------
    #-------------------------------Set Mode methods-----------------------------------
    def adjustModePrameters (self):
        #1. check what is current mode -> configValues MODE
        #2. check Parameter min max (#todo)
        #3. adjust parameter in configValues
        print("Current Mode: "+self.configValues["MODE"])
        pass
        
    def setMode (self):
        #1. check what is current mode -> configValues MODE
        #2. toggle to next mode
        #3. setMode in configValues MODE
        print("Current Mode: "+self.configValues["MODE"])
        pass
    
    
    #-----------------------------------------------------------------------------------
    #-------------------------------Pump Control methods--------------------------------
    
    def manualPumpControl(self):
        if self.pumpActivityObject.getCurrentValue():
            return
        else:
            self.pumpActivityObject.activatePump()
            utime.sleep(self.configValues["WATERING_TIME"])
            self.pumpActivityObject.stopPump()
    
    def automaticPumpControl (self):
        '''
        If wait state is still active (true if pump has been active recently)
        no automatic watering is possible. pumpActivityObject.getWaitState will
        be set to false as soon as defined waiting time period has been exceeded.
        '''
        if self.pumpActivityObject.getWaitState:
            waitStateTimeDifference = utime.time() - self.lastWateringActivity            
            if waitStateTimeDifference > self.configValues["WATERING_WAIT_TIME"]:
                self.wait = False
            else:
                print('DEBUG - "Wait" is still active') #todo delete - debugging
                return False
        print ('not waiting') #todo delete - debugging 
        
        '''
        If sensor data is below the threshold and the moseSpikeProtectionCounter is satisfied
        start watering for the defined amount of time. After the avtivity wait is set to true
        to start the wait phase
        '''
        print(str(self.moseData) +".>."+str(self.configValues["WATERING_THRESHOLD"])) #todo delete debugging
        if self.moseData > self.configValues["WATERING_THRESHOLD"]:
            print(str(self.moseSpikeProtectionCounter) +".<."+str(self.configValues["MOISTURE_SENSOR_SPIKE_PROTECTION"])) #todo delete debugging
            if self.moseSpikeProtectionCounter < self.configValues["MOISTURE_SENSOR_SPIKE_PROTECTION"]:
                self.moseSpikeProtectionCounter+=1
                return False
            else: 
                print('DEBUG - Threshold exceeded. Start watering...')#todo delete - debugging
                self.pumpActivityObject.activatePump()
                utime.sleep(self.configValues["WATERING_TIME"])
                self.pumpActivityObject.stopPump()           
                self.pumpActivityObject.setWaitState(True)
                self.lastWateringActivity = utime.time()
                self.moseSpikeProtectionCounter = 0
        else:
            if self.moseSpikeProtectionCounter > 0:
                self.moseSpikeProtectionCounter-=1
        utime.sleep(1)
   