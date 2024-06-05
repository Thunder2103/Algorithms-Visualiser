# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import screens as sc 
import tkinter as tk 
from tkinter import ttk 
from .traversal_controller import TraversalController
from .traversal_model import TraversalModel

class TraversalScreen(sc.Screen, sc.ScreenTemplate): 
    def initScreen(self) -> None:
        self.createTemplate() 

        # Create model class
        self.__model = TraversalModel() 
        # Create controller class and add referencces to screen and model
        self.__controller = TraversalController(self, self.__model)
        # Add reference to controller to the model object
        self.__model.addController(self.__controller)
        # Add event handlers to the canvas
        self.__controller.addCanvasEvents() 
        # Create the options users can interact with 
        self.__createOptions()  
        
    # Creates the widgets that allows users to toggle the visualisers settings
    def __createOptions(self) -> None: 
        self.__createAlgorithmOptions() 
        self.__createSpeedAdjuster()
        self.__createAddNodeButton()
        self.__createAddEdgeOption()
        self.__createStopSolveButtons()

    # Create the combo box that displays the algorithms users can see visualised 
    def __createAlgorithmOptions(self) -> None:
        # combo box, allows the user to choose what algorithm they want
        self.__algorithmOptions = ttk.Combobox(self.getOptionsWidgetFrame(), textvariable = tk.StringVar(), 
                                               state = "readonly", font = (self.getFont(), self.getFontSize()),\
             width = self.getOptionsWidgetFrame().winfo_width())
        self.__algorithmOptions.set('Select an algorithm.')
        # Removes the blue highlighting when something is selected that annoyed me
        self.__algorithmOptions.bind("<<ComboboxSelected>>", lambda _: self.getOptionsWidgetFrame().focus())
        self.__algorithmOptions.pack(pady = (10,0)) 
    
    # Creates a slider that allows users to adjust an algorithms speed
    def __createSpeedAdjuster(self) -> None:
        # Creates a slider that goes from the maximum delay to the minmum delay 
        # Every time the sliders value is changed the updatetDelay() method is called to update the value seen on screen
        self.__speedSlider = tk.Scale(self.getOptionsWidgetFrame(), from_ = self.__model.getMaxDelay(), 
                                      to_ = self.__model.getMinDelay(), resolution=self.__model.getResolution(), 
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
        self.__addNodeButton = tk.Button(self.getOptionsWidgetFrame(), text="Add a Node.", width=12, relief="solid", 
                  font = (self.getFont(), self.getFontSize()), command=self.__controller.spawnNode)
        self.__addNodeButton.pack(pady = (10, 0)) 
        
    # Changes the text colour of the add nodes button to the passed colour
    def changeNodeButtonColour(self, colour : str) -> None: 
        self.__addNodeButton.config(fg = colour)

    # Creates options to add edges or edit existing ones
    def __createAddEdgeOption(self) -> None: 
        # Frame containing widgets for adding an option
        self.__edgeNodesFrame = tk.Frame(self.getOptionsWidgetFrame()) 
        # Display frame on screen
        self.__edgeNodesFrame.pack(pady=(10, 0))  

        # Calls functions to create add edge options 
        self.__createNodeEdgeLabels() 
        self.__createEdgeWeightOption() 
        self.__createEdgeDirectionOptions() 
        self.__createAddEdgeButton()

    # Create options that display nodes an edge connects
    def __createNodeEdgeLabels(self) -> None:
        self.__createLabel(self.__edgeNodesFrame, text="From").grid(row=0, column=0) 
        
        # Label that will contain ID of node the edge starts at
        self.__nodeFromLabel = self.__createLabel(self.__edgeNodesFrame, width=6)
        self.__nodeFromLabel.grid(row=0, column=1)
        # Underline underneath label
        tk.Frame(background="black").place(in_=self.__nodeFromLabel, x=0, rely=1.0, height=2, relwidth=1.0)

        self.__createLabel(self.__edgeNodesFrame, text="To").grid(row=0, column=2)
        # Label that will contain ID of node the edge ends at
        self.__nodeToLabel = self.__createLabel(self.__edgeNodesFrame, width=6)
        self.__nodeToLabel.grid(row=0, column=3) 
        # Underline underneath label
        tk.Frame(background="black").place(in_=self.__nodeToLabel, x=0, rely=1.0, height=2, relwidth=1.0)

    # Create option to let user input an edges weight/cost
    def __createEdgeWeightOption(self) -> None:
        # Frame to store entry widget to let users to enter an edges weight
        self.__edgeWeightFrame = tk.Frame(self.getOptionsWidgetFrame(), background="white") 
        self.__edgeWeightFrame.pack(pady=(7,0))
        self.__createLabel(self.__edgeWeightFrame, text="Weight:").grid(row=0, column=0)

        # Entry field user types text in to set an edges weight 
        self.__weightInputField = tk.Entry(self.__edgeWeightFrame, width=13, relief="solid", 
                                           font=(self.getFont(), self.getFontSize())) 
        # Placeholder text
        self.__weightInputField.insert(0, "Type Here...")  
        # Binds event to clear text on mouse click
        self.__weightInputField.bind("<Button-1>", lambda _: self.__clearEntryText())
        self.__weightInputField.grid(row=0, column=1, padx=(5, 5))

    # Create option to decide if edge is directed/undirected
    def __createEdgeDirectionOptions(self) -> None:
        # Add Radio buttons for directed and undirected edges 
        self.__radioButtonFrame = tk.Frame(self.getOptionsWidgetFrame(), background="white")
        self.__radioButtonFrame.pack(pady=(5, 0))
        # Stores the value of the currently selected radio button
        self.__edgeType = tk.IntVar() 
        # Radio Button to indicate edge is undirected
        self.__createRadioButton(self.__radioButtonFrame, "Undirected", 0).grid(row=0, column=0)
        # Radio Button to indicate edge is directed 
        self.__createRadioButton(self.__radioButtonFrame, "Directed", 1).grid(row=0, column=1) 
    
    # Create button to add edge 
    def __createAddEdgeButton(self):
        tk.Button(self.getOptionsWidgetFrame(), text = "Add Edge.", width = 10, relief = "solid", 
                                           font=(self.getFont(), self.getFontSize()), command=self.__addEdge)\
                                            .pack(pady=(5, 0))

    # Wrapper function to create a Radio Button
    def __createRadioButton(self, frame : tk.Frame, text : str, value:int) -> tk.Radiobutton: 
        return tk.Radiobutton(frame, text=text, background="white", 
                       variable=self.__edgeType, value=value, font=(self.getFont(), 11))

    # Wrapper function for making labels 
    def __createLabel(self, frame : tk.Frame, text : str = "", width : int = 0) -> tk.Label:  
        label = tk.Label(frame, text=text, width=width, background="white", 
                        font=(self.getFont(), self.getFontSize()))  
        if(width): label.config(width=width)
        return label

    # Clears text in the edge weight entry field
    def __clearEntryText(self): 
        self.__weightInputField.delete(0, "end")
    
    # Adds edge 
    def __addEdge(self): 
        if(self.__nodeFromLabel.cget("text") == "" or self.__nodeToLabel.cget("text") == ""): 
            return
    
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
    
    # Changes colour of the given circle to the colour specified
    def changeCircleColour(self, circle : int, colour : str) -> None: 
        self.getCanvas().itemconfig(circle, fill = colour)

# Listen to Can't Stop by The Red Hot Chili Peppers 