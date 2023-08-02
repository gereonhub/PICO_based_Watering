
class Logger ():
    
    def __init__(self, debug):
        self.debug = debug
    
    def log(self, logMessage):
        if self.debug:
            print("DEBUG: " + str(logMessage))            
    
    def info(self, infoMessage):
        print("INFO: " + str(infoMessage))
        
    def error(self, errorMessage):
        print("ERROR: " + str(errorMessage))