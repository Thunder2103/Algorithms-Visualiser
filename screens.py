import tkinter as tk 
from tkinter import ttk
from abc import ABC, abstractmethod
import random

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
        # It is given a background of black to give the appearence that the different frames have borders, this prevents overlap issues
        OptionsHomeBorder = tk.Frame(contentFrame, bg = "black")
        OptionsHomeBorder.pack(side = "left", anchor = "n")

        # Frame to store options users can interact with
        self.optionsFrame = tk.Frame(OptionsHomeBorder, height = contentFrame.winfo_height() - 50, width = 195, bg = "white")
        self.optionsFrame.grid(row = 0, column = 0) 
        self.optionsFrame.pack_propagate(False)

        # Frame to store button to redirect user back to the Introduction Screen
        homeFrame = tk.Frame(OptionsHomeBorder, height = 50, \
            width = 195, bg = "white")
        homeFrame.grid(row = 1, column = 0, pady = 2)
        homeFrame.pack_propagate(False)

        # Updates widths - used to calculate other widgets widths
        self.view.updateIdleTasks()
      
        # Creates and places button in the centre of the frame
        tk.Button(homeFrame, text = "Home", font = ("Arial", 12), width = 7, height = 1, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 

        # This frame holds all the widgets, it used grid so that all the other frames can easily be positioned
        # It is given a background of black to give the appearence that the different frames have borders, this prevents overlap issues
        algorithmBorder = tk.Frame(contentFrame, bg = "black")
        algorithmBorder.pack(side = "right", anchor = "n")

        # Updates widths - used to calculate other widgets widths
        self.view.updateIdleTasks()

        # This frame will be where the array is displayed.
        # And and displays the algorithms steps
        self.displayFrame = tk.Frame(algorithmBorder, height = contentFrameHeight // 2, width = contentFrameWidth - self.optionsFrame.winfo_width() + 4, bg = "white")
        self.displayFrame.grid(row = 0, column = 0, padx = 2) 
        self.displayFrame.pack_propagate(False)
        
        # This frame will be where information on the algorithm will be displayed
        self.algorithmInfoFrame = tk.Frame(algorithmBorder, height = contentFrameHeight // 2, width = contentFrameWidth - 190, bg = "white")
        self.algorithmInfoFrame.grid(row = 2, column = 0, padx = 2, pady = 2) 
    
        # Updates widths
        self.view.updateIdleTasks()

    # getter methods, so Sorting and Searching Screens can place widgets
    def getOptionsFrame(self):
        return self.optionsFrame 
    
    def getdisplayFrame(self):
        return self.displayFrame
    
    def getAlgorithmInfoFrame(self):
        return self.algorithmInfoFrame 
    
# Ideally this should be the first screen the user sees 
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
        self.intArray = []

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
        # Creating and displaying options
        self.createOptions(layout)
        # intitalises the frame that shows all the elements the array includes
        self.createArrayFrame(layout)
        
    # This functions handles creating and displaying the options the user is presented with
    def createOptions(self, layout):
        # getting relevant frame 
        optionsFrame = layout.getOptionsFrame()
        #combo box, allows the user to choose what algorithm they want
        algorithmOptions = ttk.Combobox(optionsFrame, textvariable = tk.StringVar(), state = "readonly", width = 17, font = ("Arial", 12))
        algorithmOptions['value'] = ('1',
                                     '2', 
                                     '3', 
                                     '4')
        algorithmOptions.set('Select an algorithm.')
        algorithmOptions.pack(pady = (10,0))
                
        # Textbox allows user to enter a number to be added
        addElement = tk.Entry(optionsFrame, font = ("Arial italic", 12),width = 19,\
             highlightthickness = 2, highlightbackground = "black", highlightcolor= "black")
        # Default text
        addElement.insert(0, "Click to enter element.")
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        addElement.bind("<Button-1>", lambda event: self.deleteDefaultText(event, addElement))
        addElement.pack(pady = (15,0)) 
        
        # Button - confirm element to be added
        tk.Button(optionsFrame, text = "Add.", width = 7, font = ("Arial", 11), relief = "solid", command = lambda: self.add(layout, addElement))\
            .pack(pady = (2, 0), padx = 8, anchor = "e")

        # Randomly generate new array
        tk.Button(optionsFrame, text = "Generate.", relief = "solid", font = ("Arial", 12), width = 12, command = lambda: self.randomAdd(layout))\
            .pack(pady = (15,0), padx = 12)

        # Frame to store Clear and Delete buttons allows them to be arranged in a grid layout
        clearDeleteFrame = tk.Frame(optionsFrame, bg = "White")
        clearDeleteFrame.pack(pady = (15,0))

        # Allows user to clear the array
        tk.Button(clearDeleteFrame, text = "Clear.", relief = "solid", font = ("Arial", 12), width = 7, command = self.placeholder)\
            .grid(row = 0, column = 0, padx = 11)

        # Allows user to delete a single element from the end of the array
        tk.Button(clearDeleteFrame, text = "Delete.", relief = "solid", font = ("Arial", 12), width = 7, command = self.placeholder)\
            .grid(row = 0, column = 1, padx = 11)

        # Textbox, let's user choose what the search algorithms look for
        targetInput = tk.Entry(optionsFrame, width = 19, font = ("Arial italic", 12), \
            highlightthickness = 2, highlightbackground = "black", highlightcolor= "black")
        # Default text
        targetInput.insert(0, "Click to enter target.") 
        # Binds event to textbox, deleteDefaultText() is called when the textbox is clicked
        targetInput.bind("<Button-1>", lambda event: self.deleteDefaultText(event, targetInput))
        targetInput.pack(pady = (15,0), padx = 5) 

        # Button - confirms target
        tk.Button(optionsFrame, text = "Set target.", width = 9, font = ("Arial", 11), relief = "solid", command = self.placeholder)\
            .pack(pady = (2, 0), padx = 8, anchor = "e")
            
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        self.speedSlider = tk.Scale(optionsFrame, from_ = 0, to_ = 2, length = 175,\
                                orient = "horizontal", showvalue = False, bg =  "white", highlightbackground = "white", command = self.intToSpeed)
        self.speedSlider.pack()  
        # Initially the slider is set at 0, which is the Slow speed
        self.speedSlider.config(label = "Slow") 

        # Makes sure there is enough space for extra options
        tk.Label(optionsFrame, text = "Filler for extra options", font = ("Arial", 12)).pack(pady = 15)

        # Frame to store stop and solve buttons in a grid layout
        stopSolveFrame = tk.Frame(optionsFrame, bg = "white")
        stopSolveFrame.pack(side = "bottom")
        # Allows user to see the algorithm in action
        tk.Button(stopSolveFrame, text = "Solve.", width = 7, relief = "solid", font = ("Arial", 12), command = self.placeholder)\
            .grid(row = 0, column = 0, pady = (0,15), padx = 11) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        tk.Button(stopSolveFrame, text = "Stop.", width = 7, relief = "solid", font = ("Arial", 12), state = "disabled", command = self.placeholder)\
            .grid(row = 0, column = 1, pady = (0,10), padx = 11) 
    
    # Creates the frame that stores the numbers in the array
    # A seperate frame is used as it will be easier to prevent the array from extending past displayFrame
    def createArrayFrame(self, layout):
        displayFrame = layout.getdisplayFrame()
        # Stored as attribute so it can be accessed by add(), randomAdd(), deleteElement() and clearArray() methods
        self.arrayFrame = tk.Frame(displayFrame, bg = "White")
        self.arrayFrame.pack(pady = 15)
        
    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])  
    
    # Placeholder function, just prints the array
    def placeholder(self):
        print(self.intArray) 

    # Input texboxes have default text
    # When a textbox is clicked for the first time the default text is deleted
    def deleteDefaultText(self, event, textbox):
        textbox.delete(0, tk.END)
        # Removes the italic font 
        textbox.config(font = ("Arial")) 
        # Unbind event - so user input isn't deleted whenever they click the textbox
        textbox.unbind("<Button-1>") 

    # Adds user typed element to the array
    def add(self, layout, textbox):
        # Needed to check if array is within bounds of the display frame
        displayFrame = layout.getdisplayFrame()
        # Value user entered 
        element = textbox.get()
        # By default border colour is set to red - signifies user has not entered an integer
        borderColour = "red"
        # if string user inputted is a number
        if(element.isnumeric() and self.arrayFrame.winfo_width() < (displayFrame.winfo_width() - 50)):  
            # The length of the integer array is used to decide what column the element is stored in arrayFrame
            elementColumn = len(self.intArray)
            # label containing element, added to next column of array frame
            label = tk.Label(self.arrayFrame, text = element, font = ("Arial", 12), bg = "white")
            # adds label with element to the window
            label.grid(row = 0, column = elementColumn) 
            # set border colour to black
            borderColour = "black"
            # Cast string to int and add to array
            self.intArray.append(int(element))
            #clears textbox when number is successfully added
            textbox.delete(0, tk.END) 
        # updates width of array frame - important to prevent array from extending past display Frame
        self.view.updateIdleTasks()
        # Sets border colour of textbox - easy way to tell user if what they inputted was valid or not  
        textbox.config(highlightbackground = borderColour, highlightcolor= borderColour) 
    
    def randomAdd(self, layout):
        # call function to clear array otherwise stuff will get messef up
        
        # Needed to check if array is within bounds of the display frame
        displayFrame = layout.getdisplayFrame()
        i = 0
        arraySize = random.randint(5, 75) 

        while(i < arraySize and self.arrayFrame.winfo_width() < displayFrame.winfo_width() - 50):
            element = random.randint(0, 100)
            self.intArray.append(element)
            tk.Label(self.arrayFrame, text = element, bg = "white", font = ("Arial", 12)).grid(row = 0, column = i)
            self.view.updateIdleTasks()
            i += 1  
        
        print(self.arrayFrame.winfo_width())




    
        







        


