import machine
import _thread

class pump_activity ():

    wait_state = False
    
    #Pin objects
    pump_control_object = ()
    
    def __init__(self, pin):
        self.pumpControlPin = pin # usually PIN 16 at position 21
        
    def initialize_pin_object(self):
        #Instantiate Pin object for AUTOMATIC pump control
        self.pump_control_object = machine.Pin(self.pumpControlPin, machine.Pin.OUT)
        self.pump_control_object.value(0)

    # Set pump control pin to 1 - start watering process
    def activate_pump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pump_control_object.value(1)
            print('DEBUG - Pump is active!')#todo delete - debugging
    
    # Set pump control pin to 0 - stop warterin process
    def stop_pump(self):
        lock = _thread.allocate_lock()
        with lock:
            self.pump_control_object.value(0)
            print('DEBUG - Pump is inactive again!')#todo delete - debugging
    
    def set_wait_state (self, state):
        self.wait_state = state
        
    def get_wait_state (self):
        return self.wait_state
    
    def get_current_value (self):
        return self.pump_control_object.value()
