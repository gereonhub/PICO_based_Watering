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
    data = 0
    i2c = ()
    lcd = ()
    threshold = 0
    
    def __init__ (self):
        # Initialisierung I2C
        self.i2c= I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)
        # Initialisierung LCD über I2C
        self.lcd = I2cLcd(self.i2c, 0x27, 2, 16)
        self.lcd.putstr("Initializing...")
    
    def update(self, sensor):
        if sensor.getName() == "MOISTURESENSOR":
            self.data = sensor.value # The latest piece of data the sensor has measured.
        elif sensor.getName() == "POTENTIOMETER":
            self.threshold = sensor.threshold # The threshold value set by
        else:
            print ("ERROR - no value has been transmitted")
        #print(sensor.threshold) # checked - works
        print ("Moisturesensor : "+ str(self.data)+ " Ponti: " + str(self.threshold) )
        self.update_LCD()
        

    def update_LCD(self):
        # Display-Zeilen ausgeben
        self.lcd.clear()        
        self.lcd.putstr("Sensor: "+ str(self.data) + "\n")
        self.lcd.putstr("Thresh: "+ str(self.threshold))
        #sleep_ms(500)
     
    def destroy_LCD(self):
        self.lcd.display_off()
        sleep_ms(3000)
  
    
