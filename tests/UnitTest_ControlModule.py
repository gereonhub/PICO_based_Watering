from controlModule import ControlModule

if __name__ == '__main__':   # Program entrance
    controlModule = ControlModule()
    controlModule.setupManagers()
    controlModule.establishManagerConnections()
    controlModule.sensorDM.update(controlModule.sensorDM.moistureSensor)
    controlModule.startMainThread()