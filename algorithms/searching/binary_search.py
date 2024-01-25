# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


from ..algorithm import Algorithm
import time

class BinarySearch(Algorithm):
    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self):
        return "Binary Search" 
    
    # Binary Search algorithm -> see markdown for explanation
    def binarySearch(self, Searching):
        # Grabs everything array needs
        self.init(Searching)
        # Sorts array 
        self.sortArray(Searching)
        # Low and high variables used to adjust mid
        low = 0 
        high = len(self.array) - 1
        
        while(low <= high):
            # Calculate new mid
            mid = (low + high) // 2
            # If element at mid is equal to the target
            if self.array[mid] == self.target:
                Searching.displayArray("Black", mid, "Green")
                return 1
            # If element at mid is greater than the target
            elif self.array[mid] > self.target:
                # Disreguard upper end of array
                high = mid - 1
            # If element is less than the target
            # Disreguard lower end of the array
            else: low = mid + 1
            Searching.displayArray("Black", mid, "Red")
            time.sleep(self.delay)
        return 0 
    
# Listen to Welcome to the DCC by Nothing But Thieves