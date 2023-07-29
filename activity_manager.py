import utime

from Observer import Observer, Subject
from pump_activity import PumpActivity
from Visualisation import LCD1602Visualisation

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
    def __init__(self, valueManagerObject):
        self.configValues = valueManagerObject.values
        self.valueManager = valueManagerObject
        Observer.__init__(self)
        Subject.__init__(self)


    def setupActivities(self):
        # Pump
        self.pumpActivityObject = PumpActivity(self.configValues["PIN_PUMP_ACTIVITY"])
        self.pumpActivityObject.initializePinObject()
        # LCD 1602
        self.lcd1602visualisation = LCD1602Visualisation(self.configValues["PIN_LCD_I2C_SDA"],self.configValues["PIN_LCD_I2C_SCL"], self.configValues["FREQ_LCD_1602"])
         #todo Communication


    def update (self, data):
        if data.getEvent() == "DECREASE_EVENT":     
            print ("AM - update(): DECREASE_EVENT")
            self.adjustModeParameters("DOWN")
            self.updateDisplayedModeValue()
        elif data.getEvent() == "INCREASE_EVENT":
            print ("AM - update(): INCREASE_EVENT")
            self.adjustModeParameters("UP")
            self.updateDisplayedModeValue()
        elif data.getEvent() == "MODE_CHANGE_EVENT":
            print ("AM - update(): MODE_CHANGE_EVENT")
            self.setMode()
            self.updateDisplayedMode()
        elif data.getEvent() == "WATERING_EVENT":
            print ("AM - update(): WATERING_EVENT")
            self.manualPumpControl()
            self.visualiseWateringActivity()
        elif data.getEvent() == "MOISTURE_SENSOR_VALUE_EVENT":
            print ("AM - update(): MOISTURE_SENSOR_VALUE_EVENT")
            #todo how to get the actual SensorData through? 
            self.automaticPumpControl()
            self.updateDisplayedSensorValue()
        else:
            print ("NONE")#todo Implement action


    #-----------------------------------------------------------------------------------
    #-------------------------------Set Mode methods-----------------------------------
    def adjustModeParameters (self, upDownFlag):
        print("AM - adjustModeParameters(): Current Mode: "+self.configValues["MODE"])
        print("AM - adjustModeParameters(): Current Mode Value: "+str(self.configValues[self.configValues["MODE"]]))
        #1. get current value of MODE/Category
        #2. increase/decrease value (usually +/-1, except for WATERING_THRESHOLD)
        #3. try to set value in ValueManager
        tempModeValue = self.configValues[self.configValues["MODE"]]
        if self.configValues["MODE"] == "WATERING_THRESHOLD":
            if upDownFlag == "UP":
                tempModeValue += self.configValues["WATERING_THRESHOLD_UP_DOWN_VALUE"]
            if upDownFlag == "DOWN":
                tempModeValue -= self.configValues["WATERING_THRESHOLD_UP_DOWN_VALUE"]
        else:
            if upDownFlag == "UP":
                tempModeValue +=1
            if upDownFlag == "DOWN":
                tempModeValue -=1
                
        if self.valueManager.setValue(self.configValues["MODE"], tempModeValue):
            #todo implement LCD output
            print("Value has been changed")
        print("AM - adjustModeParameters(): NEW Mode Value: "+ str(self.configValues[self.configValues["MODE"]]))
        
    def setMode (self):
        print("AM - setMode(): Current Mode: "+self.configValues["MODE"])
        if self.valueManager.toggleMode():
            print("Mode has been changed")
        else:
            print("ERROR Value has NOT been changed")
    
    
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
        if self.pumpActivityObject.getWaitState():
            waitStateTimeDifference = utime.time() - self.lastWateringActivity            
            if waitStateTimeDifference <= self.configValues["WATERING_WAIT_TIME"]:
                print('DEBUG - "Wait" is still active') #todo delete - debugging
                return False
            self.wait = False
        print ('AM - automaticPumpControl: not waiting') #todo delete - debugging 
        
        '''
        If sensor data is below the threshold and the moseSpikeProtectionCounter is satisfied
        start watering for the defined amount of time. After the avtivity wait is set to true
        to start the wait phase
        '''
        print("AM - automaticPumpControl(): Sensor data versus threshold: "+str(self.moseData) +".>."+str(self.configValues["WATERING_THRESHOLD"])) #todo delete debugging
        if self.moseData > self.configValues["WATERING_THRESHOLD"]:
            print(str(self.moseSpikeProtectionCounter) + ".<." + str(self.configValues["MOISTURE_SENSOR_SPIKE_PROTECTION"])) #todo delete debugging
            if self.moseSpikeProtectionCounter < self.configValues["MOISTURE_SENSOR_SPIKE_PROTECTION"]:
                self.moseSpikeProtectionCounter+=1
                return False
            # else überflüssig - Du hast ein return drin, im if-Fall
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
        
    #-----------------------------------------------------------------------------------
    #-------------------------------Visualisation methods-------------------------------
        
    def updateDisplayedSensorValue(self):
        self.lcd1602visualisation.debugDisplay("Thresh: " + str(self.valueManager.values[self.configValues["MODE"]]), "Sensor: "+ str(33333))
    
    def updateDisplayedModeValue(self):
        self.lcd1602visualisation.debugDisplay(self.configValues["MODE"], str(self.valueManager.values[self.configValues["MODE"]]))
    
    def updateDisplayedMode(self):
        self.lcd1602visualisation.debugDisplay("Mode:",self.configValues["MODE"])
    
    def visualiseWateringActivity(self):
        self.lcd1602visualisation.debugDisplay("Watering", "...-'`´'-...")
        
   