# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

class TraversalModel():
    def __init__(self): 
        self.__controller = None  
        self.__minDelay = 1 
        self.__maxDelay = 1000
        self.__resolution = 1
        self.__initialNodeCoords = (5, 30)
        self.__circleRadius = abs(self.__initialNodeCoords[1] - self.__initialNodeCoords[0])   
        self.__canvasUpperBoundOffset = 4
        self.__canvasLowerBoundOffset = 2
        self.__nodesSpacingOffset = 20
        
    def addController(self, controller): 
        self.__controller = controller 
    
    def getMinDelay(self): return self.__minDelay
    def getMaxDelay(self): return self.__maxDelay  
    def getResolution(self): return self.__resolution   
    def getInitialCoords(self): return self.__initialNodeCoords
    def getRadius(self): return self.__circleRadius
    def getCanvasUpperBoundOffset(self) -> int: return self.__canvasUpperBoundOffset
    def getCanvasLowerBoundOffset(self) -> int: return self.__canvasLowerBoundOffset 
    def getSpaceBetweenNodes(self) -> int: return self.__nodesSpacingOffset

# Listen to Jigsaws Falling Into Place by Radiohead