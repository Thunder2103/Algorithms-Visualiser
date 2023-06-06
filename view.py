import tkinter as tk

# If the file is run as is message is returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()


# View Class - Creates a blank tkinter window
class View():
    def __init__(self, width, height):

        # The screen was made with a ratio of 750x500 and works best at this ratio
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
        self.frameWidth = self.width - 15
        self.frameHeight = self.height - 15
        
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

        # Declaring and customising the frame
        # This is where all the displayed content 
        self.contentFrame = tk.Frame(self.window, height = self.frameHeight, width = self.frameWidth, borderwidth = 2, relief = "solid", bg = "white")
        
        # Makes the frame centred in the GUI window
        self.contentFrame.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Stops frame resizing to same size as widgets inside it 
        self.contentFrame.pack_propagate(False) 

    def show(self):
        # Draws window
        self.window.mainloop()
      
    # Takes in a new object (the new screen) and calls the relevant function
    def addScreen(self, newScreen):
        newScreen.createLayout(self.contentFrame)

    # Removes every widget from the passed frame
    def removeScreen(self): 
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        
    def getFrameHeight(self):
        return self.frameHeight 

    def getFrameWidth(self):
        return self.frameWidth