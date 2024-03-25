# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


from ..algorithm import Algorithm
import time
import math 

class JumpSearch(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        self.__dataModel = dataModel

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self):
        return "Jump Search" 

    def jumpSearch(self):
        # Sorts array 
        self.__dataModel.sortArray()
        self.__dataModel.displayArray()
        
        array = self.__dataModel.getArray()
        target = self.__dataModel.getTarget()
    
        # length of array
        n = len(array)
        # Square root length of array to find jump size
        step = int(math.sqrt(n))
        # Store index of last jump
        prev = 0
        # Find block clostest to target -> if it exists
        while(array[min(step, n) - 1] < target):
            prev = step
            self.__dataModel.setBarColour(prev, "red")
            if prev >= n: 
                self.__dataModel.displayArray()
                return 0
            self.__dataModel.displayArray()
            step += int(math.sqrt(n))
            self.delay(self.__dataModel)  
        
        # Linear search to find target
        # Start at index of last jump and stops at index of next jump 
        for i in range(prev, prev + int(math.sqrt(n))):
            self.__dataModel.setBarColour(i, "red")
            # If current elment > target then target not in array
            if array[i] > target:
                self.__dataModel.displayArray()
                return 1 
            # If current element is equal to target
            if array[i] == target:
                self.__dataModel.setBarColour(i, "green")
                self.__dataModel.displayArray()
                return 1  
            self.__dataModel.displayArray()
            self.delay(self.__dataModel)  
        return 0
    
# Listen to Waiting For The End by Linkin Park