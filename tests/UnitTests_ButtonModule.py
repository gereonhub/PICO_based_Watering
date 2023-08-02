from Button import Button
from button_event_manager import ButtonEventManager
from io_manager import IOManager

def runButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

if __name__ == '__main__':   # Program entrance
    
    print(ButtonType().getButtonTypes())
    ioManager = IOManager()
    bev = ButtonEventManager(ioManager.getConfigObject())
    bev.setupButtons()
    for button in bev.buttonList:
        runButtonTest (button)

    
    while (True):
        pass