from activity import activity

from time import sleep_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

'''
Meant to be used as visualisation of sensor data. 
Currently only used to write sensor data in a file.

Implements Activity -> Is an Observer.A
'''
class LCD1602Visualisation ():
    
    datapoints = []
    data = "-boot-"
    i2c = ()
    lcd = ()
    
    # Configuration values for 1620 LCD
    i2c_address = 0x27
    lcd_num_lines = 2
    lcd_num_columns = 16

    threshold = 0
    
    def __init__ (self,sdaPin, sclPin, frequency):
        
        #DEBUG
        pass
        #DEBUG
        
        # Initialization I2C at given I2C port
        ### self.i2c= I2C(0, sda=Pin(sdaPin), scl=Pin(sclPin), freq=frequency)
        # Initialization LCD via I2C
        ### self.lcd = I2cLcd(self.i2c, i2c_address, lcd_num_lines, lcd_num_columns)
    
    def update(self, sensor):
        if sensor.getName() == "MOISTURESENSOR":
            self.data = sensor.value # The latest piece of data the sensor has measured.
            #print("Moisty")
            self.update_lcd()
        elif sensor.getName() == "POTENTIOMETER":
            self.threshold = sensor.threshold # The threshold value set by
            #print("Ponti")
            self.update_lcd()
        else:
            print ("ERROR - no value has been transmitted") 

    def update_lcd(self):
        # Display-Zeilen ausgeben
        self.lcd.clear()        
        self.lcd.putstr("Sensor: "+ str(self.data) + "\n")
        self.lcd.putstr("Thresh: "+ str(self.threshold))
        #print("Sleep update")
        sleep_ms(1000)
     
    def destroy_LCD(self):
        self.lcd.display_off()
        sleep_ms(3000)
