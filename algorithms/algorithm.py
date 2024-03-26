# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from abc import ABC, abstractmethod
import time
import sys

# Abstract class - every algorithm must implement the getName() method
class Algorithm(ABC):    
    @abstractmethod
    def getName(self): pass 

    def delay(self, dataModel):
        self.__stopCheck(dataModel)
        time.sleep(dataModel.getDelay())
    
    def __stopCheck(self, dataModel):
        if(dataModel.isStopped()): 
            print("Algorithm Thread has terminated safely")
            sys.exit()
    
# Listen to American Idiot by Green Day