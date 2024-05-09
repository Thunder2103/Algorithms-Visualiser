# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm
class MergeSort(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        super().__init__(dataModel)

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self) -> str:
        return "Merge Sort" 
    
    # Merge Sort Algorithm
    def mergeSort(self) -> int: 
        self.mergeSortHelper(0, len(self.getArray()) - 1)
        return 1
    
    def mergeSortHelper(self, leftPtr, rightPtr):  
        if(leftPtr >= rightPtr): return  
        mid = (leftPtr + rightPtr) // 2 
        self.mergeSortHelper(leftPtr, mid)
        self.mergeSortHelper(mid+1, rightPtr)
        self.mergeArrays(leftPtr, mid, rightPtr)

    def mergeArrays(self, start, mid, end):  
        leftPtr = start 
        rightPtr = mid + 1 
        while(leftPtr <= mid and rightPtr <= end): 
            self.changeBarColour(leftPtr, "red")
            self.updateArrayOnScreen()
            self.delay()
            if(self.isSwapNeeded(leftPtr, rightPtr)): 
                self.shiftArrayElements(leftPtr, rightPtr)
                leftPtr += 1
                mid += 1 
                rightPtr += 1 
            else: 
                leftPtr += 1 
            
    def shiftArrayElements(self, leftPtr, rightPtr):  
        value = self.getElement(rightPtr)
        index = rightPtr 
        while(index != leftPtr):  
            self.swapElements(index, index - 1) 
            index -=  1
        
        self.changeElement(leftPtr, value)
        self.changeBarColour(rightPtr, "red")
        self.updateArrayOnScreen()
        self.delay()

# Listen to Wake Me Up When September Ends by Green Day
