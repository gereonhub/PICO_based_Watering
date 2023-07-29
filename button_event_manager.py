from observer import subject
from observer import observer
from button import Button

'''
General 
- Creates all SW Interfaces for HW buttons that can interact with the system
- Gateway function: Listens to all Buttons notifies its subscribers (Observer Pattern in both directions)

Todos:
- #todo Sanity check: Collect all GPIO pin information, check for duplicates and provides pin information for global check in tbd module
- #todo Informs the activities that are meant to be triggered by an event (to reduce traffic it implements an Observer pattern).
'''
class button_event_manager(observer, subject):
    
    buttonList = []
    #Stores the type of button that has triggered the current event to be used by subscribers 
    
    event = "" #IMPORTANT for every Manager class
    
    def __init__(self, values):
        observer.__init__(self)
        subject.__init__(self)
        self.configValues = values
    
    def check_pin_validity (self): #todo
        pass 
    
    '''
    Specific buttons are created using the information stored in the configValues (todo) and are being listened to (Observer pattern)
    '''
    def setup_buttons(self): #todo how to store these values in a config file
        
        for type, values in self.configValues["BUTTONS"].items(): 
            if type == "DOWN_BUTTON":
                downButton = Button (type, values["PIN"])
                self.buttonList.append(downButton)             
            elif type == "UP_BUTTON":
                upButton = Button (type, values["PIN"])
                self.buttonList.append(upButton)                
            elif type == "SETMODE_BUTTON":
                modeButton = Button (type, values["PIN"])
                self.buttonList.append(modeButton)                
            elif type == "WATERING_BUTTON":
                wateringButton = Button (type, values["PIN"])
                self.buttonList.append(wateringButton)                
        for x in self.buttonList:
            x.attach(self)
            x.setupButton()

    '''
    Buttons trigger notify() whenever pressed physically. 
    '''
    def update (self, button):
        print("BEM - update() : BUTTON UPDATE TRIGGERED by " + button.getButtonType())        
        self.event = self.determine_event_type(button)
        self.notify()
        
    def get_event (self):
        return self.event
    
    def determine_event_type(self, button):
        eventType = ""
        if button.getButtonType() == "DOWN_BUTTON":
            eventType = "DECREASE_EVENT"
        elif button.getButtonType() == "UP_BUTTON":
            eventType = "INCREASE_EVENT"             
        elif button.getButtonType() == "SETMODE_BUTTON":
            eventType = "MODE_CHANGE_EVENT"                
        elif button.getButtonType() == "WATERING_BUTTON":
            eventType = "WATERING_EVENT"
        else:
            eventType == "ERROR_NO_EVENT_FOUND"
        return eventType
