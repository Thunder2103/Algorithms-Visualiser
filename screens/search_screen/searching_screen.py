# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc
import algorithms.handlers as h
import tkinter as tk 
from tkinter import ttk
import random

class SearchScreen(sc.Screen, sc.SharedLayout):
    def initScreen(self) -> None:
        # Creates basic layout of the screen
        self.createTemplate()

        # Dictionary pairing numbers to speed
        # This allows the slider to show "Small", "Medium" and "Fast" instead of 0, 1, 2
        self.__numbersToSpeed = {
            0: ["Slow", 4],
            1: ["Medium", 2.5],
            2: ["Fast", 1],
            3: ["Super Fast", 0.5]
        }   

        # Dictionary pairing numbers to speed 
        self.__numbersToText = {
            0: ["Target: Random", self.targetRandom], 
            1: ["Target: In array", self.targetIn],
            2: ["Target: Not in array", self.targetOut]
        }

        # Handles logic of the GUI and handling the array
        self.__model = sc.SearchModel()
        self.__controller = sc.SearchController(self, self.__model)

        # Creating and displaying options
        self.__createOptions() 

    # This functions handles creating and displaying the options the user is presented with
    def __createOptions(self) -> None: 
        self.__createAlgorithmOptions()               
        self.__createSpeedAdjuster()
        self.__createArrayAdjuster()
        self.__createTargetAdjuster()
        self.__createStopSolveButtons()

    # Creates a combo box which displays all algorithms 
    def __createAlgorithmOptions(self) -> None:
        #combo box, allows the user to choose what algorithm they want
        self.__algorithmOptions = ttk.Combobox(self.getOptionsWidgetFrame(), textvariable = tk.StringVar(), state = "readonly", font = (self.getFont(), 12),\
             width = self.getOptionsWidgetFrame().winfo_width())
        self.__algorithmOptions['value'] = h.getAlgorithms()
        self.__algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        self.__algorithmOptions.bind("<<ComboboxSelected>>", lambda _: self.getOptionsWidgetFrame().focus())
        self.__algorithmOptions.pack(pady = (10,0)) 
    
    # Creates a slider that allows users to adjust an algorithms speed
    def __createSpeedAdjuster(self) -> None:
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.__speedSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = 0, to_ = 3, length = self.getOptionsWidgetFrame().winfo_width(),\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.__speedSlider.pack(pady = (10, 0))  
        # Initially the slider is set at 0, which is the Slow speed
        self.__speedSlider.config(label = "Slow")  
    
    # Creates a slider that allows users to alter an arrays size
    def __createArrayAdjuster(self) -> None:
        self.__arraySizeSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = 1, to_ = self.__model.getMaxBars(), length = self.getOptionsWidgetFrame().winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", command = self.__controller.adjustArray)
        self.__arraySizeSlider.pack(pady = (10, 0))

    # Creates a slider that lets sers decide if the target is in the array, not in the array or randomly generated
    def __createTargetAdjuster(self) -> None:
        # Creates a slider that goes from 0 to 1 to 2
        # The three values correlate to the three possible target options
        # The target can guranteed to be in the array, guaranteed to not be in the array or randomly selected
        self.__targetSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = 0, to_ = 2, length = self.getOptionsWidgetFrame().winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", showvalue = False, command = self.intToText)
        self.__targetSlider.pack(pady = (10, 0))
        # Initially the slider is set at 0, which is the target being randomly selected
        self.__targetSlider.config(label = "Target: Random") 
    
    # Creates buttons that lets user execute algorithms or stop them
    def __createStopSolveButtons(self) -> None:
        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(self.getOptionsWidgetFrame(), bg = "white")
        stopSolveFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.getFont(), 12), command = lambda: self.initAlgorithm())\
            .grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.getFont(), 12), state = "disabled", command = lambda : print("Hello"))\
            .grid(row = 0, column = 1)  

    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value : str) -> None: 
        self.__speedSlider.config(label = self.__numbersToSpeed[int(value)][0])  

    # When the target slider has changed value a label is added to show the relevant target information
    def intToText(self, value : str) -> None:
        self.__targetSlider.config(label = self.__numbersToText[int(value)][0]) 
               
    # Gets options user has selected from the slider (an intger used as the dictionary key)
    # and calls the paired function stored in the dictionary 
    # Each function returns an integer -> the target
    def generateTarget(self) -> int:
        return self.__numbersToText[self.__targetSlider.get()][1]()
    
    # Makes sure that target generated has (almost) equal chance to be in the array or not 
    def targetRandom(self) -> int: 
        # Chooses either 1 or 0 
        # If 1 is chosen then call function to gurantee target is in array
        if random.randint(0 , 1): return self.targetIn()
        # Else call function to gurantee target not in array
        else: return self.targetOut()
    
    # Guarantees target is in the array
    def targetIn(self) -> int: 
       # Randomly chooses index from array and returns integers at that index
       return self.__model.getArray()[random.randint(0, len(self.__model.getArray()) - 1)] 

    # Guarantees target is not in arrat
    def targetOut(self) -> int: 
        # Chooses a number between the range of arrays smallest value - 20 and arrays largest value + 20
        target = random.randint(min(self.__model.getArray()) - 20, max(self.__model.getArray()) + 20)
        # If generated number in array recall function
        if target in self.__model.getArray(): self.targetOut()
        # If generated number not in array then just return value
        else: return target
        
    # Call algorithm user has selected
    def initAlgorithm(self) -> None:
        # Doesn't do anything is user hasn't chosen an algorithm
        if(self.getAlgorithmChoice() == 'Select an algorithm.'): 
            self.__algorithmOptions.config(foreground = "red")
        else:
            # Generates target the algorithm looks for 
            self.target = self.generateTarget()
            # Call algorithm -> so this program actually has a use
            h.callAlgorithm(self, self.getAlgorithmChoice())
    
    # Returns algorithm the user has selected 
    def getAlgorithmChoice(self) -> str:
        return self.__algorithmOptions.get()

    # Returns array
    def getArray(self) -> list:
        return self.__model.getArray()

    # Returns target
    def getTarget(self) -> int:
        return self.target
    
    # Returns number of seconds to delay each iteration of algorithm
    def getDelay(self) -> int:
        return self.__numbersToSpeed[self.__speedSlider.get()][1]
    
    def displayArray(self, defaultColour, index = None, currentIndex = None): 
        self.__controller.displayArray(defaultColour, index, currentIndex)
