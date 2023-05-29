'''
Abstract class for observer pattern.
Subject: The object that is being observed. Able to inform all its subscribers, if something happens.
Observer: Object that waits for updates from the object it observes...

'''
class Subject:

    #observer list
    activities = [] #todo:rename this
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


class Observer:
    
    def __init__ (self):
        pass
    
    #Override
    def update(self, data):
        pass