# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc
import tkinter as tk 

from .search_controller import SearchController
from .search_model import SearchModel

class SearchScreen(sc.Screen, sc.SharedLayout):    
    def initScreen(self) -> None:
        self.createBaseLayout()
        self.loadAlgorithmOptions("search")
    
        # Controller and Model classes
        self.__searchModel = SearchModel()
        self.__searchController = SearchController(self, self.__searchModel, self.getDataModel()) 

        # Create Target slider
        self.__createTargetAdjuster() 
    
    # Creates a slider that lets sers decide if the target is in the array, not in the array or randomly generated
    def __createTargetAdjuster(self) -> None:
        # Creates a slider that goes from 0 to 1 to 2
        # The three values correlate to the three possible target options
        # The target can guranteed to be in the array, guaranteed to not be in the array or randomly selected
        self.__targetSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = 0, to_ = 2, length = self.getOptionsWidgetFrame().winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", showvalue = False, command = self.updateDisplayedText)
        self.__targetSlider.pack(pady = (10, 0))
        # Initially the slider is set at 0, which is the target being randomly selected
        self.__targetSlider.config(label = "Target: Random") 

    # When the target slider has changed value a label is added to show the relevant target information 
    def updateDisplayedText(self, value : str) -> None: 
        self.__targetSlider.config(label = self.__searchController.updateSliderText(value)) 

# Wretches and Kings by Linkin Park                 