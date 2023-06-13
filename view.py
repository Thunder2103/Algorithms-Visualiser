import tkinter as tk

# If the file is run as is message is returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


# View Class - Creates a blank tkinter window
class View():
    def __init__(self, width, height):
        # This prevents screens being made smaller than 750x500
        if(width < 750 or height < 500):
            self.width = 750
            self.height = 500
        else:
            self.width = width
            self.height = height  
    
    def create(self):
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

        # Set minimum size
        self.window.minsize(750, 500)
        
        #changed window colour to grey 
        # gives window solid black border
        self.window.config(bg = "#CCCCCC", borderwidth = 2, relief = "solid")
        
        # This gives the appearance that the content frame has a border
        # There are built in hyperparamters for adding a border but this caused issues with widgets being centred
        tk.Frame(self.window, bg = "black", width = self.contentFrameWidth + 4, height = self.contentFrameHeight + 4).place(relx = 0.5, rely = 0.5, anchor = "center")

        # Declaring and customising the frame
        # This is where all the displayed content 
        self.contentFrame = tk.Frame(self.window, height = self.contentFrameHeight, width = self.contentFrameWidth, bg = "white")
        
        # Makes the frame centred in the GUI window
        self.contentFrame.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Stops frame resizing to same size as widgets inside it 
        self.contentFrame.pack_propagate(False) 

    # Draws window
    def show(self):
        self.window.mainloop() 
 
    # Takes in a new object (the new screen) and calls the relevant function
    def addScreen(self, newScreen):
        newScreen.createLayout() 

    # Removes every widget from the passed frame
    def removeScreen(self): 
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    def update(self):
        self.window.update() 

    def getContentFrame(self):
        return self.contentFrame
        
    def getContentFrameHeight(self):
        return self.contentFrameHeight 

    def getContentFrameWidth(self):
        return self.contentFrameWidth 
    
