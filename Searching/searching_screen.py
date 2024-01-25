# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import Screen_Templates as st
from .searching_model import SearchModel
from .algorithm_names import getAlgorithms
from Searching.init_algorithm import callAlgorithm
import tkinter as tk 
from tkinter import ttk
import random

class SearchScreen(st.Screen, st.SharedLayout):
    def initScreen(self) -> None:
        # Creates basic layout of the screen
        self.createTemplate()

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

        # Dictionary pairing numbers to speed 
        self.numbersToText = {
            0: ["Target: Random", self.targetRandom], 
            1: ["Target: In array", self.targetIn],
            2: ["Target: Not in array", self.targetOut]
        }

        # Returns the height of the canvas - maximum number of pixels an element can possibly have
        self.maximumPixels = self.calculateMaximumPixels()
        
        # Calculates spacing between canvas border and displayed array 
        # Is also used to calculate the largest possible size of the array
        self.minPadding = self.calculateBestPadding() 

        # Creating and displaying options
        self.createOptions() 

        # SearchModel contains all the data
        self.model = SearchModel()
     
        # Get array from SearchModel
        self.array = self.model.getArray()

        # Lower bound 
        self.randomLow = self.model.getLow() 
        # Highest value that can appear in array
        self.randomHigh = self.model.getHigh()

        # Calculate upper and lower array bounds
        self.calculateArrayBounds()

    # This functions handles creating and displaying the options the user is presented with
    def createOptions(self) -> None: 
        self.createAlgorithmOptions()               
        self.createSpeedAdjuster()
        self.createArrayAdjuster()
        self.createTargetAdjuster()
        self.createStopSolveButtons()

    # Creates a combo box which displays all algorithms 
    def createAlgorithmOptions(self) -> None:
        #combo box, allows the user to choose what algorithm they want
        self.algorithmOptions = ttk.Combobox(self.optionsWidgetsFrame, textvariable = tk.StringVar(), state = "readonly", font = (self.FONT, 12),\
             width = self.optionsWidgetsFrame.winfo_width())
        self.algorithmOptions['value'] = getAlgorithms()
        self.algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        self.algorithmOptions.bind("<<ComboboxSelected>>", lambda _: self.algorithmInfoFrame.focus())
        self.algorithmOptions.pack(pady = (10,0)) 
    
    # Creates a slider that allows users to adjust an algorithms speed
    def createSpeedAdjuster(self) -> None:
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 0, to_ = 3, length = self.optionsWidgetsFrame.winfo_width(),\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack(pady = (10, 0))  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow")  
    
    # Creates a slider that allows users to alter an arrays size
    def createArrayAdjuster(self) -> None:
        self.arraySizeSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 1, to_ = self.maxBars, length = self.optionsWidgetsFrame.winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", command = self.adjustArray)
        self.arraySizeSlider.pack(pady = (10, 0))

    # Creates a slider that lets sers decide if the target is in the array, not in the array or randomly generated
    def createTargetAdjuster(self) -> None:
        # Creates a slider that goes from 0 to 1 to 2
        # The three values correlate to the three possible target options
        # The target can guranteed to be in the array, guaranteed to not be in the array or randomly selected
        self.targetSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 0, to_ = 2, length = self.optionsWidgetsFrame.winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", showvalue = False, command = self.intToText)
        self.targetSlider.pack(pady = (10, 0))
        # Initially the slider is set at 0, which is the target being randomly selected
        self.targetSlider.config(label = "Target: Random") 
    
    # Creates buttons that lets user execute algorithms or stop them
    def createStopSolveButtons(self) -> None:
        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(self.optionsWidgetsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.FONT, 12), command = lambda: self.initAlgorithm())\
            .grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.FONT, 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1)  

    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value : str) -> None: 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)][0])  

    # When the target slider has changed value a label is added to show the relevant target information
    def intToText(self, value : str) -> None:
        self.targetSlider.config(label = self.numbersToText[int(value)][0]) 
               
    # Adjusts size of bars so amount of elements can fit on screen and stay in the canvas' centre
    def adjustArray(self, value : str) -> None:
        # If the value given from the scrollbar is less than the arrays size
        # Delete elements from the array and check if bar size can increase
        if(int(value) < len(self.array)): 
            self.deleteElements(int(value))
            self.increaseBarSize()
        # Otherwise add elements to the array and check is bar size needs to decrease
        else: 
            self.addElements(int(value))
            self.decreaseBarSize()
        # If the array size is less than the maximum number of bars. 
        # Calculate padding 
        if(len(self.array) != self.maxBars): self.padding = self.calculatePadding()
        # If the array size is now at maximum size, 
        # padding is the value calulated by the calculateBestPadding() method
        else: self.padding = self.minPadding
        
        # The amount each elements is stretched along the y-axis 
        # Means the elements are scaled with the largest element
        self.yStretch = self.maximumPixels / max(self.array)
        # Draw the actual array with all the adjustments made
        # Since there is no algorithm active, all bars are drawn as black
        self.displayArray("Black")
        
    # Iterates through array, drawing each bar
    # The function has two default arguements -> currentIndex and altColour both initialised to None
    def displayArray(self, defaultColour, currentIndex = None, altColour = None) -> None:
            # Clear displayed array on screen
            self.clearDisplayedArray()
            for x, y in enumerate(self.array):
                # Calculate where each bar is placed on screen
                # Bottom left co-ord
                x1 = x * self.barDist + x * self.barWidth + self.padding
                # Top left coord
                y1 = self.arrayCanvas.winfo_height() - (y * self.yStretch)  
                # Bottom right coord
                x2 = x * self.barDist + x * self.barWidth + self.barWidth + self.padding
                # Top right coord
                y2 = self.arrayCanvas.winfo_height() 
                # Chooses correct colour for bar to be filled in with
                if x == currentIndex: self.arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = altColour) 
                else: self.arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = defaultColour) 
            # Updates screen so bars can be seen onscreen
            self.window.update()
      
    # Wipes everything off the canvas
    def clearDisplayedArray(self) -> None:
        self.arrayCanvas.delete("all")

    # Adds amount of elements corresponding to the value
    def addElements(self, value):
        for _ in range(len(self.array), value):
            # Choose random number inbetween upper and lower bounds
            self.array.append(random.randint(self.lowerBound, self.upperBound)) 
    
    # Deletes number of elements corresponding to the value
    def deleteElements(self, value) -> None:
        for _ in range(len(self.array), value, -1):
            self.array.pop()

    # Determines if bars need to shrink in size as array grows
    def decreaseBarSize(self) -> None:
        for i in range(self.barWidth, self.minBarWidth, -1):
            if(len(self.array) < round(self.calculateMaxBars(i, self.maxPadding))):
                self.barWidth = i
                return
        self.barWidth = self.minBarWidth
            
    # Determines if bars needs to increase in size as array shrinks
    def increaseBarSize(self) -> None:
        for i in range(self.barWidth + 1, self.maxBarWidth + 1):
             if(len(self.array) < round(self.calculateMaxBars(i, self.maxPadding))):
                self.barWidth = i 
    
    # Calculate upper and lower bounds of the array
    def calculateArrayBounds(self) -> None:
        # Calculate maximum value the array can have by:
        # Choosing an arbitrary number between randomLow and randomHigh and doubling it 
        self.upperBound = random.randint(self.randomLow, self.randomHigh) * 2 
        
        # Long explanation time...
        # Lower is the absolute minimum value that can appear on screen 
        # Bars are only visible if the top right coorindate is less than or equal to the value of maximumPixels - 0.5 
        # So lower can be calculated be rearranging the y1 coord equation to solve for y
        # 0.5 was rounded up to 1 because it looks nicer
        self.lowerBound = round((self.arrayCanvas.winfo_height() - self.maximumPixels + 1) / (self.maximumPixels / self.upperBound))  
    
        # Draw the first element on screen
        self.adjustArray('1')
    
    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self) -> int:
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn   
        return self.arrayCanvas.winfo_height() - 2
    
    # Finds the best distance between the displayed array and the edges of canvas, 
    # to maximise the number of elements and centre the array as best as possible
    def calculateBestPadding(self) -> int:
        for i in range(self.minPadding, self.maxPadding):
            # Calculates how many bars can be displayed on the screen 
            bars = self.calculateMaxBars(self.minBarWidth, i)  
            # If the number of bars is a whole number
            if((bars).is_integer()):  
                # Maximum size the array can be
                self.maxBars = int(bars)
                # Function terminates - returning the best padding (i)
                return i
        # If no whole number can be found, just use the max padding (the array being off centre is less noticeable) 
        self.maxBars = round(self.calculateMaxBars(self.minBarWidth, self.maxPadding))
        return self.maxPadding
       
    # Calculates maximum number of bars that can be displayed given the padding
    def calculateMaxBars(self, barWidth, padding) -> int:
        return ((self.arrayCanvas.winfo_width()) - (padding * 2)) / (barWidth + self.barDist)

    # Calculates the padding to centre the array of a given size
    def calculatePadding(self) -> int:
        return ((self.arrayCanvas.winfo_width() - (len(self.array) * (self.barDist + self.barWidth))) // 2) + self.barDist 

    # Gets options user has selected from the slider (an intger used as the dictionary key)
    # and calls the paired function stored in the dictionary 
    # Each function returns an integer -> the target
    def generateTarget(self) -> int:
        return self.numbersToText[self.targetSlider.get()][1]()
    
    # Makes sure that target generated has (almost) equal chance to be in the arry or not 
    def targetRandom(self) -> int: 
        # Chooses either 1 or 0 
        # If 1 is chosen then call function to gurantee target is in array
        if random.randint(0 , 1): return self.targetIn()
        # Else call function to gurantee target not in array
        else: return self.targetOut()
    
    # Guarantees target is in the array
    def targetIn(self) -> int: 
       # Randomly chooses index from array and returns integers at that index
       return self.array[random.randint(0, len(self.array) - 1)] 

    # Guarantees target is not in arrat
    def targetOut(self) -> int: 
        # Chooses a number between the range of arrays smallest value - 20 and arrays largest value + 20
        target = random.randint(min(self.array) - 20, max(self.array) + 20)
        # If generated number in array recall function
        if target in self.array: self.targetOut()
        # If generated number not in array then just return value
        else: return target
        
    # Call algorithm user has selected
    def initAlgorithm(self) -> None:
        # Doesn't do anything is user hasn't chosen an algorithm
        if(self.getAlgorithmChoice() == 'Select an algorithm.'): 
            self.algorithmOptions.config(foreground = "red")
        else:
            # Generates target the algorithm looks for 
            self.target = self.generateTarget()
            # Call algorithm -> so this program actually has a use
            callAlgorithm(self, self.getAlgorithmChoice())
    
    # Returns algorithm the user has selected 
    def getAlgorithmChoice(self) -> str:
        return self.algorithmOptions.get()

    # Returns array
    def getArray(self) -> list:
        return self.array

    # Returns target
    def getTarget(self) -> int:
        return self.target
    
    # Returns number of seconds to delay each iteration of algorithm
    def getDelay(self) -> int:
        return self.numbersToSpeed[self.speedSlider.get()][1]
    
    # Just a placeholder until I write actual functions 
    def placeholder(self): 
        print(self.array)