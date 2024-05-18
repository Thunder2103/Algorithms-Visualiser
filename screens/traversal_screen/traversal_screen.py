# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc 
import tkinter as tk 
from tkinter import ttk 
from .traversal_controller import TaversalController
from .traversal_model import TraversalModel


class TraversalScreen(sc.Screen, sc.ScreenTemplate): 
    def initScreen(self) -> None:
        self.createTemplate() 

        # Create model class
        self.__model = TraversalModel() 
        # Create controller class and add referencces to screen and model
        self.__controller = TaversalController(self, self.__model)
        # Add reference to controller to the model object
        self.__model.addController(self.__controller) 
        # Create the options users can interact with 
        self.__createOptions()

    # Creates the widgets that allows users to toggle the visualisers settings
    def __createOptions(self) -> None: 
        self.__createAlgorithmOptions() 
        self.__createSpeedAdjuster()

        self.__createStopSolveButtons()

    # Create the combo box that displays the algorithms users can see visualised 
    def __createAlgorithmOptions(self) -> None:
        # combo box, allows the user to choose what algorithm they want
        self.__algorithmOptions = ttk.Combobox(self.getOptionsWidgetFrame(), textvariable = tk.StringVar(), state = "readonly", font = (self.getFont(), self.getFontSize()),\
             width = self.getOptionsWidgetFrame().winfo_width())
        self.__algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        self.__algorithmOptions.bind("<<ComboboxSelected>>", lambda _: self.getOptionsWidgetFrame().focus())
        self.__algorithmOptions.pack(pady = (10,0)) 
    
    # Creates a slider that allows users to adjust an algorithms speed
    def __createSpeedAdjuster(self) -> None:
        # Creates a slider that goes from the maximum delay to the minmum delay 
        # Every time the sliders value is changed the updatetDelay() method is called to update the value seen on screen
        self.__speedSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = self.__model.getMaxDelay(), to_ = self.__model.getMinDelay(), resolution=self.__model.getResolution(), 
                                      length = self.getOptionsWidgetFrame().winfo_width(), orient = "horizontal", showvalue = False, 
                                      bg =  "white", highlightbackground = "white", command = self.__updateDelay)
        self.__speedSlider.pack(pady = (10, 0))  
        self.__speedSlider.set(self.__model.getMaxDelay())
        # When the user stops moving the slider the slider is updated in the DataModel class 
        self.__speedSlider.bind("<ButtonRelease-1>", lambda _ : self.__setDelay()) 
     
    def __updateDelay(self, value : str) -> None:
        self.__speedSlider.config(label = f"Delay: {value} Milliseconds")  

    def __setDelay(self) -> None:
        pass  


    # Creates buttons that lets user execute algorithms or stop them
    def __createStopSolveButtons(self) -> None:
        # Frame to store stop and solve buttons in a grid layout
        algorithmToggleFrame = tk.Frame(self.getOptionsWidgetFrame(), bg = "white")
        algorithmToggleFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        self.__solveStopButton = tk.Button(algorithmToggleFrame, text = "Solve.", width = 7, relief = "solid", 
                                           font = (self.getFont(), self.getFontSize()))
        self.__solveStopButton.grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        self.__pauseResumeButton = tk.Button(algorithmToggleFrame, text = "Pause.", width = 7, relief = "solid", 
                                             font = (self.getFont(), self.getFontSize()), state = "disabled")
        self.__pauseResumeButton.grid(row = 0, column = 1)  

# Listen to Can't Stop by The Red Hot Chili Peppers 