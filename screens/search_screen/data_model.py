import random

# This class contains solely the data and functions algorithms need to run 
# This is kept seperate from the SearchModel class to add more abstraction
class SearchDataModel():
    def __init__(self):
        self.__controller = None
        self.__array =  []
        self.__barColours = []
        self.__target = None
        self.__delay = None 
    
    def addController(self, controller):
        if(self.__controller is None):
            self.__controller = controller
    
    def getArray(self) -> list: 
        return self.__array  
    
    def appendArray(self, value : int) -> None: 
        self.__array.append(value)
        self.__barColours.append("black")
    
    def popArray(self) -> None: 
        self.__array.pop()
        self.__barColours.pop()
    
    def sortArray(self):
        self.__array.sort()

    def shuffleArray(self):
        random.shuffle(self.__array)

    def displayArray(self):
        self.__controller.displayArray()  
    
    def getBarColour(self, index : int) -> str:
        if(index >= len(self.__array)): return "" 
        else: return self.__barColours[index]
    
    def setBarColour(self, index : int, colour: str) -> None: 
        if(index >= len(self.__array)): return 
        else: self.__barColours[index] = colour
    
    def resetBarColours(self): 
        self.__barColours = ["black" for _ in range(len(self.__array))] 
    
    def getDelay(self) -> int: 
        return self.__delay
    
    def setDelay(self, value : int) -> None:
        self.__delay = value 
    
    def getTarget(self) -> int: 
        return self.__target
    
    def setTarget(self, value : int) -> None:
        self.__target = value 
    
