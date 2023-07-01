import machine
import _thread

class PumpActivity ():
    
    waitState = False
    
    #Pin objects
    pumpControlObject = ()
    
    def __init__(self, pin):
        self.pumpControlPin = 16 # at position 21 

    # Observer method
    def update(self):
        pass
    
    def initializePinObject(self):
        #Instantiate Pin object for AUTOMATIC pump control
        self.pumpControlObject = machine.Pin(self.pumpControlPin, machine.Pin.OUT)
        self.pumpControlObject.value(0)

    # Set pump control pin to 1 - start watering process
    def activatePump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pumpControlObject.value(1)
            print('DEBUG - Pump is active!')#todo delete - debugging
    
    # Set pump control pin to 0 - stop warterin process
    def stopPump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pumpControlObject.value(0)
            print('DEBUG - Pump is inactive again!')#todo delete - debugging
    
    def setWaitState (self, state):
        self.waitState = state
        
    def getWaitState (self):
        return self.waitState
    
    def getCurrentValue (self):
        return self.pumpControlObject.value()
