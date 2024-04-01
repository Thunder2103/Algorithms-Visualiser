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
            self.__dataModel.acquireLock()
            self.__dataModel.releaseLock()
            time.sleep(interval) 
            i += interval
    
    def __stopCheck(self):
        if(self.__dataModel.isStopped()): 
            print("Algorithm Thread has terminated safely")
            sys.exit()
        
    def sortArray(self):
        self.__dataModel.sortArray()
        self.__dataModel.updateArrayOnScreen()
        self.delay() 
    
    def shuffleArray(self):
        self.__dataModel.shuffleArray()
        self.__dataModel.updateArrayOnScreen()
        self.delay(self.__dataModel)  
    
    def updateArrayOnScreen(self):
        self.__dataModel.updateArrayOnScreen() 
    
    def getArray(self):
        return self.__dataModel.getArray()
    
    def getTarget(self):
        return self.__dataModel.getTarget() 
    
    def changeBarColour(self, index : int, colour : str):
        self.__dataModel.setBarColour(index, colour)
    
    def getDataModel(self):
        return self.__dataModel
# Listen to American Idiot by Green Day