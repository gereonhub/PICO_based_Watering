
#Abstract class for observer

class Sensor:

    #observer list
    activities = []
    value = 0

    def __init__(self):
        pass

    #observer method
    def notify (self):
        for x in self.activities:
            #print(x)
            x.update(self)
    
    #observer method
    def attach (self, activity):
        self.activities.append(activity)
    
    #observer method
    def detach (self, activity):
        self.activities.remove(actitity)
        
    def getName(self):
        return self.NAME
