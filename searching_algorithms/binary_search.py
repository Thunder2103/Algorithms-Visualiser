# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


from .algorithm import Algorithm
import time

class BinarySearch(Algorithm):
    def getName(self):
        return "Binary Search" 
    
    # Returns algorithms name -> user sees this when selecting algorithm
    def init(self, Searching):
        self.array = Searching.getArray()
        self.target = Searching.getTarget()
        self.delay = Searching.getDelay()
        
        # Binary search neess sorted array to work
        self.array.sort()
        Searching.displayArray("Black")
        # Small delay after sorting and displaying array
        time.sleep(0.5)
    
    # Binary Search algorithm -> see markdown for explanation
    def binarySearch(self, Searching):
        self.init(Searching)
        
        low = 0 
        high = len(self.array) - 1
        
        while(low <= high):
            mid = (low + high) // 2
            if self.array[mid] == self.target:
                Searching.displayArray("Black", mid, "Green")
                print("Found", self.target, self.target in self.array)
                return 1
            elif self.array[mid] > self.target:
                high = mid - 1
            else: low = mid + 1
            
            Searching.displayArray("Black", mid, "Red")
            time.sleep(self.delay)
        return 0

        
        
