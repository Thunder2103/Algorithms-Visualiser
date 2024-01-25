# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


from ..algorithm import Algorithm
import time
import math 

class JumpSearch(Algorithm):
    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self):
        return "Jump Search" 

    def jumpSearch(self, Searching):
        # Gets everything the algorithm needs
        self.init(Searching)
        # Sorts array
        self.sortArray(Searching)
        # length of array
        n = len(self.array)
        # Square root length of array to find jump size
        step = int(math.sqrt(n))
        # Store index of last jump
        prev = 0
        # Find block clostest to target -> if it exists
        while(self.array[min(step, n) - 1] < self.target):
            prev = step
            if prev >= n: 
                print("Here", prev)
                Searching.displayArray("Black", n - 1, "Red")
                return 0
            Searching.displayArray("Black", step, "Red")
            step += int(math.sqrt(n))
            time.sleep(self.delay) 
        
        # Linear search to find target
        # Start at index of last jump and stops at index of next jump 
        for i in range(prev, prev + int(math.sqrt(n))):
            # If current elment > target then target not in array
            if self.array[i] > self.target:
                Searching.displayArray("Black", i, "Red")
                return 1 
            # If current element is equal to target
            if self.array[i] == self.target:
                Searching.displayArray("Black", i, "Green")
                return 1  
            Searching.displayArray("Black", i, "Red")
            time.sleep(self.delay)
        return 0
    
# Listen to Waiting For The End by Linkin Park