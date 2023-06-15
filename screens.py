import tkinter as tk 
from tkinter import ttk
from abc import ABC, abstractmethod
import random

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
        self.barWidth = 5
        # Distance between each bar 
        self.barDist = 2 
    
    def createTemplate(self):
        # Get content Frame to store all widgets
        contentFrame = self.view.getContentFrame()
        # Get content frames width and height
        contentFrameHeight = self.view.getContentFrameHeight()
        contentFrameWidth = self.view.getContentFrameWidth()
        
        # This black frame will give the appearence that every frame inside it has a border - prevents overlapping issues
        OptionsHomeBorder = tk.Frame(contentFrame, bg = "black")
        OptionsHomeBorder.pack(side = "left", anchor = "n")

        # Frame to store options users can interact with 
        # The size of the frame is calculated using the fixed size of the home frame
        self.optionsFrame = tk.Frame(OptionsHomeBorder, height = contentFrame.winfo_height() - 50, width = 195, bg = "white")
        self.optionsFrame.grid(row = 0, column = 0) 
        self.optionsFrame.pack_propagate(False)

        # Frame to store button to redirect user back to the Introduction Screen 
        # This frame is always a fixed size, this is used to calculate the size of the options frame
        homeFrame = tk.Frame(OptionsHomeBorder, height = 50, \
            width = 195, bg = "white")
        homeFrame.grid(row = 1, column = 0, pady = 2)
        homeFrame.pack_propagate(False)

        # Updates widths - used to calculate other widgets widths
        self.view.update()
      
        # Creates and places button in the centre of the frame
        tk.Button(homeFrame, text = "Home", font = (self.FONT, 12), width = 7, height = 1, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 

        # This black frame will give the appearence that every frame inside it has a border - prevents overlapping issues
        algorithmBorder = tk.Frame(contentFrame, bg = "black")
        algorithmBorder.pack(side = "right", anchor = "n")

        # Updates widths - used to calculate other widgets widths
        self.view.update()

        # Height of the canvas and algorithm info frame 
        # Minus two takes into account the two pixels used by the border frame
        canvasFrameHeight = (contentFrameHeight // 2) - 2
        # Width of the canvas and the border
        # Minus six takes into account the 6 pixels used taken up by the border frames
        canvasFrameWidth = (contentFrameWidth - self.optionsFrame.winfo_width()) - 6

        # This canvas will be where the array is displayed.    
        self.arrayCanvas = tk.Canvas(algorithmBorder, height = canvasFrameHeight, width = canvasFrameWidth, bg = "white") 
        self.arrayCanvas.grid(row = 0, column = 0, padx = 2)
        self.arrayCanvas.pack_propagate(False)

        # This frame will be where information on the algorithm will be displayed 
        self.algorithmInfoFrame = tk.Frame(algorithmBorder, height = canvasFrameHeight, width = canvasFrameWidth + 4, bg = "white")
        self.algorithmInfoFrame.grid(row = 1, column = 0, pady = 2, padx = 2) 
        self.algorithmInfoFrame.pack_propagate(False)
       
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

        tk.Button(buttonsFrame, text = "Tree Traversal", font = (self.FONT, 12), height = 2, width = 15, relief = "solid")\
            .pack(pady = (25, 0)) 

        tk.Button(buttonsFrame, text = "Searching",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid", \
                command = lambda : [self.view.removeScreen(), self.view.addScreen(Searching(self.view))]).pack(side = "left", pady = 15, padx = (100, 0))

        tk.Button(buttonsFrame, text = "Sorting",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid",\
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
        self.largestNumber = self.calculateLargestNumber()
        
        # Calculates spacing between canvas border and displayed array 
        self.padding = self.calculatePadding()
        
    # This functions handles creating and displaying the options the user is presented with
    def createOptions(self):
        #combo box, allows the user to choose what algorithm they want
        algorithmOptions = ttk.Combobox(self.optionsFrame, textvariable = tk.StringVar(), state = "readonly", width = 17, font = (self.FONT, 12))
        algorithmOptions['value'] = ('1',
                                     '2', 
                                     '3', 
                                     '4')
        algorithmOptions.set('Select an algorithm.')
        algorithmOptions.pack(pady = (10,0))
                
        # Textbox allows user to enter a number to be added
        addElement = tk.Entry(self.optionsFrame, font = (f'{self.FONT} italic', 12),width = 19,\
             highlightthickness = 2, highlightbackground = "black", highlightcolor= "black")
        # Default text
        addElement.insert(0, "Click to enter element.")
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        addElement.bind("<Button-1>", lambda event: self.deleteDefaultText(event, addElement))
        addElement.pack(pady = (15,0)) 
        
        # Button - confirm element to be added
        tk.Button(self.optionsFrame, text = "Add.", width = 7, font = (self.FONT, 11), relief = "solid", command = self.add)\
            .pack(pady = (2, 0), padx = 8, anchor = "e")

        # Randomly generate new array
        tk.Button(self.optionsFrame, text = "Generate.", relief = "solid", font = (self.FONT, 12), width = 12, command = self.randomAdd)\
            .pack(pady = (15,0), padx = 12)

        # Frame to store Clear and Delete buttons allows them to be arranged in a grid layout
        clearDeleteFrame = tk.Frame(self.optionsFrame, bg = "White")
        clearDeleteFrame.pack(pady = (15,0))

        # Allows user to clear the array
        tk.Button(clearDeleteFrame, text = "Clear.", relief = "solid", font = (self.FONT, 12), width = 7, command = self.clear)\
            .grid(row = 0, column = 0, padx = 11)

        # Allows user to delete a single element from the end of the array
        tk.Button(clearDeleteFrame, text = "Delete.", relief = "solid", font = (self.FONT, 12), width = 7, command = self.delete)\
            .grid(row = 0, column = 1, padx = 11)

        # Textbox, let's user choose what the search algorithms look for
        targetInput = tk.Entry(self.optionsFrame, width = 19, font = (f'{self.FONT} italic', 12), \
            highlightthickness = 2, highlightbackground = "black", highlightcolor= "black")
        # Default text
        targetInput.insert(0, "Click to enter target.") 
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        targetInput.bind("<Button-1>", lambda event: self.deleteDefaultText(event, targetInput))
        targetInput.pack(pady = (15,0), padx = 5) 

        # Button - confirms target
        tk.Button(self.optionsFrame, text = "Set target.", width = 9, font = (self.FONT, 11), relief = "solid", command = self.placeholder)\
            .pack(pady = (2, 0), padx = 8, anchor = "e")
            
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(self.optionsFrame, from_ = 0, to_ = 2, length = 175,\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack()  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        # Makes sure there is enough space for extra options
        tk.Label(self.optionsFrame, text = "Filler for extra options", font = (self.FONT, 12)).pack(pady = 15)

        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(self.optionsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom")
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = (self.FONT, 12), command = self.placeholder)\
            .grid(row = 0, column = 0, pady = (0,15), padx = 11) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = (self.FONT, 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1, pady = (0,15), padx = 11) 
        
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

    # Adds the number if user typed to the array
    def add(self): 
        pass
    
    # Generates a random array 
    def randomAdd(self):
        # Generates random array
        # The maximum value is the one calculated from the calculateLargestNumber() method
        self.array = [random.randint(1, self.largestNumber) for i in range(0, self.maxBars)]
        for x,y in enumerate(self.array): 
            x1 = x * self.barDist + x * self.barWidth + self.padding
            y1 = self.arrayCanvas.winfo_height() - y 
            x2 = x * self.barDist + x * self.barWidth + self.barWidth + self.padding
            y2 = self.arrayCanvas.winfo_height() 
            arrayCanvas.create_rectangle(x1, y1, x2, y2, fill = "black")     
        print(self.array)
    # Removes all elements from the array and clears the screen
    def clear(self): 
        pass
    
    # Delete a single element from the array
    def delete(self): 
        pass 

    # Largest number that can be displayed on screen
    def calculateLargestNumber(self):
        return self.arrayCanvas.winfo_height() - 6 
    
    # Calculates the best distance between displayed array and borders of canvas
    # Makes displayed array look as centred as possible
    def calculatePadding(self):
        minPadding = 5 
        maxPadding = 21 
        for i in range(minPadding, maxPadding):
            # Calculates how many bars can be displayed on the screen 
            bars = self.calculateMaxBars(i)
            # If the number of bars is a while number
            if((bars).is_integer()): 
                self.maxBars = int(bars)
                return i 
                
    # Calculates maximum number of bars that can be displayed given the padding
    def calculateMaxBars(self, padding):
        return ((self.arrayCanvas.winfo_width()) - padding * 2) / (self.barWidth + self.barDist)
