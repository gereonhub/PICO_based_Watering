from machine import Pin
import _thread
import time

MODE = True

def setMode(bool):
    global Mode
    MODE = bool
    print("Mode ist jetzt: "+ str(MODE))

def doStuff():
    global MODE
    while (True):
        print("Doing Stuff in Thread 1. Mode is: "+ str(MODE))
        time.sleep(1)
        
def doOtherStuff():
    global MODE
    while (True):
        print("Doing Stuff in Thread 2. Mode is: "+ str(MODE))
        time.sleep(1)

def button_handler(pin):
    global MODE
    if MODE:
        MODE = False
    else:
        MODE = True    
    
if __name__ == '__main__':
    #Mode = True
    try:
        btn = Pin(2, Pin.IN, Pin.PULL_UP)
        print("1")
        btn.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
        print("2")
        thread2 = _thread.start_new_thread(doStuff, ())
        print("3")
        doOtherStuff()
    except:
        print("Exception!!!")
    
