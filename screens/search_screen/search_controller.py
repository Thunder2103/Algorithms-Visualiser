# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import random 

class SearchController():
    def __init__(self, screen, model, dataModel) -> None:
        self.__screen = screen
        self.__model = model
        self.__dataModel = dataModel
        # Returns the height of the canvas - maximum number of pixels an element can possibly have
        self.__model.setMaximumPixels(self.__calculateMaximumPixels())
        # Calculates spacing between canvas border and displayed array 
        # Is also used to calculate the largest possible size of the array
        self.__model.setMinPadding(self.__calculateBestPadding())
        # Calculate largest and smallest values that can be put in the array
        self.__calculateArrayBounds()

    # Largest number that can be displayed on screen
    def __calculateMaximumPixels(self) -> int:
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn   
        return self.__screen.getArrayCanvas().winfo_height() - 2 

    # Finds the best distance between the displayed array and the edges of canvas, 
    # to maximise the number of elements and centre the array as best as possible
    def __calculateBestPadding(self) -> int:
        for i in range(self.__model.getMinPadding(), self.__model.getMaxPadding()):
            # Calculates how many bars can be displayed on the screen 
            bars = self.__calculateMaxBars(self.__model.getMinBarWidth(), i)  
            # If the number of bars is a whole number
            if((bars).is_integer()):  
                # Maximum size the array can be 
                self.__model.setMaxBars(int(bars))
                # Function terminates - returning the best padding (i)
                return i
        # If no whole number can be found, just use the max padding (the array being off centre is less noticeable) 
        maxBars = round(self.__calculateMaxBars(self.__model.getMinBarWidth(), self.__model.getMaxPadding())) 
        self.__model.setMaxBars(maxBars)
        return self.__model.getMaxPadding()

    # Calculates maximum number of bars that can be displayed given the padding
    def __calculateMaxBars(self, barWidth, padding) -> int:
        return ((self.__screen.getArrayCanvas().winfo_width()) - (padding * 2)) / (barWidth + self.__model.getBarDistance())

    # Calculates the padding to centre the array of a given size
    def __calculatePadding(self) -> int:
        return ((self.__screen.getArrayCanvas().winfo_width() - (len(self.__dataModel.getArray()) * (self.__model.getBarDistance() 
                                                                                      + self.__model.getBarWidth()))) // 2) + self.__model.getBarDistance()
    
    # Adjusts size of bars so amount of elements can fit on screen and stay in the canvas' centre
    def adjustArray(self, value : str) -> None:
        # If the value given from the scrollbar is less than the arrays size
        # Delete elements from the array and check if bar size can increase
        if(int(value) < len(self.__dataModel.getArray())): 
            self.__deleteElements(int(value))
            self.__increaseBarSize()
        # Otherwise add elements to the array and check is bar size needs to decrease
        else: 
            self.__addElements(int(value))
            self.__decreaseBarSize()
        # If the array size is less than the maximum number of bars. 
        # Calculate padding 
        if(len(self.__dataModel.getArray()) != self.__model.getMaxBars()): self.__padding = self.__calculatePadding()
        # If the array size is now at maximum size, 
        # padding is the value calulated by the calculateBestPadding() method
        else: self.__padding = self.__model.getMinPadding()
        
        # The amount each elements is stretched along the y-axis 
        # Means the elements are scaled with the largest element
        self.yStretch = self.__model.getMaximumPixels() / max(self.__dataModel.getArray())
        # Draw the actual array with all the adjustments made
        # Since there is no algorithm active, all bars are drawn as black
        self.displayArray()
        
    # Iterates through array, drawing each bar
    # The function has two default arguements -> currentIndex and altColour both initialised to None
    def displayArray(self) -> None:
            # Clear displayed array on screen
            self.__clearDisplayedArray()
            for x, y in enumerate(self.__dataModel.getArray()):
                # Calculate where each bar is placed on screen
                # Bottom left co-ord
                x1 = x * self.__model.getBarDistance() + x * self.__model.getBarWidth() + self.__padding
                # Top left coord
                y1 = self.__screen.getArrayCanvas().winfo_height() - (y * self.yStretch)  
                # Bottom right coord
                x2 = x * self.__model.getBarDistance() + x * self.__model.getBarWidth()+ self.__model.getBarWidth() + self.__padding
                # Top right coord
                y2 = self.__screen.getArrayCanvas().winfo_height() 
                # Chooses correct colour for bar to be filled in with
                self.__screen.getArrayCanvas().create_rectangle(x1, y1, x2, y2, fill = self.__dataModel.getBarColour(x)) 
            # Updates screen so bars can be seen onscreen
            self.__screen.getWindow().update() 
            self.__dataModel.resetBarColours()
      
    # Wipes everything off the canvas
    def __clearDisplayedArray(self) -> None:
        self.__screen.getArrayCanvas().delete("all")

    # Adds amount of elements corresponding to the value
    def __addElements(self, value):
        for _ in range(len(self.__dataModel.getArray()), value):
            # Choose random number inbetween upper and lower bounds
            self.__dataModel.appendArray(random.randint(self.__model.getLowerBound(), self.__model.getHigherBound()))
         
    # Deletes number of elements corresponding to the value
    def __deleteElements(self, value) -> None:
        for _ in range(len(self.__dataModel.getArray()), value, -1):
            self.__dataModel.popArray()

    # Determines if bars need to shrink in size as array grows
    def __decreaseBarSize(self) -> None:
        for i in range(self.__model.getBarWidth(), self.__model.getMinBarWidth(), -1):
            if(len(self.__dataModel.getArray()) < round(self.__calculateMaxBars(i, self.__model.getMaxPadding()))):
                self.__model.setBarWidth(i)
                return 
        self.__model.setBarWidth(self.__model.getMinBarWidth())
    
    # Determines if bars needs to increase in size as array shrinks
    def __increaseBarSize(self) -> None:
        for i in range(self.__model.getBarWidth() + 1, self.__model.getMaxBarWidth() + 1):
             if(len(self.__dataModel.getArray()) < round(self.__calculateMaxBars(i, self.__model.getMaxPadding()))): 
                self.__model.setBarWidth(i)
  
    # Calculate upper and lower bounds of the array
    def __calculateArrayBounds(self) -> None:
        # Calculate maximum value the array can have by:
        # Choosing an arbitrary number between randomLow and randomHigh and doubling it 
        higherBound = random.randint(self.__model.getLowestRandomBound(), self.__model.getHighestRandomBound()) * 2  
        self.__model.setHigherBound(higherBound)
        
        # Long explanation time...
        # Lower is the absolute minimum value that can appear on screen 
        # Bars are only visible if the top right coorindate is less than or equal to the value of maximumPixels - 0.5 
        # So lower can be calculated be rearranging the y1 coord equation to solve for y
        # 0.5 was rounded up to 1 because it looks nicer
        lowerBound = round((self.__screen.getArrayCanvas().winfo_height() - self.__model.getMaximumPixels() + 1) 
                                  / (self.__model.getMaximumPixels() / self.__model.getHigherBound()))  
        self.__model.setLowerBound(lowerBound)
        # Draw the first element on screen
        self.adjustArray('1')
    
    def setDataModel(self, dataModel):
        self.__dataModel = dataModel

# Listen to Give Me Novacaine by Greeb Day