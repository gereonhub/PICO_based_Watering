from controlModule import control_module

if __name__ == '__main__':   # Program entrance
    controlModule = control_module()
    controlModule.setupManagers()
    controlModule.establishManagerConnections()
    controlModule.sensorDM.update(controlModule.sensorDM.moistureSensor)
    while (True):
        pass