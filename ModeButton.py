from Button import Button

class ModeButton (Button):
    
    VALID_MODES = ["SET_WATERING_TIME", "SET_THRESHOLD", "ACTIVATE_WATERING_MODE"]
    
    def __init__ (self, btnType, pin, mode):
        try:
            if mode in self.VALID_MODES:
                self.MODE = mode
            else:
                raise Exception('Provided MODE (' +str(mode)+ ') does not exist!')
        except ValueError as ve:
            print('ERROR: ' + repr(ve))
        super().__init__(btnType,pin)
        
    def getMode(self):
        return self.MODE
    