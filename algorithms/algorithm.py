# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from abc import ABC, abstractmethod
import time
# Abstract class - every algorithm must implement the getName() method
class Algorithm(ABC):    
    @abstractmethod
    def getName(self): pass 

    def delay(self, dataModel):
        i = 0 
        while(i < dataModel.getDelay()):
            time.sleep(0.1)
            i+=0.1

# Listen to American Idiot by Green Day