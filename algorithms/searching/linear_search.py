# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm
import time
class LinearSearch(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        self.__dataModel = dataModel

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self) -> str:
        return "Linear Search" 
    
    # Linear Search Algorithm
    def linearSearch(self) -> int:        
        # Iterate through array one element at a time
        for index, num in enumerate(self.__dataModel.getArray()):
            # If current element is equal to the target
            if num == self.__dataModel.getTarget():
                self.__dataModel.setBarColour(index, "green")
                self.__dataModel.displayArray()
                return 1
            self.__dataModel.setBarColour(index, "red")
            self.__dataModel.displayArray()
            self.delay(self.__dataModel)     
        return -1