# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


class SearchModel():
    # The lowest and highest values in the array, 
    # can be decided by the user or the can be given default values
    def __init__(self, lowest = None, highest = None):
         #array to be searched
        self.array = []

        # Dictionary pairing numbers to speed
        # This allows the slider to show "Small", "Medium" and "Fast" instead of 0, 1, 2
        self.numbersToSpeed = {
            0: ["Slow", 4],
            1: ["Medium", 2.5],
            2: ["Fast", 1],
            3: ["Super Fast", 0.5]
        }   

        # Binds number the speed to an integer value -> number seconds to delay algorithm
        self.speedToSeconds = {
            "Slow": 4,
            "Medium": 2.5,
            "Fast": 1,
            "Super Fast": 0.5
        }

        # If the user has not given the lowest value in the array -> set it to the default
        if lowest == None:
            self.lowest = 100 
        else: self.lowest = lowest
        # If the user has not given the highest value in the array -> set it to the default
        if highest == None:
            self.highest = 5000
        else:
            self.highest = highest 
    
    def getArray(self) -> list:
        return self.array 

    # If user wants to change default LOWEST value
    def setLow(self, value : int) -> None:
        self.lowest = value 

    # If user wants to change default HIGHEST value 
    def setHigh(self, value : int) -> None:
        self.highest = value 
    
    def getLow(self) -> int:
        return self.lowest

    def getHigh(self) -> int:
        return self.highest
