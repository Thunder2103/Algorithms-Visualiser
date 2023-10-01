# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from .algorithm import Algorithm
import time
class LinearSearch(Algorithm):
    def getName(self):
        return "Linear Search" 
    
    # Retrieves whatever algorithm needs to run
    def init(self, Searching):
        self.array = Searching.getArray()
        self.target = Searching.getTarget()
        self.delay = Searching.getDelay()
        
    # Linear Searching algorithm -> see markdown for explanation
    def linearSearch(self, Searching):
        self.init(Searching)
        for index, num in enumerate(self.array):
            if num == self.target:
                Searching.displayArray("Black", index, "Green")
                return 1
            else: Searching.displayArray("Black", index, "Red")
            time.sleep(self.delay)       