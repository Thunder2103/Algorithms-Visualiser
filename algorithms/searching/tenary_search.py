# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm 

class TenarySearch(Algorithm): 
    # Constructor
    def __init__(self, dataModel):
        super().__init__(dataModel)
    
    def getName(self):
        return "Tenary Search"
    
    def tenarySearch(self): 
        self.sortArray()
        array = self.getArray()
        target = self.getTarget() 

        left = 0 
        right = len(array) - 1

        while(left <= right): 
            mid1 = left + (right - left) // 3 
            mid2 = right - (right - left) // 3 
            self.changeBarColour(mid1, "red")
            self.changeBarColour(mid2, "red")

            if(array[mid1] == target): 
                self.changeBarColour(mid1, "green") 
                self.changeBarColour(mid2, "black") 
                self.updateArrayOnScreen()
                return 1 
            if(array[mid2] == target): 
                self.changeBarColour(mid1, "black") 
                self.changeBarColour(mid2, "green") 
                self.updateArrayOnScreen()
                return 1  

            if(target < array[mid1]): right = mid1 - 1 
            elif(target > array[mid2]): left = mid2 + 1 
            else: 
                left = mid1 + 1 
                right = mid2 - 1 
            self.updateArrayOnScreen()
            self.delay()
        return -1 