class CanvasNode():
    nodeID = 0

    def __init__(self, canvasID : int, x0 : int, y0 : int, x1 : int, y1 : int) -> None: 
        self.__canvasID = canvasID 
        self.__ID = CanvasNode.nodeID
        CanvasNode.nodeID += 1
        self.__x0 = x0
        self.__y0 = y0  
        self.__x1 = x1
        self.__y1 = y1
        
    def updateCoords(self, x0 : int, y0 : int, x1 : int, y1: int) -> None: 
        self.__x0 = x0
        self.__y0 = y0  
        self.__x1 = x1
        self.__y1 = y1

    def getCanvasID(self) -> int: return self.__canvasID 
    def getXCoord(self) -> int: return self.__x0 
    def getYCoord(self) -> int: return self.__y0
    def getCoords(self) -> tuple: return (self.__x0, self.__y0, self.__x1, self.__y1)
    def getID(self) -> int: return self.__ID   
    
    