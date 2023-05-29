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
        pass
    
    def setUpButtons(self):
        self.downButton = DownButton (ButtonType().getButtonTypes()["down"], 2, 50)
        self.downButton.attach(self)
        self.upButton = UpButton (ButtonType().getButtonTypes()["up"], 3, 50)
        self.upButton.attach(self)
        self.modeButton = ModeButton (ButtonType().getButtonTypes()["setMode"], 4, "ACTIVATE_WATERING_MODE")
        self.modeButton.attach(self)
        self.wateringButton = WateringButton (ButtonType().getButtonTypes()["watering"], 5)
        self.wateringButton.attach(self)
    
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
        else:
            print ("NONE")#todo Implement action
    