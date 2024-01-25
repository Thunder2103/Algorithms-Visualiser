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

    # All Searching Algorithms need the array, the target and the time delay
    def init(self, Searching):
        self.array = Searching.getArray()
        self.target = Searching.getTarget()
        self.delay = Searching.getDelay()
    
    # Sorts given array -> since several algorithms need a sorted array
    def sortArray(self, Searching):
        self.array.sort()
        Searching.displayArray("Black")
        # Small delay after sorting and displaying array
        time.sleep(0.5)
    
# Listen to American Idiot by Green Day