from Button import Button
from DownButton import DownButton
from UpButton import UpButton
from WateringButton import WateringButton
from ModeButton import ModeButton
from ButtonEventManager import ButtonEventManager
from buttonType import ButtonType

def runButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

def runDownButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    print(testButton.getDecreaseByValue())
    return True

def runWateringButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

def runUpButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    print(testButton.getIncreaseByValue())
    return True

def runModeButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    print(testButton.getMode())
    return True

if __name__ == '__main__':   # Program entrance
    
    '''
    downButton = DownButton ("Holger", 2, 100)
    runDownButtonTest (downButton)
    
    upButton = UpButton ("Pedro", 3, 50)
    runUpButtonTest (upButton)
    
    modeButton = ModeButton ("Moody", 4, "ACTIVATE_WATERING_MODE")
    runModeButtonTest (modeButton)
    
    wateringButton = WateringButton ("Watery", 5)
    runWateringButtonTest (wateringButton)
    '''
    
    print(ButtonType().getButtonTypes())
    
    bev = ButtonEventManager()
    bev.setupButtons()
    runDownButtonTest (bev.downButton)
    runUpButtonTest (bev.upButton)
    runModeButtonTest (bev.modeButton)
    runWateringButtonTest (bev.wateringButton)
    
    while (True):
        pass

    '''
    print("*** *** *** BUTTON class")
    testButton = Button ("Holger", 5)
    if runButtonTest(testButton):
        print("passed")
    #testButton = Button ("Peter", -8)
    #if runDownButtonTest(testButton):
    #    print("passed")
    #testButton = Button ("Peter", 500)
    #if runDownButtonTest(testButton):
    #   print("passed")        
    '''
    '''
    print("*** *** *** DOWNBUTTON class")
    testButton = DownButton ("Holger", 2, 100)
    if runDownButtonTest(testButton):
        print("passed")
        while (True):
            pass
    #testButton = DownButton ("Peter", 5, -100)
    #if runDownButtonTest(testButton):
    #    print("passed")
    #testButton = DownButton ("Peter", 5, 1001)
    #if runDownButtonTest(testButton):
    #    print("passed")
    '''
    '''
    print("*** *** *** WATERINGBUTTON class")
    testButton = WateringButton ("Holger", 5)
    if runWateringButtonTest(testButton):
        print("passed")
    #testButton = WateringButton ("Holger", -1)
    #if runWateringButtonTest(testButton):
    #    print("passed")
 
    print("*** *** *** UPBUTTON class")
    testButton = UpButton ("Holger", 5, 100)
    if runUpButtonTest (testButton):
        print("passed")
    #testButton = UpButton ("Peter", 5, -100)
    #if runUpButtonTest (testButton):
    #    print("passed")
    #testButton = UpButton ("Peter", 5, 1001)
    #if runUpButtonTest (testButton):
    #    print("passed")
    '''   



    
