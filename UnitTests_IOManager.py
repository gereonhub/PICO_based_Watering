from ioManager import IOManager

if __name__ == '__main__':   # Program entrance
    iom = IOManager()
    values = iom.getConfigObject()
    print (values["MOISTURE_SENSOR_INITIAL_IGNORE"])
    
    
    