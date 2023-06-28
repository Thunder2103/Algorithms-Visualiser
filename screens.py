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

        # Target is initially set to none 
        self.target = None 
    
    def createTemplate(self):
        # Get content Frame to store all widgets
        contentFrame = self.view.getContentFrame()
        # Get content frames width and height
        contentFrameHeight = self.view.getContentFrameHeight()
        contentFrameWidth = self.view.getContentFrameWidth()
       
        # This black frame will give the appearence that every frame inside it has a border - prevents overlapping issues
        optionsHomeBorder = tk.Frame(contentFrame, bg = "black", width = 202, height = contentFrameHeight)
        optionsHomeBorder.pack(side = "left")
        optionsHomeBorder.grid_propagate(False)
        
        self.view.update()

        # Frame to store button to redirect user back to Introduction Screen
        # This frame should always bee fixed in size
        homeFrame = tk.Frame(optionsHomeBorder, height = 50, width = optionsHomeBorder.winfo_width() - 2, bg = "white")
        homeFrame.grid(row = 1, column = 0, pady = (2,0))

        # Updates widths - used to calculate other widgets widths
        self.view.update() 

        # Frame to store options users can interact with 
        # The size of the frame is calculated using the fixed size of the home frame
        optionsFrame = tk.Frame(optionsHomeBorder, width = optionsHomeBorder.winfo_width() - 2,\
            height = optionsHomeBorder.winfo_height() - homeFrame.winfo_height(), bg = "white")
        optionsFrame.grid(row = 0, column = 0) 
        optionsFrame.pack_propagate(False) 

        # Updates widths - used to calculate other widgets widths
        self.view.update() 

        # This is the frame where the actual option widgets are stored
        # This is needed or otherwise the formatting breaks for different devices
        self.optionsWidgetsFrame = tk.Frame(optionsFrame, bg = "white", width = optionsFrame.winfo_width() - 10,\
             height = optionsFrame.winfo_height())
        self.optionsWidgetsFrame.pack()
        self.optionsWidgetsFrame.pack_propagate(False)

        # Updates widths - used to calculate other widgets widths
        self.view.update() 
      
        # Creates and places button in the centre of the frame
        tk.Button(homeFrame, text = "Home", font = (self.FONT, 12), width = 7, height = 1, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 

        # Updates widths - used to calculate other widgets widths
        self.view.update()

        # This black frame will give the appearence that every frame inside it has a border - prevents overlapping issues
        algorithmBorder = tk.Frame(contentFrame, bg = "black", height = contentFrameHeight, width = contentFrameWidth - optionsHomeBorder.winfo_width())
        algorithmBorder.pack()
        algorithmBorder.grid_propagate(False)

        # Updates widths - used to calculate other widgets widths
        self.view.update()
     
        # Width of the canvas and the algorithm info frame
        canvasFrameWidth = algorithmBorder.winfo_width()

        # Height of the canvas and algorithm info frame 
        # If the height of the border frame is even then 
        if(algorithmBorder.winfo_height() % 2 == 0):
            canvasFrameHeight = algorithmBorder.winfo_height() // 2
            algorithmInfoHeight = algorithmBorder.winfo_height() // 2 - 2
        else:
            canvasFrameHeight = algorithmBorder.winfo_height() // 2 + 1
            algorithmInfoHeight = algorithmBorder.winfo_height() // 2
        

        # This frame will be where information on the algorithm will be displayed 
        canvasFrame = tk.Frame(algorithmBorder, height = canvasFrameHeight, width = canvasFrameWidth, bg = "white")
        canvasFrame.grid(row = 0, column = 0, pady = (0,2)) 
        canvasFrame.pack_propagate(False)

        # This frame will be where information on the algorithm will be displayed 
        self.algorithmInfoFrame = tk.Frame(algorithmBorder, height = algorithmInfoHeight, width = canvasFrameWidth, bg = "white")
        self.algorithmInfoFrame.grid(row = 1, column = 0) 
        self.algorithmInfoFrame.pack_propagate(False)
       
        # Updates widths
        self.view.update()

        # This canvas will be where the array is displayed.    
        self.arrayCanvas = tk.Canvas(canvasFrame, height = canvasFrame.winfo_height(), width = canvasFrame.winfo_width(), bg = "white") 
        self.arrayCanvas.pack()
        self.arrayCanvas.pack_propagate(False)

        # Updates widths
        self.view.update()  
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
            .pack(side = "bottom", anchor = "w", pady = 10, padx = 10)  

class Searching(Screen, SharedLayout):
    def initScreen(self):
        # Creates basic layout of the screen
        self.createTemplate()
    
        # Creating and displaying options
        self.createOptions() 

        # Calculates largest number that can be displayed on screen
        self.maximumPixels = self.calculateMaximumPixels()
        # Calculates spacing between canvas border and displayed array 
        self.padding = self.calculateBestPadding()
        
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
        algorithmOptions.pack(pady = (5,0))
                
        # Textbox allows user to enter a number to be added
        addElement = tk.Entry(self.optionsWidgetsFrame, font = (f'{self.FONT} italic', 12),\
            highlightbackground = "black", highlightcolor= "black", highlightthickness = 2, width = self.optionsWidgetsFrame.winfo_width())
        # Default text
        addElement.insert(0, "Click to enter element.")
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        addElement.bind("<Button-1>", lambda event: self.deleteDefaultText(event, addElement))
        addElement.pack(pady = (5,0))
        
        # Button - confirm element to be added
        tk.Button(self.optionsWidgetsFrame, text = "Add.", font = (self.FONT, 11), relief = "solid", command = lambda: self.add(addElement))\
            .pack(anchor = "e", pady = (3, 0))

        # Randomly generate new array
        tk.Button(self.optionsWidgetsFrame, text = "Generate.", width = 11, relief = "solid", font = (self.FONT, 12), command = self.randomGenerate)\
            .pack(pady = (5, 0))

        # Frame to store Clear and Delete buttons allows them to be arranged in a grid layout
        clearDeleteFrame = tk.Frame(self.optionsWidgetsFrame, bg = "White")
        clearDeleteFrame.pack(pady = (5, 0))

        # Allows user to clear the array
        tk.Button(clearDeleteFrame, text = "Clear.", width = 7, relief = "solid", font = (self.FONT, 12), command = self.clear)\
            .grid(row = 0, column = 0, padx = (0,5))

        # Allows user to delete a single element from the end of the array
        tk.Button(clearDeleteFrame, text = "Delete.", width = 7, relief = "solid", font = (self.FONT, 12), command = self.delete)\
            .grid(row = 0, column = 1)


        # Textbox, let's user choose what the search algorithms look for
        targetInput = tk.Entry(self.optionsWidgetsFrame, font = (f'{self.FONT} italic', 12), \
            highlightbackground = "black", highlightcolor= "black", highlightthickness = 2, width = self.optionsWidgetsFrame.winfo_width())
        # Default text
        targetInput.insert(0, "Click to enter target.") 
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        targetInput.bind("<Button-1>", lambda event: self.deleteDefaultText(event, targetInput))
        targetInput.pack(pady = (5,0)) 

        # Button - confirms target
        tk.Button(self.optionsWidgetsFrame, text = "Set target.", font = (self.FONT, 11), relief = "solid", command = lambda: self.setTarget(targetInput))\
           .pack(anchor = "e", pady = (3,0))
            
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(self.optionsWidgetsFrame, from_ = 0, to_ = 2, length = 175,\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack()  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        # Makes sure there is enough space for extra options
        #tk.Label(self.optionsFrame, text = "Filler for extra options", font = (self.FONT, 12)).pack()

        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(self.optionsWidgetsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.FONT, 12), command = self.placeholder)\
            .grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.FONT, 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1) 
        
    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
    
    # Input texboxes have default text
    # When a textbox is clicked for the first time the default text is deleted
    def deleteDefaultText(self, event, textbox):
        textbox.delete(0, tk.END)
        # Removes the italic font 
        textbox.config(font = (self.FONT)) 
        # Unbind event - so user input isn't deleted whenever they click the textbox
        textbox.unbind("<Button-1>")  
    
    # Adds the number the user typed to the array and displays updated array
    def add(self, textbox):  
        # Get user input 
        element = textbox.get()
        # Border colour set to red by default - signifies an error  
        borderColour = "red"
        # isnumeric() filters out non-integer inputs and negatives
        # the second check makes sure the input is smaller than or equal to the largest number
        if(element.isnumeric() and int(element) <= self.maximumPixels):  
            # If the maximum amount of elements hasn't been reached - new element is added
            if(len(self.array) < self.maxBars):  
                # Border colour set to black - signifies element has been added to array and displayed on screen 
                borderColour = "black"
                # Add new element to array
                self.array.append(int(element))
                # Clear whatevers on screen 
                self.arrayCanvas.delete('all')
                # If the array is now at maximum size, can just use padding calculated by calculatePadding() method
                if(len(self.array) == self.maxBars): self.displayArray(self.padding)
                # Otherwise display array with newly calulated padding
                else: self.displayArray(self.calculatePadding())
        # Sets textbox colour to whatever borderColour has been set to 
        textbox.config(highlightbackground = borderColour, highlightcolor = borderColour)

    # Generates a random array and displayes it
    def randomGenerate(self):
        # Clear array and whatever is displayed on screen before generating new array
        self.clear() 
        # The length of the array is no greater than the maximum number of bars calculated by the calculatePadding() method
        arraySize = random.randint(1, self.maxBars)
        # Generates random array
        # The largest value that can be in the array is calculated from the calculateLargestNumber() method 
        self.array = [random.randint(1, self.maximumPixels) for i in range(0, arraySize)]  
        # If the array is now at maximum size, can just use padding calculated by calculatePadding() method 
        if(len(self.array) == self.maxBars): self.displayArray(self.padding)
        # Otherwise display array with newly calulated padding
        else: self.displayArray(self.calculatePadding()) 
     
    # Removes all elements from the array and clears the screen
    def clear(self): 
        self.arrayCanvas.delete('all')
        self.array.clear()
    
    # Delete a single element from the array
    def delete(self): 
        # Can't delete anything if array is empty
        if(len(self.array) == 0): return 
        # Remove last element from array
        self.array.pop()
        # Clear array displayed on screen
        self.arrayCanvas.delete('all')
        # Redraw array
        self.displayArray(self.calculatePadding()) 
    
    # Sets element algorithms will search for
    def setTarget(self, textbox):
        # Gets user input
        target = textbox.get() 
        # Sets border colour to red - signifies an error
        borderColour = "red"
        # Checks if inputted value is a number
        if(target.isnumeric()):
            # Sets border colour to black - signifies that target successfully set
            borderColour = "black"
            # Stores target
            self.target = target
        # Sets textbox colour to whatever borderColour has been set to 
        textbox.config(highlightbackground = borderColour, highlightcolor = borderColour)


    
    # Display array on screen.
    # Iterates through array and draws bars on screen 
    def displayArray(self, padding):
        largestElement = max(self.array)
        print(largestElement)
        for x,y in enumerate(self.array): 
            x1 = x * self.barDist + x * self.barWidth + padding
            y1 = largestElement - y 
            x2 = x * self.barDist + x * self.barWidth + self.barWidth + padding
            y2 = self.arrayCanvas.winfo_height() 
            self.arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = "black") 

    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self):
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

    # Calculates the padding to centre the array of any size
    def calculatePadding(self):
        return ((self.arrayCanvas.winfo_width() - (len(self.array) * (self.barDist + self.barWidth))) // 2) + self.barDist
    
    def placeholder(self):
        print(self.array)
        print(len(self.array))
