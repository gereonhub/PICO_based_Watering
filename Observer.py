'''
Abstract class for observer pattern.
Subject: The object that is being observed. Able to inform all its subscribers, if something happens.
Observer: Object that waits for updates from the object it observes...

'''
class subject:

    value = 0

    def __init__(self):
        self.activities = [] #todo:rename this

    #observer method
    def notify (self):
        print("Observer:Subject: notify() self.activities:"+ str(len(self.activities)))
        for x in self.activities:
            #print(x)
            x.update(self)
    
    #observer method
    def attach (self, activity):
        self.activities.append(activity)
    
    #observer method
    def detach (self, activity):
        self.activities.remove(actitity)


class observer:
    def __init__ (self):
        pass
    
    #Override
    def update(self, data):
        pass
