from Button import Button

class DownButton (Button):
    
    def __init__ (self, btnType, pin, decrease_by):
        try:
            if decrease_by > 0 and decrease_by < 1000:
                self.DECREASE_BY = decrease_by
            else:
                raise Exception('Provided DECREASE_BY value (' +str(decrease_by)+ ') is invalid!')
        except ValueError as ve:
            print('ERROR: ' + repr(ve))
        super().__init__(btnType,pin)
        
    def getDecreaseByValue(self):
        return self.DECREASE_BY
    
    
