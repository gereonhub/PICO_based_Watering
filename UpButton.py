from Button import Button

class UpButton (Button):
    
    def __init__ (self, btnType, pin, increase_by):
        try:
            if increase_by > 0 and increase_by < 1000:
                self.INCREASE_BY = increase_by
            else:
                raise Exception('Provided INCREASE_BY value (' +str(increase_by)+ ') is invalid!')
        except ValueError as ve:
            print('ERROR: ' + repr(ve))
        super().__init__(btnType,pin)
        
    def getIncreaseByValue(self):
        return self.INCREASE_BY
    