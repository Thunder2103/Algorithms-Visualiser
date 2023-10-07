# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from .algorithm import Algorithm
import time
class LinearSearch(Algorithm):
    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self):
        return "Linear Search" 
    
    # Linear Search Algorithm
    def linearSearch(self, Searching):
        # Gets everything algorithm needs to run
        self.init(Searching) 
        
        # Iterate through array one element at a time
        for index, num in enumerate(self.array):
            # If current element is equal to the target
            if num == self.target:
                Searching.displayArray("Black", index, "Green")
                return 1
            Searching.displayArray("Black", index, "Red")
            time.sleep(self.delay)       
        return 0