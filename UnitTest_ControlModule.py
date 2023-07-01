from controlModule import ControlModule

if __name__ == '__main__':   # Program entrance
    controlModule = ControlModule()
    controlModule.setupManagers()
    controlModule.establishManagerConnections()
    while (True):
        pass