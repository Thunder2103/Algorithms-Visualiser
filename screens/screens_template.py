# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc
import tkinter as tk 

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

        # Current size of bars
        self.barWidth = 15
        # Smallest bars can be 
        self.minBarWidth = 2
        # Largest bar can be 
        self.maxBarWidth = 15
        # Distance between each bar 
        self.barDist = 2
        # Maximum and minimum distance between displayed array and edge of canvas
        self.minPadding = 5
        self.maxPadding = 20

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
             command = lambda: [self.view.removeScreen(), self.view.addScreen(sc.Introduction(self.view))])\
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