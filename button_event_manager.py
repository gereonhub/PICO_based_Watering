from observer import subject
from observer import observer
from button import button

'''
General 
- Creates all SW Interfaces for HW buttons that can interact with the system
- Gateway function: Listens to all Buttons notifies its subscribers (Observer Pattern in both directions)

Todos:
- #todo Sanity check: Collect all GPIO pin information, check for duplicates and provides pin information for global check in tbd module
- #todo Informs the activities that are meant to be triggered by an event (to reduce traffic it implements an Observer pattern).
'''
class button_event_manager(observer, subject):
    
    button_list = []
    #Stores the type of button that has triggered the current event to be used by subscribers 
    
    event = "" #IMPORTANT for every Manager class
    
    def __init__(self, values):
        observer.__init__(self)
        subject.__init__(self)
        self.config_values = values
    
    def check_pin_validity (self): #todo
        pass 
    
    '''
    Specific buttons are created using the information stored in the configValues (todo) and are being listened to (Observer pattern)
    '''
    def setup_buttons(self): #todo how to store these values in a config file
        
        for type, values in self.config_values["BUTTONS"].items(): 
            if type == "DOWN_BUTTON":
                down_button = button (type, values["PIN"])
                self.button_list.append(down_button)             
            elif type == "UP_BUTTON":
                up_button = button (type, values["PIN"])
                self.button_list.append(up_button)                
            elif type == "SETMODE_BUTTON":
                mode_button = button (type, values["PIN"])
                self.button_list.append(mode_button)                
            elif type == "WATERING_BUTTON":
                watering_button = button (type, values["PIN"])
                self.button_list.append(watering_button)                
        for x in self.button_list:
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
        event_type = ""
        if button.get_button_type() == "DOWN_BUTTON":
            event_type = "DECREASE_EVENT"
        elif button.get_button_type() == "UP_BUTTON":
            event_type = "INCREASE_EVENT"             
        elif button.get_button_type() == "SETMODE_BUTTON":
            event_type = "MODE_CHANGE_EVENT"                
        elif button.get_button_type() == "WATERING_BUTTON":
            event_type = "WATERING_EVENT"
        else:
            event_type == "ERROR_NO_EVENT_FOUND"
        return event_type
