# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit() 

class CanvasEdge(): 
    def __init__(self, canvasID, coords, weight) -> None: 
        self.__canvasID = canvasID
        self.__coords = coords
        self.__weight = weight
    
    # Getter for canvas ID 
    def getCanvasID(self): 
        return self.__canvasID
    
    # Getter for weight/cost of edge
    def getWeight(self): 
        return self.__weight 
    def setWeight(self, weight : int): 
        self.__weight = weight
    
    # Coordinates Getter and setters
    def getCoords(self): 
        return self.__coords
    def updateCoords(self, coords):
        self.__coords = coords
