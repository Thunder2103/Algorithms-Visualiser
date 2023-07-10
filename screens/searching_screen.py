# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc
from searching_algorithms.algorithm_names import getAlgorithms
import tkinter as tk 
from tkinter import ttk
import random
import math

class Searching(sc.Screen, sc.SharedLayout):
    def initScreen(self):
        # Creates basic layout of the screen
        self.createTemplate()

        # Returns the height of the canvas - maximum number of pixels an element can possibly have
        self.maximumPixels = self.calculateMaximumPixels()
        
        # Calculates spacing between canvas border and displayed array 
        # Is also used to calculate the largest possible size of the array
        self.padding = self.calculateBestPadding() 

        # Creating and displaying options
        self.createOptions() 

        # Calculate upper and lower array bounds
        self.calculateArrayBounds()

    # This functions handles creating and displaying the options the user is presented with
    def createOptions(self): 
        #combo box, allows the user to choose what algorithm they want
        algorithmOptions = ttk.Combobox(self.optionsWidgetsFrame, textvariable = tk.StringVar(), state = "readonly", font = (self.FONT, 12),\
             width = self.optionsWidgetsFrame.winfo_width())
        algorithmOptions['value'] = getAlgorithms()
        algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        algorithmOptions.bind("<<ComboboxSelected>>", lambda e: self.algorithmInfoFrame.focus())
        algorithmOptions.pack(pady = (10,0))
                        
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 0, to_ = 2, length = self.optionsWidgetsFrame.winfo_width(),\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack(pady = (10, 0))  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        self.arraySizeSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 1, to_ = self.maxBars, length = self.optionsWidgetsFrame.winfo_width(),\
            orient = "horizontal", bg = "white", highlightbackground = "white", command = self.displayArray)
        self.arraySizeSlider.pack(pady = (10, 0))

        # Makes sure there is enough space for extra options
        tk.Label(self.optionsWidgetsFrame, text = "Filler for extra options", font = (self.FONT, 12)).pack(pady = (10, 0))

        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(self.optionsWidgetsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.FONT, 12), command = lambda: self.initAlgorithm(algorithmOptions))\
            .grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.FONT, 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1)  
        
    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
       
    # Iterates through array and draws bars on screen 
    def displayArray(self, value):
        # If the value given from the scrollbar is less than the arrays size
        # Delete elements from the array and check if bar size can increase
        if(int(value) < len(self.array)): 
            self.deleteElements(int(value))
            self.increaseBarSize()
        # Otherwise add elements to the array and check is bar size needs to decrease
        else: 
            self.addElements(int(value))
            self.decreaseBarSize()
        # Clear displayed array on screen
        self.clearDisplayedArray()
        # If the array less than the maximum number of bars. 
        # Calculate padding 
        if(len(self.array) != self.maxBars): padding = self.calculatePadding()
        # If the array is now at maximum size, 
        # padding is the value calulated by the calculateBestPadding() method
        else: padding = self.padding
        
        # The amount each elements is stretched along the y-axis 
        # Means the elements are scaled with the largest element
        yStretch = self.maximumPixels / max(self.array)
        # Calculate where each bar is placed on screen
        for x, y in enumerate(self.array):
            # Bottom left co-ord
            x1 = x * self.barDist + x * self.barWidth + padding
            # Top left coord
            y1 = self.arrayCanvas.winfo_height() - (y * yStretch)  
            # Bottom right coord
            x2 = x * self.barDist + x * self.barWidth + self.barWidth + padding
            # Top right coord
            y2 = self.arrayCanvas.winfo_height() 
            self.arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = "Black")
      
    # Wipes everything off the canvas
    def clearDisplayedArray(self):
        self.arrayCanvas.delete("all")

    # Adds amount of elements corresponding to the value
    def addElements(self, value):
        for i in range(len(self.array), value):
            self.array.append(random.randint(self.lower, self.upper)) 
    
    # Deletes number of elements corresponding to the value
    def deleteElements(self, value):
        for i in range(len(self.array), value, -1):
            self.array.pop()

    # Determines if bars need to shrink in size as array grows
    def decreaseBarSize(self):
        for i in range(self.barWidth, self.minBarWidth, -1):
            if(len(self.array) < round(self.calculateMaxBars(i, self.maxPadding))):
                self.barWidth = i
                return
        self.barWidth = self.minBarWidth
            
    # Determines if bars needs to increase in size as array shrinks
    def increaseBarSize(self):
        for i in range(self.barWidth + 1, self.maxBarWidth + 1):
             if(len(self.array) < round(self.calculateMaxBars(i, self.maxPadding))):
                self.barWidth = i 
    
    # Calculate upper and lower bounds of the array
    def calculateArrayBounds(self):
        # Choose an arbitary number, this is used to calculate the upper and lower bounds 
        mid = random.randint(100, 5000)
        # Upper is the largest value the array can display
        self.upper = mid * 2 
        
        # Long explanation time...
        # Lower is the absolute minimum value that can appear on screen 
        # Bars are only visible if the top right coorindate is less than or equal to the value of maximumPixels - 0.5 
        # So lower can be calculated be rearranging the y1 coord equation to solve for y
        # 0.5 was rounded up to 1 because it looks nicer
        self.lower = round((self.arrayCanvas.winfo_height() - self.maximumPixels + 1) / (self.maximumPixels / self.upper))  
    
        # Draw the first element on screen
        self.displayArray('1')
    
    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self):
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn  
        return self.arrayCanvas.winfo_height() - 2
    
    # Finds the best distance between the displayed array and the edges of canvas, 
    # to maximise the number of elements and centre the array as best as possible
    def calculateBestPadding(self):
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
    def calculateMaxBars(self, barWidth, padding):
        return ((self.arrayCanvas.winfo_width()) - (padding * 2)) / (barWidth + self.barDist)

    # Calculates the padding to centre the array of a given size
    def calculatePadding(self):
        return ((self.arrayCanvas.winfo_width() - (len(self.array) * (self.barDist + self.barWidth))) // 2) + self.barDist 

    # Makes sure user has selected an algorithm
    def initAlgorithm(self, algorithmOptions):
        if(algorithmOptions.get() == 'Select an algorithm.'): 
            algorithmOptions.config(foreground = "red")
        else: 
            print("Selected")

    def placeholder(self):
        print(self.array)
        print(len(self.array)) 
    