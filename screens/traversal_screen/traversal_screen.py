# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc 
import tkinter as tk 
from tkinter import Event
from tkinter import ttk 
from .traversal_controller import TaversalController
from .traversal_model import TraversalModel
from  canvas_node import CanvasNode


class TraversalScreen(sc.Screen, sc.ScreenTemplate): 
    def initScreen(self) -> None:
        self.createTemplate() 

        # Create model class
        self.__model = TraversalModel() 
        # Create controller class and add referencces to screen and model
        self.__controller = TaversalController(self, self.__model)
        # Add reference to controller to the model object
        self.__model.addController(self.__controller) 
        # Create the options users can interact with 
        self.__createOptions()

    # Creates the widgets that allows users to toggle the visualisers settings
    def __createOptions(self) -> None: 
        self.__createAlgorithmOptions() 
        self.__createSpeedAdjuster()
        self.__createAddNodeButton()
        self.__createStopSolveButtons()

    # Create the combo box that displays the algorithms users can see visualised 
    def __createAlgorithmOptions(self) -> None:
        # combo box, allows the user to choose what algorithm they want
        self.__algorithmOptions = ttk.Combobox(self.getOptionsWidgetFrame(), textvariable = tk.StringVar(), state = "readonly", font = (self.getFont(), self.getFontSize()),\
             width = self.getOptionsWidgetFrame().winfo_width())
        self.__algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        self.__algorithmOptions.bind("<<ComboboxSelected>>", lambda _: self.getOptionsWidgetFrame().focus())
        self.__algorithmOptions.pack(pady = (10,0)) 
    
    # Creates a slider that allows users to adjust an algorithms speed
    def __createSpeedAdjuster(self) -> None:
        # Creates a slider that goes from the maximum delay to the minmum delay 
        # Every time the sliders value is changed the updatetDelay() method is called to update the value seen on screen
        self.__speedSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = self.__model.getMaxDelay(), to_ = self.__model.getMinDelay(), resolution=self.__model.getResolution(), 
                                      length = self.getOptionsWidgetFrame().winfo_width(), orient = "horizontal", showvalue = False, 
                                      bg =  "white", highlightbackground = "white", command = self.__updateDelay)
        self.__speedSlider.pack(pady = (10, 0))  
        self.__speedSlider.set(self.__model.getMaxDelay())
        # When the user stops moving the slider the slider is updated in the DataModel class 
        self.__speedSlider.bind("<ButtonRelease-1>", lambda _ : self.__setDelay()) 
     
    def __updateDelay(self, value : str) -> None:
        self.__speedSlider.config(label = f"Delay: {value} Milliseconds")  

    def __setDelay(self) -> None:
        pass   

    # Creates the button that lets users add nodes to the canvas 
    def __createAddNodeButton(self) -> None: 
        tk.Button(self.getOptionsWidgetFrame(), text="Add a Node.", width=12, relief="solid", 
                  font = (self.getFont(), self.getFontSize()), command=self.__spawnNode).pack(pady = (10, 0))

    # Draws a circle (node) on the canvas 
    def __spawnNode(self):  
        canvas = self.getCanvas() 
        initialX, initialY = self.__model.getInitialCoords()
        circle = canvas.create_oval(initialX, initialX, initialY, initialY, outline = "black", fill="blue")  
        # Add event to let nodes change colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Enter>", lambda _: self.__changeColourOnHover(circle))
        canvas.tag_bind(circle, "<Leave>", lambda _: self.__changeColourOnLeave(circle)) 
        # Add event listener to move node when it's dragged by the mouse 
        canvas.tag_bind(circle, "<B1-Motion>", lambda event: self.__moveNode(event, circle))
        
        # Updates screen so node can be seen onscreen
        self.getWindow().update()
        
    def __moveNode(self, event : Event, circle : int) -> None: 
        # Radius of the nodes
        circleRadius = self.__model.getRadius()    
        # Offset to keep center of circle underneath mouse  
        circleOffset = circleRadius // 2 
        # Space that should exist between nodes 
        spaceBetweenNodes = self.__model.getSpaceBetweenNodes()

        circleCoords = (self.getCanvas().coords(circle)) 

  
        # Checks if mouse has gone out of bounds to the left 
        # Stops the node from moving off the canvas
        xCoord = max(event.x - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds to the right 
        # Stops the node from moving off the canvas
        xCoord = min(xCoord, self.getCanvas().winfo_width() - self.__model.getCanvasUpperBoundOffset() - circleRadius) 

        # Checks if mouse has gone out of bounds by going above the canvas
        # Stops the node from moving off the canvas 
        yCoord = max(event.y - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds by going below the canvas
        # Stops the node from moving off the canvas 
        yCoord = min(yCoord, self.getCanvas().winfo_height() - self.__model.getCanvasUpperBoundOffset() - circleRadius)
     
        # The above could be done in one line but just because it can doesn't mean it should 
        # Doing it in one line would make the calculations very hard to read  


        # Checks if the node is going to collide with the node to it's left 
        if(self.__isCollision(circle, xCoord, yCoord, 
                              xCoord + circleRadius + spaceBetweenNodes, yCoord + circleRadius)):  
            return
        if(self.__isCollision(circle, xCoord - spaceBetweenNodes, yCoord, 
                              xCoord + circleRadius, yCoord + circleRadius)): 
            return
        if(self.__isCollision(circle, xCoord, yCoord, 
                              xCoord + circleRadius, yCoord + circleRadius + spaceBetweenNodes)):  
            return
        if(self.__isCollision(circle, xCoord, yCoord - spaceBetweenNodes, 
                              xCoord + circleRadius, yCoord + circleRadius)): 
            return
            


        # Moves center of the circle to the coordinates specified 
        self.getCanvas().moveto(circle, xCoord, yCoord) 
        # Updates screen so node can be seen onscreen
        self.getWindow().update()
  
    # Checks if node is going to intersect with another node 
    def __isCollision(self, circle : int, x :int, y : int, x2 : int, y2: int) -> bool: 
        overlapping =  self.getCanvas().find_overlapping(x, y , x2, y2) 
        numOverlapping = len(overlapping)
        return True if numOverlapping > 1 or (numOverlapping == 1 and circle not in overlapping) else False



    # Changes the nodes colour the mouse is hovering to red
    def __changeColourOnHover(self, circle): 
        self.getCanvas().itemconfig(circle, fill="red") 
    
    # Changes the mouse stops hovering over a node it's colour is set to blue 
    def __changeColourOnLeave(self, circle):
        self.getCanvas().itemconfig(circle, fill="blue") 

    # Creates buttons that lets user execute algorithms or stop them
    def __createStopSolveButtons(self) -> None:
        # Frame to store stop and solve buttons in a grid layout
        algorithmToggleFrame = tk.Frame(self.getOptionsWidgetFrame(), bg = "white")
        algorithmToggleFrame.pack(side = "bottom", pady = (0,5))
        # Allows user to see the algorithm in action
        self.__solveStopButton = tk.Button(algorithmToggleFrame, text = "Solve.", width = 7, relief = "solid", 
                                           font = (self.getFont(), self.getFontSize()))
        self.__solveStopButton.grid(row = 0, column = 0, padx = (0,5)) 
        # Allows user to stop algorithm whilst it's running - button is initially disabled
        self.__pauseResumeButton = tk.Button(algorithmToggleFrame, text = "Pause.", width = 7, relief = "solid", 
                                             font = (self.getFont(), self.getFontSize()), state = "disabled")
        self.__pauseResumeButton.grid(row = 0, column = 1)  

# Listen to Can't Stop by The Red Hot Chili Peppers 