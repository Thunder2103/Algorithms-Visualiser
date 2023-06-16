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

        #array to be searched
        self.array = []

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
        algorithmOptions = ttk.Combobox(optionsFrame, textvariable = tk.StringVar(), state = "readonly", width = 17, font = ("Arial", 13))
        algorithmOptions['value'] = ('1',
                                     '2', 
                                     '3', 
                                     '4')
        algorithmOptions.set('Select an algorithm.')
        algorithmOptions.pack(pady = (10,0))
                
        # Textbox allows user to enter a number to be added
        addElement = tk.Entry(optionsFrame, font = ("Arial italic", 13),width = 19,\
             highlightthickness = 2, highlightbackground = "black", highlightcolor= "black")
        # Default text
        addElement.insert(0, "Click to enter element.")
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        addElement.bind("<Button-1>", lambda event: self.deleteDefaultText(event, addElement))
        addElement.pack(pady = (15,0)) 
        
        # Button - confirm element to be added
        tk.Button(optionsFrame, text = "Add.", width = 7, font = ("Arial", 11), relief = "solid", command = lambda: self.add(addElement, addElement.get()))\
            .pack(pady = (2, 0), padx = 12, anchor = "e")

        # Randomly generate new array
        tk.Button(optionsFrame, text = "Generate.", relief = "solid", font = ("Arial", 12), width = 13, command = self.placeholder)\
            .pack(pady = (15,0), padx = 12)

        # Frame to store Clear and Delete buttons allows them to be arranged in a grid layout
        clearDeleteFrame = tk.Frame(optionsFrame, bg = "White")
        clearDeleteFrame.pack(pady = (15,0))

        # Allows user to clear the array
        tk.Button(clearDeleteFrame, text = "Clear.", relief = "solid", font = ("Arial", 11), width = 7, command = self.placeholder)\
            .grid(row = 0, column = 0, padx = 11)

        # Allows user to delete a single element from the end of the array
        tk.Button(clearDeleteFrame, text = "Delete.", relief = "solid", font = ("Arial", 11), width = 7, command = self.placeholder)\
            .grid(row = 0, column = 1, padx = 11)

        # Textbox, let's user choose what the search algorithms look for
        targetInput = tk.Entry(optionsFrame, width = 19, font = ("Arial italic", 13), relief = "solid")
        # Default text
        targetInput.insert(0, "Click to enter target.") 
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        targetInput.bind("<Button-1>", lambda event: self.deleteDefaultText(event, targetInput))
        targetInput.pack(pady = (15,0), padx = 5) 

        # Button - confirms target
        tk.Button(optionsFrame, text = "Target.", width = 7, font = ("Arial", 11), relief = "solid", command = self.placeholder)\
            .pack(pady = (2, 0), padx = 12, anchor = "e")
            
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(optionsFrame, from_ = 0, to_ = 2, length = 175,\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack()  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        # Makes sure there is enough space for extra options
        tk.Label(optionsFrame, text = "Filler for extra options", font = ("Arial", 13)).pack(pady = 15)

        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(optionsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom")
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = ("Arial", 13), command = self.placeholder)\
            .grid(row = 0, column = 0, pady = (0,15), padx = 11) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = ("Arial", 13), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1, pady = (0,15), padx = 11) 

    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
    
    # Placeholder function, just prints the array
    def placeholder(self):
        print(self.array) 

    # Input texboxes have default text
    # When a textbox is clicked for the first time the default text is deleted
    def deleteDefaultText(self, event, textbox):
        textbox.delete(0, tk.END)
        # Removes the italic font 
        textbox.config(font = ("Arial")) 
        # Unbind event - so user input isn't deleted whenever they click the textbox
        textbox.unbind("<Button-1>") 

    # Adds user types element to array
    def add(self, textbox, element):
        # By default border colour is set to red - signifies user has not entered an integer
        borderColour = "red"
        # if string user inputted is a nuumber
        if(element.isnumeric()): 
            # set border colour to black
            borderColour = "black"
            # Cast string to int and add to array
            self.array.append(int(element))
            #clears textbox when number is successfully added
            textbox.delete(0, tk.END)
        
        # Sets border colour of textbox - easy way to tell user if what they inputted was valid or not 
        textbox.config(highlightbackground = borderColour, highlightcolor= borderColour)
        







        


