# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from abc import ABC, abstractmethod
import time
import sys

# Abstract class - every algorithm must implement the getName() method
class Algorithm(ABC):     

    def __init__(self, dataModel) -> None:
        self.__dataModel = dataModel

    @abstractmethod
    def getName(self): pass 

    def delay(self):
        interval = self.__dataModel.getDelay() / 10
        i = 0 
        while(i < self.__dataModel.getDelay()):
            self.__stopCheck() 
            # Checks if the GUI thread is holding the pause lock
            if(self.__dataModel.isPaused()): self.__pauseAlgorithm()
            time.sleep(interval) 
            i += interval
    
    # Used to check is the algorithm needs to halt
    def __stopCheck(self): 
        # Checks if the algorithm needs to stop
        if(self.__dataModel.isStopped()): 
            # Output message confirming thrad termination
            print("Algorithm Thread has terminated safely") 
            # Exit thread
            sys.exit() 
    
    def __pauseAlgorithm(self):
        # Attempts to acquire lock, pausing the thread
        self.__dataModel.acquireLock()
        # If the lock is not released then the GUI thread freezed next time pause is pressed
        self.__dataModel.releaseLock()

    # Sort and display array on screen
    def sortArray(self):
        self.__dataModel.sortArray()
        self.__dataModel.updateArrayOnScreen()
        self.delay() 
    
    # Shuffle and display array on screen
    def shuffleArray(self):
        self.__dataModel.shuffleArray()
        self.__dataModel.updateArrayOnScreen()
        self.delay()  
    
    # Refreshes screen to display any changes to the array
    def updateArrayOnScreen(self):
        self.__dataModel.updateArrayOnScreen() 
    
    # Returns array
    def getArray(self):
        return self.__dataModel.getArray()
    
    # Returns the target
    def getTarget(self):
        return self.__dataModel.getTarget() 
    
    # Change colour of bar at specified index to colour given
    def changeBarColour(self, index : int, colour : str):
        self.__dataModel.setBarColour(index, colour)
    
    # Used to check constructor implementation
    def getDataModel(self):
        return self.__dataModel
# Listen to American Idiot by Green Day