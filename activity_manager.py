import utime

from Observer import Observer, Subject
from pump_activity import PumpActivity
from Visualisation import LCD1602Visualisation
from logger import Logger

'''
Responsible to instanciate and control the Activities
'''
class ActivityManager (Observer, Subject) :
    
    lastWateringActivity = 0
    
    #MoistureSensor -> mose
    moseData = 5 # todo 5 only for debug reason. should be 0
    moseSpikeProtectionCounter = 0 
    

    '''
    values is the reference to the valueManager object #todo should be a singleton
    '''    
    def __init__(self, valueManagerObject, logger):
        self.logger = logger
        self.values = valueManagerObject.values
        self.valueManager = valueManagerObject
        Observer.__init__(self)
        Subject.__init__(self)


    def setupActivities(self):
        # Pump
        self.pumpActivityObject = PumpActivity(self.values["PIN_PUMP_ACTIVITY"])
        self.pumpActivityObject.initializePinObject()
        # LCD 1602
        self.lcd1602visualisation = LCD1602Visualisation(self.values["PIN_LCD_I2C_SDA"],self.values["PIN_LCD_I2C_SCL"], self.values["FREQ_LCD_1602"],self.logger)
         #todo Communication


    def update (self, data):
        if data.getEvent() == "DECREASE_EVENT":     
            self.logger.log ("AM - update(): DECREASE_EVENT")
            self.adjustModeParameters("DOWN")
            self.updateDisplayedValueOfMode()
        elif data.getEvent() == "INCREASE_EVENT":
            self.logger.log ("AM - update(): INCREASE_EVENT")
            self.adjustModeParameters("UP")
            self.updateDisplayedValueOfMode()
        elif data.getEvent() == "MODE_CHANGE_EVENT":
            self.logger.log ("AM - update(): MODE_CHANGE_EVENT")
            self.setMode()
            self.updateDisplayedMode()
        elif data.getEvent() == "WATERING_EVENT":
            self.logger.log ("AM - update(): WATERING_EVENT")
            self.manualPumpControl()
            self.visualiseWateringActivity()
        elif data.getEvent() == "MOISTURE_SENSOR_VALUE_EVENT":
            self.logger.log ("AM - update(): MOISTURE_SENSOR_VALUE_EVENT")
            #todo how to get the actual SensorData through? 
            self.automaticPumpControl()
            self.updateDisplayedSensorValue()
        else:
            self.logger.error ("AM - update() - NONE... event value is unknown")


    #-----------------------------------------------------------------------------------
    #-------------------------------Set Mode methods-----------------------------------
    def adjustModeParameters (self, upDownFlag):
        self.logger.log("AM - adjustModeParameters(): Current Mode: "+self.values["MODE"])
        self.logger.log("AM - adjustModeParameters(): Current Mode Value: "+str(self.values[self.values["MODE"]]))
        #1. get current value of MODE/Category
        #2. if: normal (Tresh/sensorValue) view - do nothing and return
        #   else: increase/decrease value (usually +/-1, except for WATERING_THRESHOLD)
        #3. try to set value in ValueManager
        if self.values["MODE"] == "STANDARD_SENSOR_AND_THRESH_VIEW":
            return
        tempModeValue = self.values[self.values["MODE"]]
        if self.values["MODE"] == "WATERING_THRESHOLD":
            if upDownFlag == "UP":
                tempModeValue += self.values["WATERING_THRESHOLD_UP_DOWN_VALUE"]
            if upDownFlag == "DOWN":
                tempModeValue -= self.values["WATERING_THRESHOLD_UP_DOWN_VALUE"]
        else:
            if upDownFlag == "UP":
                tempModeValue +=1
            if upDownFlag == "DOWN":
                tempModeValue -=1
                
        if self.valueManager.setValue(self.values["MODE"], tempModeValue):
            #todo implement LCD output
            self.logger.log("AM - Value has been changed")
        self.logger.log("AM - adjustModeParameters(): NEW Mode Value: "+ str(self.values[self.values["MODE"]]))
        
    def setMode (self):
        self.logger.log("AM - setMode(): Current Mode: "+self.values["MODE"])
        if self.valueManager.toggleMode():
            self.logger.log("AM - Mode has been changed")
        else:
            self.logger.log("ERROR Value has NOT been changed")
    
    
    #-----------------------------------------------------------------------------------
    #-------------------------------Pump Control methods--------------------------------
    
    def manualPumpControl(self):
        if self.pumpActivityObject.getCurrentValue():
            return
        else:
            self.pumpActivityObject.activatePump()
            utime.sleep(self.values["WATERING_TIME"])
            self.pumpActivityObject.stopPump()
            # Restore standard view after watering
            self.setStandardViewOnDisplay()
            
    
    def automaticPumpControl (self):
        '''
        If wait state is still active (true if pump has been active recently)
        no automatic watering is possible. pumpActivityObject.getWaitState will
        be set to false as soon as defined waiting time period has been exceeded.
        '''
        if self.pumpActivityObject.getWaitState():
            waitStateTimeDifference = utime.time() - self.lastWateringActivity            
            if waitStateTimeDifference <= self.values["WATERING_WAIT_TIME"]:
                self.logger.log('AM - automaticPumpControl() "Wait" is still active') #todo delete - debugging
                return False
            self.wait = False
        self.logger.log ('AM - automaticPumpControl(): not waiting') #todo delete - debugging 
        
        '''
        If sensor data is below the threshold and the moseSpikeProtectionCounter is satisfied
        start watering for the defined amount of time. After the avtivity wait is set to true
        to start the wait phase
        '''
        self.logger.log("AM - automaticPumpControl(): Sensor data versus threshold: "+str(self.moseData) +".>."+str(self.values["WATERING_THRESHOLD"])) #todo delete debugging
        if self.moseData > self.values["WATERING_THRESHOLD"]:
            self.logger.log(str(self.moseSpikeProtectionCounter) + ".<." + str(self.values["MOISTURE_SENSOR_SPIKE_PROTECTION"])) #todo delete debugging
            if self.moseSpikeProtectionCounter < self.values["MOISTURE_SENSOR_SPIKE_PROTECTION"]:
                self.moseSpikeProtectionCounter+=1
                return False
            # Make sure display shows Sensor and Threshold value when watering starts.
            if self.values["MODE"] != "STANDARD_SENSOR_AND_THRESH_VIEW":
                self.setStandardViewOnDisplay()
            self.logger.log('AM - automaticPumpControl() - Threshold exceeded. Start watering...')#todo delete - debugging
            self.pumpActivityObject.activatePump()
            utime.sleep(self.values["WATERING_TIME"])
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
        self.lcd1602visualisation.debugDisplay("Thresh: " + str(self.valueManager.values[self.values["MODE"]]), "Sensor: "+ str(self.values["CURRENT_SENSOR_VALUE"]))
        # todo: as soon as LCD is in place - switch to this method ´:
        #self.lcd1602visualisation.update_sensor_value(self.values["CURRENT_SENSOR_VALUE"])
    
    def updateDisplayedValueOfMode(self):
        self.lcd1602visualisation.debugDisplay(self.values["MODE"], str(self.valueManager.values[self.values["MODE"]]))
    
    def updateDisplayedMode(self):
        if self.values["MODE"] == "STANDARD_SENSOR_AND_THRESH_VIEW":
            self.setStandardViewOnDisplay()
        else:
            self.lcd1602visualisation.debugDisplay("Mode:",self.values["MODE"])
    
    def visualiseWateringActivity(self):
        self.lcd1602visualisation.debugDisplay("Watering", "...-'`´'-...")
        
    def setStandardViewOnDisplay(self):
        self.lcd1602visualisation.debugDisplay("Sensor: " + str(self.values["CURRENT_SENSOR_VALUE"]), "Thresh: "+ str(self.values["WATERING_THRESHOLD"]))
        
   