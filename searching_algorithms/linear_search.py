# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from .algorithm import Algorithm
import time

class LinearSearch():
    def getName(self):
        return "Linear Search" 
    
    def linearSearch(self, array, target):
        for i, element in enumerate(array):
            if element == target: return i
        return -1 
    