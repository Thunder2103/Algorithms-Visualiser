class CanvasNode():

    # Static variable share dbetween each instance 
    nodeID = 0

    def __init__(self, canvasID : int, x0 : int, y0 : int, x1 : int, y1 : int) -> None: 
        # ID of the node on the canvas
        self.__canvasID = canvasID 
        # Node ID
        self.__ID = CanvasNode.nodeID
        CanvasNode.nodeID += 1 
        # X-Y Coorindates of the node on screen
        self.__x0 = x0
        self.__y0 = y0  
        self.__x1 = x1
        self.__y1 = y1
        # Edges between this and other nodes 
        # and the weight of each edge
        self.__connectedNodes = {} 
        # Main colour of the node
        self.__colour = "Blue"
        # Colour of the node when it is hovered over 
        self.__highlightColour = "Red"
    
    # Updates the coordinates of the node to be accurate to the coordinates on screen
    def updateCoords(self, x0 : int, y0 : int, x1 : int, y1: int) -> None: 
        self.__x0 = x0
        self.__y0 = y0  
        self.__x1 = x1
        self.__y1 = y1

    # Getters 
    def getCanvasID(self) -> int: return self.__canvasID 
    def getXCoord(self) -> int: return self.__x0 
    def getYCoord(self) -> int: return self.__y0
    def getCoords(self) -> tuple: return (self.__x0, self.__y0, self.__x1, self.__y1)
    def getID(self) -> int: return self.__ID    
    def getMainColour(self) -> str: return self.__colour 
    def getHighlightColour(self) -> str: return self.__highlightColour 

    # Adds a connection between this node and another node
    def addConnection(self, nodeID : int, weight : int) -> None: 
        self.__connectedNodes[nodeID] = weight 
    
    # Gets a connection and it's weight given a node
    # Returns -1 if the connection doesn't exist
    def getConnection(self, nodeID: int) -> int:
        if(nodeID not in self.__connectedNodes): return -1 
        return self.__connectedNodes[nodeID]
    
    