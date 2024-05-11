# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm
class QuickSort(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        super().__init__(dataModel)

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self) -> str:
        return "Quick Sort"  
    
    # Quick Sort Algorithm
    # Pivot selection using median of three 
    def quickSort(self) -> int:  
        self.__quickSortHelper(0, len(self.getArray()) - 1)
        self.updateArrayOnScreen() 
        self.delay() 
        return 1 
    
    def __quickSortHelper(self, start, end):   
        if(start >= end): return
        pivotIndex = self.__partition(start, end) 
        self.__quickSortHelper(start, pivotIndex - 1) 
        self.__quickSortHelper(pivotIndex + 1, end)
      
    def __partition(self, start, end):  
        # Middle of the array 
        mid = (start + end) // 2
        # Pivot is median of the elements at indexes start, mid, end 
        pivot, pivotIndex = sorted([(self.getElement(start), start), (self.getElement(mid), mid), (self.getElement(end), end)])[1]    
        pivotShift = pivotIndex
        
        # Iterate through any elements between pivot to end of array
        for i in range(pivotIndex + 1, end + 1): 
            if(self.getElement(i) <= pivot):  
                arr = self.__shiftRight(pivotShift, i)
                pivotShift += 1
        
        # Iterate between elements between start of array and pivot index 
        i = 0 
        while(i != pivotIndex):
            if(self.getElement(i) > pivot): 
                arr = self.__shiftLeft(i, pivotShift)  
                pivotShift -= 1  
                pivotIndex -= 1
            else: i+=1
        return pivotShift
    
    def __shiftRight(self, start, end): 
        index = end 
        value = self.getElement(end)
        while(index != start):  
            self.changeElement(index, self.getElement(index - 1))
            index-=1  
        self.changeElement(index, value)
    
    def __shiftLeft(self, start, end): 
        index = start 
        value = self.getElement(start)
        while(index != end):  
            self.changeElement(index, self.getElement(index + 1))
            index+=1  
        self.changeElement(index, value)    

                     
# Listen to Times like these by the Foo Fighters