from Observer import Subject
from Observer import Observer
from buttonType import ButtonType
from DownButton import DownButton
from UpButton import UpButton
from WateringButton import WateringButton
from ModeButton import ModeButton

'''
- Has information about all Buttons that exist in the system
- Collects all GPIO pin information, checks for duplicates and provides pin information for global check in control class
- Gets notified by button_pressed events
- Informs the activities that are meant to be triggered by an event (to reduce traffic it implements an Observer pattern).
'''
class ButtonEventManager(Observer, Subject):
    
    def __init__(self):
        Observer.__init__(self)
        Subject.__init__(self)
        
    
    def setupButtons(self): #todo how to store these values in a config file
        self.downButton = DownButton (ButtonType().getButtonTypes()["down"], 2, 50)
        self.downButton.attach(self)
        self.downButton.setupButton()
        self.upButton = UpButton (ButtonType().getButtonTypes()["up"], 3, 50)
        self.upButton.attach(self)
        self.upButton.setupButton()
        self.modeButton = ModeButton (ButtonType().getButtonTypes()["setMode"], 4, "ACTIVATE_WATERING_MODE")
        self.modeButton.attach(self)
        self.modeButton.setupButton()
        self.wateringButton = WateringButton (ButtonType().getButtonTypes()["watering"], 5)
        self.wateringButton.attach(self)
        self.wateringButton.setupButton()
    
    def update (self, button):
        print("BUTTON UPDATE TRIGGERED")
        if button.getButtonType() == ButtonType().getButtonTypes()["down"]:
            print ("Runter") #todo Implement action
        elif button.getButtonType() == ButtonType().getButtonTypes()["up"]:
            print ("Hoch")#todo Implement action
        elif button.getButtonType() == ButtonType().getButtonTypes()["setMode"]:
            print ("Modus")#todo Implement action
        elif button.getButtonType() == ButtonType().getButtonTypes()["watering"]:
            print ("Wässern")#todo Implement action
            self.notify()
        else:
            print ("NONE")#todo Implement action
    