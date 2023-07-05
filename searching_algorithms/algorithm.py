# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from abc import ABC, abstractmethod
# Abstract class - every algorithm must implement the algorithmName method
class Algorithm(ABC):
    @abstractmethod
    def getName(self): pass 

