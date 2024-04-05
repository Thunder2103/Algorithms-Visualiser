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
        self.__delayLock = threading.Lock()
 
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
        self.__delayLock.acquire()  
        delay = self.__delay
        self.__delayLock.release()
        return delay
    
    # Sets the delay to the passed integer
    def setDelay(self, value : int) -> None:
        self.__delayLock.acquire()
        self.__delay = value  
        self.__delayLock.release()
    
    # Returns the target (the element being looked for)
    def getTarget(self) -> int: 
        return self.__target
    
    # Sets the element being looked for to the passed value
    def setTarget(self, value : int) -> None:
        self.__target = value   
    
    # Sets the stop flag, used to tell algorithm threads to stop
    def setStopFlag(self):
        self.__algorithmRunning.set()
    
    # Sets stop flag back to false
    def clearStopFlag(self):
        self.__algorithmRunning.clear()
    
    # Returns True if algorithm thread needs to stop, else false
    def isStopped(self) -> bool:
        return True if self.__algorithmRunning.is_set() else False

    # Threads call this to hold the lock
    def acquireLock(self):
        self.__algorithmPauseLock.acquire() 
    
    # Threads call this to release the lock
    def releaseLock(self):
        self.__algorithmPauseLock.release() 
    
    # Checks if the algorithm thread is paused or not 
    def isPaused(self): 
        return self.__algorithmPauseLock.locked()

# Listen to Everlong By Foo Fighters