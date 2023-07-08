

class ModeType ():
    modeTypes = { 
    "setWateringTime":"SET_WATERING_TIME",
    "setWateringThreshold":"SET_THRESHOLD",
    "setWateringMode":"ACTIVATE_WATERING_MODE", #Other modes stop watering mechanism. This mode restarts the automated routine.
    "none":"DEFAULT"
        }

    def __init__ (self):
        pass
    
    def getModeTypes (cls):
        return cls.modeTypes