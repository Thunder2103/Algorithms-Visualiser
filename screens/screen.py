# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from abc import ABC, abstractmethod
# Abstract class - every screen must implement the layout method
class Screen(ABC):
    @abstractmethod
    def initScreen(self):
        pass 
