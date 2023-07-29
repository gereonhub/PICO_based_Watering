from button import Button
from button_event_manager import button_event_manager
from io_manager import io_manager
from button_event_manager import ButtonEventManager
from io_manager import IOManager

def runButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

if __name__ == '__main__':   # Program entrance
    
    ioManager = io_manager()
    bev = button_event_manager(ioManager.getConfigObject())
    bev.setup_buttons()
    for button in bev.button_list:
        runButtonTest (button)

    
    while (True):
        pass