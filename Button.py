from machine import Pin
from Observer import Subject
from time import sleep_ms
import sys

class Button (Subject):
    
    waitAfterPressed = False
   
    VALID_GPIO_PINS = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,26,27,28] #todo should be in config file
    
    '''
    Instanciate the class by providing its name and the GPIO pin. PIN availability needs to be checked in caller class.
    name has to be a membe of Buttontype dictionary #todo find alternative for proper enum class here.
    '''
    def __init__(self, btnType, pin):
        try:
            if pin not in self.VALID_GPIO_PINS:
                raise Exception('GPIO pin provided (' +str(pin)+ ') is invalid!')
            self.GPIO_PIN = pin

            #if btnType not in ButtonType().getButtonTypes().values():
            #    raise Exception('Name provided (' +str(btnType)+ ') is not a valid ButtonType name!')
            self.TYPE = btnType
        except ValueError as ve:
            print('ERROR: ' + repr(ve) + " - Program terminated.")
            sys.exit()
        super().__init__()
    '''
    Method defined to handle button event that is triggered when pressed (GPIO Event).
    Calls notify() which is defined in parent class Subject from Observer module
    '''
    def buttonHandler (self, pin):
        print("Button class:" + str(self.getButtonType()) + " has been pressed and is notifying its subscribers")
        sleep_ms(100)
        self.notify()
    
    def setupButton(self):
        self.buttonObject = Pin(self.GPIO_PIN, Pin.IN, Pin.PULL_UP)
        self.buttonObject.value(0) # check ob nötig?
        # Button interrupt
        self.buttonObject.irq(trigger=Pin.IRQ_FALLING, handler=self.buttonHandler)
        
    def getButtonState (self):
        return self.buttonObject.value()
    
    def getButtonType (self):
        return self.TYPE

        