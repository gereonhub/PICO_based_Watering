from button import Button
from DownButton import DownButton
from UpButton import UpButton
from WateringButton import WateringButton
from ModeButton import ModeButton
from button_event_manager import button_event_manager
from buttonType import ButtonType
from io_manager import io_manager

def runButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

if __name__ == '__main__':   # Program entrance
    
    print(ButtonType().getButtonTypes())
    ioManager = io_manager()
    bev = button_event_manager(ioManager.getConfigObject())
    bev.setup_buttons()
    for button in bev.button_list:
        runButtonTest (button)

    
    while (True):
        pass