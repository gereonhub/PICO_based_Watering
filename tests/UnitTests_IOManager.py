from io_manager import io_manager

if __name__ == '__main__':   # Program entrance
    iom = io_manager()
    values = iom.get_config_values()
    minmax = iom.get_min_max_values()
    modeType = iom.get_types_and_modes()
    print (values["MOISTURE_SENSOR_INITIAL_IGNORE"])
    print (minmax["MOISTURE_SENSOR_INITIAL_IGNORE"])
    print (modeType["MODE"])
    print (minmax)
    
    
    