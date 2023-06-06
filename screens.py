import tkinter as tk 
from tkinter import ttk
from abc import ABC, abstractmethod

# If the file is run as is message is returned and program exits
if(__name__ == "__main__"): 
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

# Abstract class - every screen must implement the layout method
class Screen(ABC):
    @abstractmethod
    def createLayout(self, contentFrame):
        pass 

# Searching and Sorting Screens both use the same basic layout
# This class delegates the reponsiblity of creating the basic layout
class SharedLayout(Screen):
    def __init__(self, view):
        self.view = view 
    
    def createLayout(self, contentFrame):
        # Python OOP doesn't have private attributes but using getter functions make it easier to read
        contentFrameHeight = self.view.getFrameHeight()
        contentFrameWidth = self.view.getFrameWidth()
        
        # This frame holds all the widgets, it uses grid so that all the other frames can easily be positioned
        # It is given a background of black to give the appearence that the different frames have borders preventing overlap issues
        OptionsHomeFrame = tk.Frame(contentFrame, bg = "black")
        OptionsHomeFrame.pack(side = "left", anchor = "n")

        # Frame to store options users can interact with
        self.options = tk.Frame(OptionsHomeFrame, height = contentFrameHeight - 75, width = contentFrameWidth - 535, bg = "white")
        self.options.grid(row = 0, column = 0) 
        self.options.pack_propagate(False)
    
        # Frame to store button to redirect user back to the Introduction Screen
        home = tk.Frame(OptionsHomeFrame, height = 75, width = contentFrameWidth - 535, bg = "white")
        home.grid(row = 1, column = 0, pady = 2)
        home.pack_propagate(False)
        
        # Creates and places button in the centre of the frame
        tk.Button(home, text = "Home", font = ("Arial", 12), width = 10, height = 2, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 

        # This frame holds all the widgets, it used grid so that all the other frames can easily be positioned
        # It is given a background of black to give the appearence that the different frames have borders preventing overlap issues
        algorithmFrame = tk.Frame(contentFrame, bg = "black")
        algorithmFrame.pack(side = "right", anchor = "n")

        # This frame will be where the array is displayed.
        # And and displays the algorithms steps
        self.arrayDisplay = tk.Frame(algorithmFrame, height = contentFrameHeight // 2, width = contentFrameWidth - 200, bg = "white")
        self.arrayDisplay.grid(row = 0, column = 0, padx = 2) 
        
        # This frame will be where information on the algorithm will be displayed
        self.algorithmInfoFrame = tk.Frame(algorithmFrame, height = contentFrameHeight // 2, width = contentFrameWidth - 200, bg = "white")
        self.algorithmInfoFrame.grid(row = 2, column = 0, padx = 2, pady = 2) 
    
    # getter methods, so Sorting and Searching Screens can place widgets
    def getOptionsFrame(self):
        return self.options 
    
    def getArrayFrame(self):
        return self.arrayDisplay
    
    def getAlgorithmInfoFrame(self):
        return self.algorithmInfoFrame 
    
# Ideally this should be first screen the user sees 
class Introduction(Screen):
    def __init__(self, view):
        # Stores reference to view object - so clearScreen() function can be called
        self.view = view

    def createLayout(self, contentFrame):
        # The introductory text is kept as a string 
        # as it makes it easier to change (and makes code easier to read)
        introText = "This program visualises different algorithms in a user friendly way. \n\
        Including array searching, sorting and tree traversal algorithms. \n\
        Press one of the buttons to start."

        # Header label
        tk.Label(contentFrame, text = "Welcome to Algorithms Anonymous.", font = ("Arial", 18, "underline"), bg = "white")\
            .pack(pady = 10)

        # Label that contains the introduction text
        tk.Label(contentFrame, text = introText, font = ("Arial", 14), justify = "center", bg = "white")\
            .pack(pady = 5)

        # Adds a frame for the buttons widgets 
        # Adding this frame makes positioning the buttons much easier
        buttonsFrame = tk.Frame(contentFrame, bg = "white")
        buttonsFrame.pack()

        tk.Button(buttonsFrame, text = "Tree Traversal", font = ("Arial", 12), height = 2, width = 15, relief = "solid")\
            .pack(pady = (25, 0)) 

        tk.Button(buttonsFrame, text = "Searching",  font = ("Arial", 12), height = 2, width = 15, relief = "solid", \
                command = lambda : [self.view.removeScreen(), self.view.addScreen(Searching(self.view))]).pack(side = "left", pady = 15, padx = (100, 0))

        tk.Button(buttonsFrame, text = "Sorting",  font = ("Arial", 12), height = 2, width = 15, relief = "solid",\
                command = lambda : self.view.removeScreen()).pack(side = "left", padx = 100) 

        tk.Label(contentFrame, text = "Created by Thomas Gibson", bg = "white", justify = "left")\
            .pack(side = "bottom", anchor = "w", pady = 10, padx = 10)  

class Searching(Screen):
    def __init__(self, view):
         # Stores reference to view object - so clearScreen() function can be called
        self.view = view 

        # Object stores the dictionary pairing numbers to speed
        # This allows the slider to show "Small", "Medium" and "Fast" instead of 0, 1, 2
        self.numbersToSpeed = {
            0: "Slow",
            1: "Medium",
            2: "Fast"
        }  
       
    def createLayout(self, contentFrame):
        # Creating the basic layout of the Sorting Screen
        layout = SharedLayout(self.view)
        layout.createLayout(contentFrame) 

        # Getting relevant frames
        optionsFrame = layout.getOptionsFrame() 
        arrayFrame = layout.getArrayFrame()
        algorithmInfoFrame = layout.getAlgorithmInfoFrame()
        
        #combo box, allows the user to choose what algorithm they want
        algorithmOptions = ttk.Combobox(optionsFrame, textvariable = tk.StringVar(), state = "readonly", width = 20)
        algorithmOptions['value'] = ('1',
                                     '2', 
                                     '3', 
                                     '4')
        algorithmOptions.set('Select an algorithm...')
        algorithmOptions.pack(pady = (5,0))
        
        # Randomly generate new array
        tk.Button(optionsFrame, text = "Generate.", relief = "solid", command = self.placeholder).pack(pady = (5,0))

        
        # Textbox and button to allow user to add a number to the array
        # A seperate frame is used to position the textbox and button on the same line as it doesn't mess everything up
        addElementFrame = tk.Frame(optionsFrame, bg = "white")
        addElementFrame.pack()
        addElement = tk.Text(addElementFrame, width = 10, height = 1, font = ("Arial", 12), relief = "solid").grid(row = 0, column = 0, pady = (5,0)) 
        tk.Button(addElementFrame, text = "Add.", command = self.placeholder, width = 5, relief = "solid").grid(row = 0, column = 1, pady = (5, 0), padx = (10, 0))

        # Allows user to delete a single element from the end of the array
        tk.Button(optionsFrame, text = "Delete.", relief = "solid", command = self.placeholder).pack(pady = (5,0))
    
        # Allows user to clear the array
        tk.Button(optionsFrame, text = "Clear.", relief = "solid", command = self.placeholder).pack(pady = (5,0))
        
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(optionsFrame, from_ = 0, to_ = 2, length = 150,\
                                orient = "horizontal", showvalue = False, command = self.intToSpeed)
        self.speedSlider.pack(pady = (5,0))  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        # Allows user to see the algorithm in action
        tk.Button(optionsFrame, text = "Solve.", relief = "solid", command = self.placeholder).pack(side = "bottom", pady = (0,5))

    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
    
    # Placeholder function, doesn't do anything
    def placeholder(self):
        pass 






        


