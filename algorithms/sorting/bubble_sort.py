# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm
class BubbleSort(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        super().__init__(dataModel)

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self) -> str:
        return "Bubble Sort" 
    
    # Bubble Sort Algorithm
    def bubbleSort(self) -> int: 
        array = self.getArray()  
        n = len(array)
        for i in range(n): 
            swapped = False
            for j in range(0, n - i - 1): 
                self.changeBarColour(j, "red") 
                self.updateArrayOnScreen() 
                self.delay()
                if(self.isSwapNeeded(j, j + 1)): 
                    self.swapElements(j, j + 1)
                    self.swapBarColours(j, j + 1)
                    swapped = True
            if(not swapped): return 1
        return 1

# Listen to Times like these by the Foo Fighters