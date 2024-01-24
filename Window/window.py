import tkinter as tk

# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


# Window Class - Creates a blank tkinter window
class Window():
    def __init__(self, width : int, height : int) -> None:
        # Variables to store minimum width and height - means they can be easily changed
        minWidth = 750 
        minHeight = 500
        # This prevents screens being made smaller than 750x500
        if(width < minWidth or height < minHeight):
            self.width = minWidth
            self.height = minHeight
        else:
            self.width = width
            self.height = height  
    
    def create(self) -> None:
        # Dimensions for the frame all widgets stored in
        # Stored as attributes so they can be accessed by other objects later
        self.contentFrameWidth = self.width - 20
        self.contentFrameHeight = self.height - 20
        
        # Declaring window
        self.window = tk.Tk()
        self.window.title('Useful Algorithms')

        # windows dimensions
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.resizable(False, False) 

        #changed window colour to grey 
        # gives window solid black border
        self.window.config(bg = "#CCCCCC", borderwidth = 2, relief = "solid")
        
        # Size of border
        borderSize = 2

        # This gives the appearance that the content frame has a border
        # There are built in hyperparamters for adding a border but this caused issues with widgets being centred
        tk.Frame(self.window, bg = "black", width = self.contentFrameWidth + (borderSize * 2),\
            height = self.contentFrameHeight + (borderSize * 2)).place(relx = 0.5, rely = 0.5, anchor = "center")

        # Declaring and customising the frame
        # This is where all the displayed content 
        self.contentFrame = tk.Frame(self.window, height = self.contentFrameHeight, width = self.contentFrameWidth, bg = "white")
        
        # Makes the frame centred in the GUI window
        self.contentFrame.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Stops frame resizing to same size as widgets inside it 
        self.contentFrame.pack_propagate(False) 

    # Draws window
    def show(self) -> None:
        self.window.mainloop() 
 
    # Takes in a new object (the new screen) and calls the relevant function
    def addScreen(self, newScreen ) -> None:
        newScreen.initScreen()

    # Removes every widget from the passed frame
    def removeScreen(self) -> None: 
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    def update(self) -> None:
        self.window.update() 

    def getContentFrame(self) -> tk.Frame:
        return self.contentFrame
        
    def getContentFrameHeight(self) -> int:
        return self.contentFrameHeight 

    def getContentFrameWidth(self) -> int:
        return self.contentFrameWidth 
    
