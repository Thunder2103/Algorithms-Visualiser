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
        self.__initialX = 5
        self.__intialY = 5
        self.__circleSize = 25
        self.__initialNodeCoords = (self.__initialX, self.__intialY, 
                                    self.__initialX + self.__circleSize, 
                                    self.__intialY + self.__circleSize)
        self.__canvasUpperBoundOffset = 4
        self.__canvasLowerBoundOffset = 2
        self.__nodesSpacingOffset = 20 
        self.__maxNumNodes = 100  
        self.__forceConstant = (1e-8) * 9e9 
        self.__maximumForceDistance = 75 
        
    def addController(self, controller): 
        self.__controller = controller 
    
    # Getters and setters 
    def getMinDelay(self): return self.__minDelay
    def getMaxDelay(self): return self.__maxDelay  
    def getResolution(self): return self.__resolution   
    def getInitialCoords(self): return self.__initialNodeCoords
    def getCircleSize(self): return self.__circleSize
    def getCanvasUpperBoundOffset(self) -> int: return self.__canvasUpperBoundOffset
    def getCanvasLowerBoundOffset(self) -> int: return self.__canvasLowerBoundOffset 
    def getSpaceBetweenNodes(self) -> int: return self.__nodesSpacingOffset 
    def getMaxNumNodes(self) -> int: return self.__maxNumNodes
    def getForceConstant(self) -> float: return self.__forceConstant  
    def getMaximumForceDistance(self) -> int: return self.__maximumForceDistance 
 

# Listen to Jigsaws Falling Into Place by Radiohead