# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import Screen_Templates as st
import Searching as sc
import tkinter as tk 

# Ideally this should be the first screen the user sees 
class IntroductionScreen(st.Screen):
    def __init__(self, window):
        # Stores reference to Window object
        self.window = window
        self.FONT = "Arial"

    # Creates the screen
    def initScreen(self) -> None:
        # Get content Frame to store all widgets
        self.contentFrame = self.window.getContentFrame()
        self.createTitle()
        self.createIntroParagraph()
        self.createNavigationButtons()

    # Creates the title displaying the projects name
    def createTitle(self) -> None:
        # Header label
        tk.Label(self.contentFrame, text = "Welcome to Algorithms Anonymous.", font = (self.FONT, 18, "underline"), bg = "white")\
            .pack(pady = 10) 

    # Create introduction paragraph
    def createIntroParagraph(self) -> None:
        # The introductory text is kept as a string 
        # as it makes it easier to change (and makes code easier to read)
        introText = "This program visualises different algorithms in a user friendly way. \n\
        Including array searching, sorting and tree traversal algorithms. \n\
        Press one of the buttons to start."
        # Label that contains the introduction text
        tk.Label(self.contentFrame, text = introText, font = (self.FONT, 14), justify = "center", bg = "white")\
            .pack(pady = 5) 
    
    # Creates buttons that allow users to navigate the rest of the project
    def createNavigationButtons(self) -> None:
        # Adds a frame for the buttons widgets 
        # Adding this frame makes positioning the buttons much easier
        buttonsFrame = tk.Frame(self.contentFrame, bg = "white")
        buttonsFrame.pack()
        # Navigate to path finding algorithms screen
        tk.Button(buttonsFrame, text = "Path Finding", font = (self.FONT, 12), height = 2, width = 15, relief = "solid")\
            .pack(pady = (25, 0))  
        # Navigate to array searching screen
        tk.Button(buttonsFrame, text = "Array Searching",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid", \
                command = lambda : [self.window.removeScreen(), self.window.loadScreen(sc.SearchScreen(self.window))]).pack(side = "left", pady = 15, padx = (100, 0)) 
        # Navigate to array sorting screen
        tk.Button(buttonsFrame, text = "Array Sorting",  font = (self.FONT, 12), height = 2, width = 15, relief = "solid",)\
            .pack(side = "left", padx = 100) 
        tk.Label(self.contentFrame, text = "Created by Thomas Gibson", bg = "white", justify = "left")\
            .pack(side = "bottom", anchor = "w", pady = 5, padx = 5) 