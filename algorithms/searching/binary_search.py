# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


from ..algorithm import Algorithm

class BinarySearch(Algorithm):
    def __init__(self, dataModel):
        self.__dataModel = dataModel

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self):
        return "Binary Search" 
    
    # Binary Search algorithm -> see markdown for explanation
    def binarySearch(self):
        # Sorts array 
        self.__dataModel.sortArray()
        self.__dataModel.displayArray()
        
        array = self.__dataModel.getArray()
        target = self.__dataModel.getTarget()
 
        # Low and high variables used to adjust mid
        low = 0 
        high = len(array) - 1
        
        while(low <= high):
            # Calculate new mid
            mid = (low + high) // 2
            # If element at mid is equal to the target
            if array[mid] == target:
                self.__dataModel.setBarColour(mid, "green")
                self.__dataModel.displayArray()
                return 1
            # If element at mid is greater than the target
            elif array[mid] > target:
                # Disreguard upper end of array
                high = mid - 1
            # If element is less than the target
            # Disreguard lower end of the array
            else: low = mid + 1
            self.__dataModel.setBarColour(mid, "red")
            self.__dataModel.displayArray()
            self.delay(self.__dataModel) 
        return 0 
    
# Listen to Welcome to the DCC by Nothing But Thieves