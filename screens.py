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
    
        # The introductory text is kept as a string 
        # as it makes it easier to change (and makes code easier to read)
        introText = "This program visualises algorithms in a user friendly way. \n\
        Including array searching and sorting and tree traversal algorithms. \n\
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
       
        self.speedSlider = tk.Scale(contentFrame, from_ = 0, to_ = 2, length = 200,\
                                orient = "horizontal", showvalue = False, command = self.intToSpeed)
        self.speedSlider.pack()  
        self.speedSlider.config(label = "Slow")
    
    def intToSpeed(self, value): 
        self.speedSlider.config(label = self.numbersToSpeed[int(value)])


        


