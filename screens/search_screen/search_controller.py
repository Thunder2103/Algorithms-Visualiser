# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import random 

class SearchController():
    def __init__(self, screen) -> None:
        self.screen = screen
         # Current size of bars
        self.__barWidth = 15
        # Smallest bars can be 
        self.__minBarWidth = 2
        # Largest bar can be 
        self.__maxBarWidth = 15
        # Distance between each bar 
        self.__barDist = 2
        # Maximum and minimum distance between displayed array and edge of canvas
        self.__minPadding = 5
        self.__maxPadding = 20
        self.__array = []
        # Lower bound 
        self.__randomLow = 100
        # Highest value that can appear in array
        self.__randomHigh = 5000
        # Returns the height of the canvas - maximum number of pixels an element can possibly have
        self.__maximumPixels = self.calculateMaximumPixels()
        # Calculates spacing between canvas border and displayed array 
        # Is also used to calculate the largest possible size of the array
        self.__minPadding = self.calculateBestPadding()
        self.calculateArrayBounds()

    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self) -> int:
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn   
        return self.screen.getArrayCanvas().winfo_height() - 2 

    # Finds the best distance between the displayed array and the edges of canvas, 
    # to maximise the number of elements and centre the array as best as possible
    def calculateBestPadding(self) -> int:
        for i in range(self.__minPadding, self.__maxPadding):
            # Calculates how many bars can be displayed on the screen 
            bars = self.calculateMaxBars(self.__minBarWidth, i)  
            # If the number of bars is a whole number
            if((bars).is_integer()):  
                # Maximum size the array can be
                self.__maxBars = int(bars)
                # Function terminates - returning the best padding (i)
                return i
        # If no whole number can be found, just use the max padding (the array being off centre is less noticeable) 
        self.__maxBars = round(self.calculateMaxBars(self.__minBarWidth, self.__maxPadding))
        return self.__maxPadding

    # Calculates maximum number of bars that can be displayed given the padding
    def calculateMaxBars(self, barWidth, padding) -> int:
        return ((self.screen.getArrayCanvas().winfo_width()) - (padding * 2)) / (barWidth + self.__barDist)

    # Calculates the padding to centre the array of a given size
    def calculatePadding(self) -> int:
        return ((self.screen.getArrayCanvas().winfo_width() - (len(self.__array) * (self.__barDist + self.__barWidth))) // 2) + self.__barDist
    
    # Adjusts size of bars so amount of elements can fit on screen and stay in the canvas' centre
    def adjustArray(self, value : str) -> None:
        # If the value given from the scrollbar is less than the arrays size
        # Delete elements from the array and check if bar size can increase
        if(int(value) < len(self.__array)): 
            self.deleteElements(int(value))
            self.increaseBarSize()
        # Otherwise add elements to the array and check is bar size needs to decrease
        else: 
            self.addElements(int(value))
            self.decreaseBarSize()
        # If the array size is less than the maximum number of bars. 
        # Calculate padding 
        if(len(self.__array) != self.__maxBars): self.__padding = self.calculatePadding()
        # If the array size is now at maximum size, 
        # padding is the value calulated by the calculateBestPadding() method
        else: self.__padding = self.__minPadding
        
        # The amount each elements is stretched along the y-axis 
        # Means the elements are scaled with the largest element
        self.yStretch = self.__maximumPixels / max(self.__array)
        # Draw the actual array with all the adjustments made
        # Since there is no algorithm active, all bars are drawn as black
        self.displayArray("Black")
        
    # Iterates through array, drawing each bar
    # The function has two default arguements -> currentIndex and altColour both initialised to None
    def displayArray(self, defaultColour, currentIndex = None, altColour = None) -> None:
            # Clear displayed array on screen
            self.clearDisplayedArray()
            for x, y in enumerate(self.__array):
                # Calculate where each bar is placed on screen
                # Bottom left co-ord
                x1 = x * self.__barDist + x * self.__barWidth + self.__padding
                # Top left coord
                y1 = self.screen.getArrayCanvas().winfo_height() - (y * self.yStretch)  
                # Bottom right coord
                x2 = x * self.__barDist + x * self.__barWidth + self.__barWidth + self.__padding
                # Top right coord
                y2 = self.screen.getArrayCanvas().winfo_height() 
                # Chooses correct colour for bar to be filled in with
                if x == currentIndex: self.screen.getArrayCanvas().create_rectangle(x1, y1, x2, y2, fill = altColour) 
                else: self.screen.getArrayCanvas().create_rectangle(x1, y1, x2, y2, fill = defaultColour) 
            # Updates screen so bars can be seen onscreen
            self.screen.getWindow().update()
      
    # Wipes everything off the canvas
    def clearDisplayedArray(self) -> None:
        self.screen.getArrayCanvas().delete("all")

    # Adds amount of elements corresponding to the value
    def addElements(self, value):
        for _ in range(len(self.__array), value):
            # Choose random number inbetween upper and lower bounds
            self.__array.append(random.randint(self.__lowerBound, self.__upperBound)) 
    
    # Deletes number of elements corresponding to the value
    def deleteElements(self, value) -> None:
        for _ in range(len(self.__array), value, -1):
            self.__array.pop()

    # Determines if bars need to shrink in size as array grows
    def decreaseBarSize(self) -> None:
        for i in range(self.__barWidth, self.__minBarWidth, -1):
            if(len(self.__array) < round(self.calculateMaxBars(i, self.__maxPadding))):
                self.__barWidth = i
                return
        self.__barWidth = self.__minBarWidth
     
    # Determines if bars needs to increase in size as array shrinks
    def increaseBarSize(self) -> None:
        for i in range(self.__barWidth + 1, self.__maxBarWidth + 1):
             if(len(self.__array) < round(self.calculateMaxBars(i, self.__maxPadding))):
                self.__barWidth = i
        
    # Calculate upper and lower bounds of the array
    def calculateArrayBounds(self) -> None:
        # Calculate maximum value the array can have by:
        # Choosing an arbitrary number between randomLow and randomHigh and doubling it 
        self.__upperBound = random.randint(self.__randomLow, self.__randomHigh) * 2 
        
        # Long explanation time...
        # Lower is the absolute minimum value that can appear on screen 
        # Bars are only visible if the top right coorindate is less than or equal to the value of maximumPixels - 0.5 
        # So lower can be calculated be rearranging the y1 coord equation to solve for y
        # 0.5 was rounded up to 1 because it looks nicer
        self.__lowerBound = round((self.screen.getArrayCanvas().winfo_height() - self.__maximumPixels + 1) / (self.__maximumPixels / self.__upperBound))  
    
        # Draw the first element on screen
        self.adjustArray('1')
          
    def getMaxBars(self): return self.__maxBars
    def getArray(self): return self.__array
  