from Button import Button
from modeType import ModeType

class ModeButton (Button):
    
    def __init__ (self, btnType, pin, mode):
        try:
            if mode in ModeType().getModeTypes().values():
                self.MODE = mode
            else:
                raise Exception('Provided MODE (' +str(mode)+ ') does not exist!')
        except ValueError as ve:
            print('ERROR: ' + repr(ve))
        super().__init__(btnType,pin)
        
    def getMode(self):
        return self.MODE
    