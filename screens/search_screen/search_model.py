class SearchModel(): 
    def __init__(self) -> None: 
        # Current width of bars
        self.__barWidth = 15
        # Smallest width bars can be 
        self.__minBarWidth = 2
        # Largest bar can be 
        self.__maxBarWidth = 15
        # Distance between each bar 
        self.__barDist = 2
        # Minimum distance between displayed array and edge of canvas
        self.__minPadding = 5
        # Maximum distance between displayed array and edge of canvas
        self.__maxPadding = 20
        # Maximum number of bars that can be drawn on screen
        self.__maximumPixels = None
        # Lowest value that could appear in the array
        self.__randomLow = 100
        # Highest value that could appear in array
        self.__randomHigh = 5000
        # Lowest value that can actually appear in the array
        self.__lowerBound = None
        # Highest value that can actually appear in the array
        self.__higherBound = None
        # Array containing all the data 
        self.__array = []
    
    def getBarWidth(self) -> int: return self.__barWidth
    def setBarWidth(self, value : int) -> None: self.__barWidth = value
    def getMinBarWidth(self) -> int: return self.__minBarWidth 
    def getMaxBarWidth(self) -> int: return self.__maxBarWidth
    def getBarDistance(self) -> int: return self.__barDist
    def getMinPadding(self) -> int: return self.__minPadding
    def setMinPadding(self, value : int) -> None: self.__minPadding = value
    def getMaxPadding(self) -> int: return self.__maxPadding
    def getMaximumPixels(self) -> int: return self.__maximumPixels
    def setMaximumPixels(self, value : int) -> None: self.__maximumPixels = value
    def getLowestRandomBound(self) -> int: return self.__randomLow
    def getHighestRandomBound(self) -> int: return self.__randomHigh 
    def getLowerBound(self) -> int: return self.__lowerBound
    def setLowerBound(self, value : int) -> None: self.__lowerBound = value
    def getHigherBound(self) -> int: return self.__higherBound
    def setHigherBound(self, value : int) -> None: self.__higherBound = value

    def getArray(self) -> list: return self.__array
    def appendArray(self, value : int) -> None: self.__array.append(value)
    def popArray(self) -> None: self.__array.pop()
