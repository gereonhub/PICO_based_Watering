from Activity import Activity
from time import sleep_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

'''
Meant to be used as visualisation of sensor data. 
Currently only used to write sensor data in a file.

Implements Activity -> Is an Observer.A
'''
class Visualisation (Activity):
    
    datapoints = []
    data = "-boot-"
    i2c = ()
    lcd = ()
    threshold = 0
    
    def __init__ (self):
        # Initialisierung I2C
        self.i2c= I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)
        # Initialisierung LCD über I2C
        self.lcd = I2cLcd(self.i2c, 0x27, 2, 16)
        #self.lcd.clear()        
        #self.lcd.putstr("Initializing...")
    
    def update(self, sensor):
        if sensor.getName() == "MOISTURESENSOR":
            self.data = sensor.value # The latest piece of data the sensor has measured.
            #print("Moisty")
            self.update_LCD()
        elif sensor.getName() == "POTENTIOMETER":
            self.threshold = sensor.threshold # The threshold value set by
            #print("Ponti")
            self.update_LCD()
        else:
            print ("ERROR - no value has been transmitted") 

    def update_LCD(self):
        # Display-Zeilen ausgeben
        self.lcd.clear()        
        self.lcd.putstr("Sensor: "+ str(self.data) + "\n")
        self.lcd.putstr("Thresh: "+ str(self.threshold))
        #print("Sleep update")
        sleep_ms(1000)
     
    def destroy_LCD(self):
        self.lcd.display_off()
        sleep_ms(3000)
  
    
