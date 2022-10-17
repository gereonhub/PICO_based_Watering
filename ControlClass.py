#import RPi.GPIO as GPIO
import machine
from PumpActivity import PumpActivity
from PotentiometerSensor import PotentiometerSensor
from MoistureSensor import MoistureSensor
import utime


class Controller:

    run = True
    pinOverview = []   

    def __init__(self, sensoren, activities, visualisation):
        self.sensoren = sensoren
        self.activities = activities
        self.visualisation = visualisation
    
    """
    Iterate over all activitites (there might be more than one) and make sure that every pin
    is used only once.
    If this test passes - start all activities
    """
    def setupActivities(self):
        for pin in self.activities[0].getLedPinNumber():
            if not pin in self.pinOverview:
                self.pinOverview.append(pin)
                self.activities[0].start()
            else:
                print("ERROR --- LEDPIN already in use")
    
    def manualButtonListener(self):
        print("****************mBL()")
        self.activities[0].manualWatering()
    
    def operate(self):        
        while self.run: 
            for x in self.sensoren:
                x.readValues()
            utime.sleep(0.5)
    
    def destroy(self):
        for a in self.activities:
            a.stop()
        #self.visualisation.destroy_LCD()
        #GPIO.cleanup()


        
        
