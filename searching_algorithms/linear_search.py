# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from .algorithm import Algorithm

class LinearSearch(Algorithm):
    def getName(self):
        return "Linear Search" 
    
    def linearSearch(array, target):
        i = 0
        while(i < len(array)):
            if(array[i] == target): return i   
            i += 1
        return -1 

