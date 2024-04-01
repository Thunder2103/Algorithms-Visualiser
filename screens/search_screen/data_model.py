import random
import threading

# This class contains solely the data and functions algorithms need to run 
# This is kept seperate from the SearchModel class to add more abstraction
class SearchDataModel():
    # Constructor
    def __init__(self):
        self.__controller = None
        self.__array =  []
        self.__barColours = []
        self.__target = None
        self.__delay = None 
        self.__algorithmRunning = threading.Event()
        self.__algorithmPauseLock = threading.Lock()
 
    # Sets controller attribute to value passed
    def addController(self, controller):
        if(self.__controller is None):
            self.__controller = controller
    
    # Returns the array
    def getArray(self) -> list: 
        return self.__array  
    
    # Appends passed value to the array
    def appendArray(self, value : int) -> None: 
        self.__array.append(value)
        self.__barColours.append("black")
    
    # Removes last element from the array
    def popArray(self) -> None: 
        self.__array.pop()
        self.__barColours.pop()
    
    # Sorts the array
    def sortArray(self):
        self.__array.sort()
       
    # Shuffles the array
    def shuffleArray(self):
        random.shuffle(self.__array)

    # Updates the screen so changes to the array are shown
    def updateArrayOnScreen(self):
        self.__controller.scheduleArrayUpdate() 
    
    # Gets the colour of the bar the index passed
    def getBarColour(self, index : int) -> str:
        if(index >= len(self.__array)): return "" 
        else: return self.__barColours[index]
    
    # Sets the bar colour at the specified index to the specified colour
    def setBarColour(self, index : int, colour: str) -> None: 
        if(index >= len(self.__array)): return 
        else: self.__barColours[index] = colour
    
    # Resets all the bars colours to the default (black)
    def resetBarColours(self) -> None: 
        self.__barColours = ["black" for _ in range(len(self.__array))] 
    
    # Gets the delay (time algorithm is paused for)
    def getDelay(self) -> int: 
        return self.__delay
    
    # Sets the delay to the passed integer
    def setDelay(self, value : int) -> None:
        self.__delay = value 
    
    # Returns the target (the element being looked for)
    def getTarget(self) -> int: 
        return self.__target
    
    # Sets the element being looked for to the passed value
    def setTarget(self, value : int) -> None:
        self.__target = value   
    
    def setStopFlag(self):
        self.__algorithmRunning.set()
    
    def clearStopFlag(self):
        self.__algorithmRunning.clear()
    
    def isStopped(self) -> bool:
        return True if self.__algorithmRunning.is_set() else False

    def acquireLock(self):
        self.__algorithmPauseLock.acquire()
    
    def releaseLock(self):
        self.__algorithmPauseLock.release()

# Listen to Everlong By Foo Fighters