#import RPi.GPIO as GPIO
import machine
import utime
import _thread
#from datetime import datetime
from Activity import Activity


class PumpActivity (Activity):
     
    sensorData = 0
    activityName = "Pump activity"
    
    # Pins used by this activity.
    # !!! New pins must be added to getLedPinNumber() function!!!
    pumpControlPin = 16 # at position 21
    manualButtonPin = 22 # at position 29
    debugPin = 1 # at position 2
    
    #Pin objects
    pumpControlObject = () 
    manualButtonObject = () 
    debugPinObject = ()
    
    threshold = 24000  # Sensor value threshold for this activity. Values are provided by 5V capacitive soil moist sensor.
    sensorSpikeProtectionThreshold = 4 # Sometimes the sensors values will be invalid and might cause unintended watering. A defined number of threshold value exceedances prevents the system from doing so.
    sensorSpikeProtectionCounter = 0 
    pumpActivityTime = 3 # How many seconds to you want the pump to work
    waitStateTime = 120 # After the pump has been active the water needs some time to spread. System needs to wait for a while to avoid excessive watering.
    wait = False # Bolean for wait state
    timeDiff = 0
    
    
    def __init__ (self):
        pass  
    
    # Observer method
    # Receives updates from sensor
    def update(self, sensor):
        if sensor.getName() == "MOISTURESENSOR":
            self.sensorData = sensor.value # The latest piece of data the sensor has measured.
            #debug diod start
            if self.debugPinObject.value():
                self.debugPinObject.value(0)
            else:
                self.debugPinObject.value(1)
            # debug diod end
            self.execute() # Start processing
        elif sensor.getName() == "POTENTIOMETER":
            self.threshold = sensor.threshold # The threshold value set by
        else:
            print ("ERROR - no value has been transmitted")

        
    def getLedPinNumber(self):
        return (self.pumpControlPin, self.manualButtonPin, self.debugPin)
    
    def start(self):
        #Instantiate Pin object for AUTOMATIC pump control
        self.pumpControlObject = machine.Pin(self.pumpControlPin, machine.Pin.OUT)
        self.pumpControlObject.value(0)
        
        #Instantiate Pin object for MANUAL pump control
        self.manualButtonObject = machine.Pin(self.manualButtonPin, machine.Pin.IN, machine.Pin.PULL_UP)
        
        #Instantiate Pin object for debug diod
        self.debugPinObject = machine.Pin(self.debugPin, machine.Pin.OUT)
        self.debugPinObject.value(0)
        
    def execute(self):
        
        # If wait state is still acitve (true if pump has been active recently) don't do anything
        # Wait will be set to false as soon as defined wait period has been exceeded
        if self.wait:
            tempTimeDifference = utime.time() - self.timeDiff            
            if tempTimeDifference > self.waitStateTime:
                self.wait = False
            else:
                print('DEBUG - "Wait" is still active')
                return False
            
        # If sensor data is below the threshold and the sensorSpikeProtectionCounter is satisfied - start watering for the defined amount of time.
        # After the avtivity wait is set to true to start the wait phase
        if self.sensorData > self.threshold:
            if self.sensorSpikeProtectionCounter < self.sensorSpikeProtectionThreshold:
                self.sensorSpikeProtectionCounter+=1
                return False
            else: 
                print('DEBUG - Threshold exceeded. Start watering...')
                self.activatePump()
                utime.sleep(self.pumpActivityTime)
                self.stopPump()            
                self.wait = True
                self.timeDiff  = utime.time()
                self.sensorSpikeProtectionCounter = 0
        else:
            if self.sensorSpikeProtectionCounter > 0:
                self.sensorSpikeProtectionCounter-=1
        utime.sleep(1)

    # Set pump control pin to 1 - start watering process
    def activatePump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pumpControlObject.value(1)
            print('DEBUG - Pump is active!')
    
    # Set pump control pin to 0 - stop warterin process
    def stopPump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pumpControlObject.value(0)
            print('DEBUG - Pump is inactive again!')
            
    # Todo when more than one sensor is used   
    def setName(self, name):
        self.c = name
    
    # Todo when more than one sensor is used   
    def getName(self):
        return self.activityName

    # Method to start watering using the manual button
    def manualWatering (self):
        print("******************PumpAct.mW()")
        while True:
            #utime.sleep(1)
            if not self.manualButtonObject.value():
                if not self.pumpControlObject.value():
                    self.activatePump()
                    utime.sleep(3)
                    self.stopPump()

