# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from ..algorithm import Algorithm
class BogoSort(Algorithm):
    # Constructor
    def __init__(self, dataModel):
        super().__init__(dataModel)

    # Returns algorithms name -> user sees this when selecting algorithm
    def getName(self) -> str:
        return "Bogo Sort" 
    
    # Bogo Sort Algorithm
    def bogoSort(self) -> int: 
        array = self.getArray()
        while(sorted(array) != array): 
            self.shuffleArray(delay=False)
            self.delay()

# Listen to Times like these by the Foo Fighters