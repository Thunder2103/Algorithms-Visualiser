# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc
import tkinter as tk 
from .sort_controller import SortController
from .sort_model import SortModel

class SortScreen(sc.Screen, sc.SharedLayout):    
    def initScreen(self) -> None:
        self.createBaseLayout()
        self.loadAlgorithmOptions("sort")
    
        # Controller and Model classes
        self.__searchModel = SortModel()
        self.__searchController = SortController(self, self.__searchModel, self.getDataModel()) 

# Wretches and Kings by Linkin Park                 