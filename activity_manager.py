import utime

from observer import observer, subject
from pump_activity import pump_activity
from visualisation import LCD1602Visualisation

'''
Responsible to instanciate and control the Activities
'''
class activity_manager (observer, subject) :
    
    last_watering_activity = 0
    
    #MoistureSensor -> mose
    mose_data = 5 # todo 5 only for debug reason. should be 0
    mose_spike_protection_counter = 0 
    

    '''
    ConfigValues is the reference to the valueManager object #todo should be a singleton
    '''    
    def __init__(self, value_manager_object):
        self.config_values = value_manager_object.values
        self.value_manager = value_manager_object
        observer.__init__(self)
        subject.__init__(self)


    def setup_activities(self):
        # Pump
        self.pump_activity_object = pump_activity(self.config_values["PIN_PUMP_ACTIVITY"])
        self.pump_activity_object.initialize_pin_object()
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
            self.set_mode()
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
    def adjust_mode_parameters (self, up_down_flag):
        print("AM - adjustModeParameters(): Current Mode: "+self.config_values["MODE"])
        print("AM - adjustModeParameters(): Current Mode Value: "+str(self.config_values[self.config_values["MODE"]]))
        #1. get current value of MODE/Category
        #2. increase/decrease value (usually +/-1, except for WATERING_THRESHOLD)
        #3. try to set value in ValueManager
        temp_mode_value = self.config_values[self.config_values["MODE"]]
        if self.config_values["MODE"] == "WATERING_THRESHOLD":
            if up_down_flag == "UP":
                temp_mode_value += self.config_values["WATERING_THRESHOLD_UP_DOWN_VALUE"]
            if up_down_flag == "DOWN":
                temp_mode_value -= self.config_values["WATERING_THRESHOLD_UP_DOWN_VALUE"]
        else:
            if up_down_flag == "UP":
                temp_mode_value +=1
            if up_down_flag == "DOWN":
                temp_mode_value -=1
                
        if self.value_manager.set_value(self.config_values["MODE"], temp_mode_value):
            #todo implement LCD output
            print("Value has been changed")
        print("AM - adjustModeParameters(): NEW Mode Value: "+ str(self.config_values[self.config_values["MODE"]]))
        
    def set_mode (self):
        print("AM - setMode(): Current Mode: " + self.config_values["MODE"])
        if self.value_manager.toggleMode():
            print("Mode has been changed")
        else:
            print("ERROR Value has NOT been changed")
    
    
    #-----------------------------------------------------------------------------------
    #-------------------------------Pump Control methods--------------------------------
    
    def manual_pump_control(self):
        if self.pump_activity_object.get_current_value():
            return
        else:
            self.pump_activity_object.activate_pump()
            utime.sleep(self.config_values["WATERING_TIME"])
            self.pump_activity_object.stop_pump()
    
    def automaticPumpControl (self):
        '''
        If wait state is still active (true if pump has been active recently)
        no automatic watering is possible. pumpActivityObject.getWaitState will
        be set to false as soon as defined waiting time period has been exceeded.
        '''
        if self.pump_activity_object.get_wait_state():
            wait_state_time_difference = utime.time() - self.last_watering_activity            
            if wait_state_time_difference <= self.config_values["WATERING_WAIT_TIME"]:
                print('DEBUG - "Wait" is still active') #todo delete - debugging
                return False
            self.wait = False
        print ('AM - automaticPumpControl: not waiting') #todo delete - debugging 
        
        '''
        If sensor data is below the threshold and the moseSpikeProtectionCounter is satisfied
        start watering for the defined amount of time. After the avtivity wait is set to true
        to start the wait phase
        '''
        print("AM - automaticPumpControl(): Sensor data versus threshold: "+str(self.mose_data) +".>."+str(self.config_values["WATERING_THRESHOLD"])) #todo delete debugging
        if self.mose_data > self.config_values["WATERING_THRESHOLD"]:
            print(str(self.mose_spike_protection_counter) + ".<." + str(self.config_values["MOISTURE_SENSOR_SPIKE_PROTECTION"])) #todo delete debugging
            if self.mose_spike_protection_counter < self.config_values["MOISTURE_SENSOR_SPIKE_PROTECTION"]:
                self.mose_spike_protection_counter += 1
                return False
            # else überflüssig - Du hast ein return drin, im if-Fall
            print('DEBUG - Threshold exceeded. Start watering...') #todo delete - debugging
            self.pump_activity_object.activate_pump()
            utime.sleep(self.config_values["WATERING_TIME"])
            self.pump_activity_object.stop_pump()           
            self.pump_activity_object.set_wait-state(True)
            self.last_watering_activity = utime.time()
            self.mose_spike_protection_counter = 0
        else:
            if self.mose_spike_protection_counter > 0:
                self.mose_spike_protection_counter-=1
        utime.sleep(1)
        
    #-----------------------------------------------------------------------------------
    #-------------------------------Visualisation methods-------------------------------
        
    def updateDisplayedSensorValue():
        pass
    
    def updateDisplayedModeValue():
        pass
    
    def updateDisplayedMode():
        pass
    
    def visualiseWateringActivity():
        pass
        
   