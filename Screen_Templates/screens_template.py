# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import Introduction_Screen as isc
import tkinter as tk 

# All screens that visualise the algorithms have the same fundamental layout
# This class delegates the reponsiblity of creating the basic layout
class SharedLayout():
    def __init__(self, view) -> None:
        # Stores reference to view object
        self.view = view  
        # Font every widget uses 
        self.FONT = "Arial"
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

    def createTemplate(self) -> None:
        # Get content Frame to store all widgets
        contentFrame = self.view.getContentFrame()
        # Get content frames width and height
        contentFrameHeight = self.view.getContentFrameHeight()
        contentFrameWidth = self.view.getContentFrameWidth()

        # width of the border
        borderSize = 2
        # Distance between the widgets and the edge of the frame
        padding = 10
        # Height of frame that contains home button       
        homeButtonFrameHeight = 50
        # Width of the home button frame and the options frame
        optionsHomeWidth = 200
        # Width of canvas frame
        canvasFrameWidth = contentFrameWidth - optionsHomeWidth - borderSize 
        # Height of canvas frame
        canvasFrameHeight = contentFrameHeight - homeButtonFrameHeight - borderSize

        # Border frame gives appearence of a border between different frames
        borderFrame = self.createBorderFrame(contentFrame, contentFrameWidth, contentFrameHeight)
        # Frame to store the options users can interact with 
        # The size of the frame is calculated using the fixed size of the home frame
        optionsFrame = self.createOptionsFrame(borderFrame, optionsHomeWidth, contentFrameHeight - homeButtonFrameHeight - borderSize)
        # Frame to store button to redirect user back to Introduction Screen
        # This frame should always be fixed in height
        homeButtonFrame = self.createHomeButtonFrame(borderFrame, optionsHomeWidth, homeButtonFrameHeight)
        # Updates sizes of frames
        self.view.update()

        # This is the frame where the actual option widgets are stored
        self.createOptionWidget(optionsFrame, optionsHomeWidth - padding, optionsFrame.winfo_height())
        # Creates a home button so user can navigate back to the intro screen
        self.createHomeButton(homeButtonFrame)
        # This frame stores the canvas that displays array
        canvasFrame = self.createCanvasFrame(borderFrame, canvasFrameWidth, canvasFrameHeight)
        # Updates widths
        self.view.update()  
        # Creates canvas to display the array 
        self.createArrayCanvas(canvasFrame, canvasFrame.winfo_width(), canvasFrame.winfo_height())
        # This frame will be where information on the algorithm will be displayed 
        self.createAlgorithmIntoFrame(borderFrame, canvasFrameWidth, 50)
        # Updates widths
        self.view.update()  

    # Creates frame to display the border
    def createBorderFrame(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> tk.Frame:
        # Border frame gives appearence of a border between different frames
        borderFrame = tk.Frame(root, bg = "black", width = frameWidth, height = frameHeight)
        borderFrame.pack()
        borderFrame.grid_propagate(False)    
        return borderFrame     

    # Creates frame to display the options
    def createOptionsFrame(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> tk.Frame:
        # Frame to store the options users can interact with 
        # The size of the frame is calculated using the fixed size of the home frame
        optionsFrame = tk.Frame(root, width = frameWidth,\
            height = frameHeight, bg = "white")
        optionsFrame.grid(row = 0, column = 0) 
        optionsFrame.pack_propagate(False) 
        return optionsFrame

    # Creates frame to display the home button
    def createHomeButtonFrame(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> tk.Frame:
        # Frame to store button to redirect user back to Introduction Screen
        # This frame should always be fixed in height
        homeButtonFrame = tk.Frame(root, width = frameWidth, height = frameHeight, bg = "white")
        homeButtonFrame.grid(row = 1, column = 0, pady = (2,0))
        homeButtonFrame.pack_propagate(False)
        return homeButtonFrame 
    
    # Creates widget to store options, prevents formatting from breaking on different devices 
    def createOptionWidget(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> None:
        # This is the frame where the actual option widgets are stored
        # This is needed or otherwise the formatting breaks for different devices
        self.optionsWidgetsFrame = tk.Frame(root, bg = "white", width = frameWidth,\
             height = frameHeight)
        self.optionsWidgetsFrame.pack()
        self.optionsWidgetsFrame.pack_propagate(False)
    
    # Creates the button to let the user navigate back to the main menu
    def createHomeButton(self, root : tk.Frame) -> None: 
        # Creates and places button in the centre of the frame
        tk.Button(root, text = "Home.", font = (self.FONT, 12), width = 7, height = 1, borderwidth = 2, relief = "solid",\
             command = lambda: [self.view.removeScreen(), self.view.loadScreen(isc.IntroductionScreen(self.view))])\
                .place(relx = 0.5, rely = 0.5, anchor = "center") 
    
    # Creates the frame to store the canvas
    def createCanvasFrame(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> tk.Frame:
        # This frame stores the canvas that displays array
        canvasFrame = tk.Frame(root, width = frameWidth, height = frameHeight, bg = "white")
        canvasFrame.grid(row = 0, column = 1, padx = (2,0)) 
        canvasFrame.pack_propagate(False)
        return canvasFrame
    
    # Creates canvas to display the array
    def createArrayCanvas(self, root : tk.Frame, canvasWidth : int, canvasHeight : int) -> None:
         # This canvas will be where the array is displayed.    
        self.arrayCanvas = tk.Canvas(root, width = canvasWidth, height = canvasHeight, bg = "white") 
        self.arrayCanvas.pack()
        self.arrayCanvas.pack_propagate(False)
    
    # Creates frame to store the algorithm information
    def createAlgorithmIntoFrame(self, root : tk.Frame, frameWidth : int, frameHeight : int) -> None:
        # This frame will be where information on the algorithm will be displayed 
        self.algorithmInfoFrame = tk.Frame(root, width = frameWidth, height = frameHeight, bg = "white")
        self.algorithmInfoFrame.grid(row = 1, column = 1, pady = (2,0), padx = (2,0)) 
        self.algorithmInfoFrame.pack_propagate(False) 


