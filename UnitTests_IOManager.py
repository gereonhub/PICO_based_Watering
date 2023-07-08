from ioManager import IOManager

if __name__ == '__main__':   # Program entrance
    iom = IOManager()
    values = iom.getConfigValues()
    minmax = iom.getMinMaxValues()
    modeType = iom.getTypesAndModes()
    print (values["MOISTURE_SENSOR_INITIAL_IGNORE"])
    print (minmax["MOISTURE_SENSOR_INITIAL_IGNORE"])
    print (modeType["MODE"])
    print (minmax)
    
    
    