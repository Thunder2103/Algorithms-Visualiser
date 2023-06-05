import tkinter as tk 
from abc import ABC, abstractmethod

# If the file is run as is message is returned and program exits
if(__name__ == "__main__"): 
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

# Abstract class - every screen must implement the layout method
class Screen(ABC):
    @abstractmethod
    def layout(self, contentFrame):
        pass
    
# Ideally this should be first screen the user sees 
class Introduction(Screen):
    def __init__(self, view):
        # Stores reference to view object - so clearScreen() function can be called
        self.view = view


    def layout(self, contentFrame):
    
        contentFrame.config(bg = "white")

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
       
    def layout(self, contentFrame):
        # Python OOP doesn't have private attributes but using getter functions make it easier to read
        contentFrameHeight = self.view.getFrameHeight()
        contentFrameWidth = self.view.getFrameWidth()
        
        # This frame holds all the widgets, it used grid so that all the other frames can easily be positioned
        OptionsHomeFrame = tk.Frame(contentFrame, bg = "black")
        OptionsHomeFrame.pack(side = "left", anchor = "n")

        options = tk.Frame(OptionsHomeFrame, height = contentFrameHeight - 75, width = contentFrameWidth - 535, bg = "white")
        options.grid(row = 0, column = 0) 

        # Frame to store button to redirect user back to the Introduction Screen
        home = tk.Frame(OptionsHomeFrame, height = 75, width = contentFrameWidth - 535, bg = "white")
        home.grid(row = 1, column = 0, pady = 2)
        home.pack_propagate(False)
        
        # Creates and places button in the centre of the frame
        tk.Button(home, text = "Home", font = ("Arial", 12), width = 10, height = 2, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.addScreen(Introduction(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 

        # This frame holds all the widgets, it used grid so that all the other frames can easily be positioned
        algorithmFrame = tk.Frame(contentFrame, bg = "black")
        algorithmFrame.pack(side = "right", anchor = "n")

        arrayDisplay = tk.Frame(algorithmFrame, height = contentFrameHeight // 2, width = contentFrameWidth - 200, bg = "white")
        arrayDisplay.grid(row = 0, column = 0, padx = 2) 
        
        algorithmInfoFrame = tk.Frame(algorithmFrame, height = contentFrameHeight // 2, width = contentFrameWidth - 200, bg = "white")
        algorithmInfoFrame.grid(row = 2, column = 0, padx = 2, pady = 2)

 



     
           
        
        # Creates a slider that goes 0 to 1 then 2
        # It has three options correlating to the three speeds; slow, medium, fast 
        # Every time the sliders value is changed the intToSpeed() method is called
        # self.speedSlider = tk.Scale(contentFrame, from_ = 0, to_ = 2, length = 150,\
        #                        orient = "horizontal", showvalue = False, command = self.intToSpeed)
        # self.speedSlider.pack()  
        # Initially the slider is set at 0, which is the Slow speed
        #self.speedSlider.config(label = "Slow") 

        

    # When the slider has changed value a label is added with the relevant speed
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])




        


