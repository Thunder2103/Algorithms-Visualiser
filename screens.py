import tkinter as tk 
from tkinter import ttk
from abc import ABC, abstractmethod
import random
import math 

# If the file is run as is this message is returned and program exits
if(__name__ == "__main__"): 
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

# Abstract class - every screen must implement the layout method
class Screen(ABC):
    @abstractmethod
    def initScreen(self):
        pass 

# Ideally this should be the first screen the user sees 
class Introduction(Screen):
    def __init__(self, view):
        # Stores reference to view object
        self.view = view
        self.FONT = "Arial"

    def initScreen(self):
        # Get content Frame to store all widgets
        contentFrame = self.view.getContentFrame()
        # The introductory text is kept as a string 
        # as it makes it easier to change (and makes code easier to read)
        introText = "This program visualises different algorithms in a user friendly way. \n\
        Including array searching, sorting and tree traversal algorithms. \n\
        Press one of the buttons to start."

        # Header label
        tk.Label(contentFrame, text = "Welcome to Algorithms Anonymous.", font = (self.FONT, 18, "underline"), bg = "white")\
            .pack(pady = 10)

        # Label that contains the introduction text
        tk.Label(contentFrame, text = introText, font = (self.FONT, 14), justify = "center", bg = "white")\
            .pack(pady = 5)

        # Adds a frame for the buttons widgets 
        # Adding this frame makes positioning the buttons much easier
        buttonsFrame = tk.Frame(contentFrame, bg = "white")
        buttonsFrame.pack()

        tk.Button(buttonsFrame, text = "Path Finding", font = (self.FONT, 12), height = 2, width = 15, relief = "solid")\
            .pack(pady = (25, 0)) 

        tk.Button(buttonsFrame, text = "Array Searching",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid", \
                command = lambda : [self.view.removeScreen(), self.view.addScreen(Searching(self.view))]).pack(side = "left", pady = 15, padx = (100, 0))

        tk.Button(buttonsFrame, text = "Array Sorting",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid",\
                command = lambda : self.view.removeScreen()).pack(side = "left", padx = 100) 

        tk.Label(contentFrame, text = "Created by Thomas Gibson", bg = "white", justify = "left")\
            .pack(side = "bottom", anchor = "w", pady = 5, padx = 5)  

# Searching and Sorting Screens both use the same basic layout
# This class delegates the reponsiblity of creating the basic layout
class SharedLayout():
    def __init__(self, view):
        # Stores reference to view object
        self.view = view  
        
        # Font every widget uses 
        self.FONT = "Arial"
        
        #array to be searched
        self.array = []

        # Object stores the dictionary pairing numbers to speed
        # This allows the slider to show "Small", "Medium" and "Fast" instead of 0, 1, 2
        self.numbersToSpeed = {
            0: "Slow",
            1: "Medium",
            2: "Fast"
        }   

        # How big each bar is
        self.barWidth = 3
        # Distance between each bar 
        self.barDist = 2

    def createTemplate(self):
        # Get content Frame to store all widgets
        contentFrame = self.view.getContentFrame()
        # Get content frames width and height
        contentFrameHeight = self.view.getContentFrameHeight()
        contentFrameWidth = self.view.getContentFrameWidth()

        # width of the border
        borderSize = 2

        # Border frame gives appearence of a border between different frames
        borderFrame = tk.Frame(contentFrame, bg = "black", width = contentFrameWidth, height = contentFrameHeight)
        borderFrame.pack()
        borderFrame.grid_propagate(False)        
    
        # Height of frame that contains home button       
        homeButtonFrameHeight = 50
        # Width of the home button frame and the options frame
        optionsHomeWidth = 200

        # Frame to store the options users can interact with 
        # The size of the frame is calculated using the fixed size of the home frame
        optionsFrame = tk.Frame(borderFrame, width = optionsHomeWidth,\
            height = contentFrameHeight - homeButtonFrameHeight - borderSize, bg = "white")
        optionsFrame.grid(row = 0, column = 0) 
        optionsFrame.pack_propagate(False) 

        # Frame to store button to redirect user back to Introduction Screen
        # This frame should always be fixed in height
        homeButtonFrame = tk.Frame(borderFrame, height = homeButtonFrameHeight, width = optionsHomeWidth, bg = "white")
        homeButtonFrame.grid(row = 1, column = 0, pady = (2,0))
        homeButtonFrame.pack_propagate(False)
        
        # Updates sizes of frames
        self.view.update()

        # Distance between the widgets and the edge of the frame
        padding = 10

        # This is the frame where the actual option widgets are stored
        # This is needed or otherwise the formatting breaks for different devices
        self.optionsWidgetsFrame = tk.Frame(optionsFrame, bg = "white", width = optionsHomeWidth - padding,\
             height = optionsFrame.winfo_height())
        self.optionsWidgetsFrame.pack()
        self.optionsWidgetsFrame.pack_propagate(False)

        # Creates and places button in the centre of the frame
        tk.Button(homeButtonFrame, text = "Home.", font = (self.FONT, 12), width = 7, height = 1, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 
    
        # Width of canvas frame and algorithm info frame
        canvasAlgorithmInfoWidth = contentFrameWidth - optionsHomeWidth - borderSize

        # This frame stores the canvas that displays array
        canvasFrame = tk.Frame(borderFrame, height = contentFrameHeight - homeButtonFrameHeight - borderSize,\
            width = canvasAlgorithmInfoWidth, bg = "white")
        canvasFrame.grid(row = 0, column = 1, padx = (2,0)) 
        canvasFrame.pack_propagate(False)

        # Updates widths
        self.view.update()  

        # This canvas will be where the array is displayed.    
        self.arrayCanvas = tk.Canvas(canvasFrame, height = canvasFrame.winfo_height(), width = canvasFrame.winfo_width(), bg = "white") 
        self.arrayCanvas.pack()
        self.arrayCanvas.pack_propagate(False)

        # This frame will be where information on the algorithm will be displayed 
        self.algorithmInfoFrame = tk.Frame(borderFrame, height = 50, width = canvasAlgorithmInfoWidth, bg = "white")
        self.algorithmInfoFrame.grid(row = 1, column = 1, pady = (2,0), padx = (2,0)) 
        self.algorithmInfoFrame.pack_propagate(False)
        
        # Updates widths
        self.view.update()  
    
class Searching(Screen, SharedLayout):
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

        self.displayArray('1')
  
    # This functions handles creating and displaying the options the user is presented with
    def createOptions(self): 
        #combo box, allows the user to choose what algorithm they want
        algorithmOptions = ttk.Combobox(self.optionsWidgetsFrame, textvariable = tk.StringVar(), state = "readonly", font = (self.FONT, 12),\
             width = self.optionsWidgetsFrame.winfo_width())
        algorithmOptions['value'] = ('1',
                                     '2', 
                                     '3', 
                                     '4')
        algorithmOptions.set('Select an algorithm.')
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
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.FONT, 12), command = self.placeholder)\
            .grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.FONT, 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1)  

        tk.Button(self.optionsWidgetsFrame, text = "dsf", command = self.displayArray).pack()
        
    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
       
    # Display array on screen.
    # Iterates through array and draws bars on screen 
    def displayArray(self, value):
        if(int(value) < len(self.array)): self.deleteElements(int(value))
        if(len(self.array) == self.maxBars): return
        
        self.clearDisplayedArray()
        self.addElements(int(value))
        
        if(len(self.array) != self.maxBars): padding = self.calculatePadding()
        else: padding = self.padding
        
        yStretch = self.maximumPixels / max(self.array)
        for x, y in enumerate(self.array):
            x1 = x * self.barDist + x * self.barWidth + padding
            y1 = self.arrayCanvas.winfo_height() - (y * yStretch) 
            x2 = x * self.barDist + x * self.barWidth + self.barWidth + padding
            y2 = self.arrayCanvas.winfo_height() 
            self.arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = "Black")
        # I hate magic numbers 
        # print(3 / yStretch)
        print(len(self.array))
   
    # Wipes everything off the canvas
    def clearDisplayedArray(self):
        self.arrayCanvas.delete("all")

    # Adds amount of elements corresponding to the value
    def addElements(self, value):
        for i in range(len(self.array), value):
            self.array.append(random.randint(10,100)) 
    
    # Deletes number of elements corresponding to the value
    def deleteElements(self, value):
        for i in range(len(self.array), value - 1, -1):
            self.array.pop()

    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self):
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn  
        return self.arrayCanvas.winfo_height() - 2
    
    # Finds the best distance between the displayed array and the edges of canvas, 
    # to maximise the number of elements and centre the array as best as possible
    def calculateBestPadding(self):
        minPadding = 5
        maxPadding = 20
        for i in range(minPadding, maxPadding):
            # Calculates how many bars can be displayed on the screen 
            bars = self.calculateMaxBars(i)  
            # If the number of bars is a whole number
            if((bars).is_integer()):  
                # Maximum size the array can be
                self.maxBars = int(bars)
                # End function 
                return i
        # If no whole number can be found, just use the max padding (the array being off centre is less noticeable) 
        self.maxBars = round(self.calculateMaxBars(maxPadding))
        return maxPadding
       
    # Calculates maximum number of bars that can be displayed given the padding
    def calculateMaxBars(self, padding):
        return ((self.arrayCanvas.winfo_width()) - (padding * 2)) / (self.barWidth + self.barDist)

    # Calculates the padding to centre the array of a given size
    def calculatePadding(self):
        return ((self.arrayCanvas.winfo_width() - (len(self.array) * (self.barDist + self.barWidth))) // 2) + self.barDist
    
    def placeholder(self):
        print(self.array)
        print(len(self.array))
