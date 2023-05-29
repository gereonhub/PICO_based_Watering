
class ButtonType:
    
    buttonTypes = {
        "down":"DOWN_BUTTON",
        "up":"UP_BUTTON",
        "setMode":"SETMODE_BUTTON",
        "watering":"WATERING_BUTTON",
        "none":"NONE"
        }

    def __init__ (self):
        pass
    
    def getButtonTypes (cls):
        return cls.buttonTypes