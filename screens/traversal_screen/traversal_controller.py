# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from canvas_node import CanvasNode 
from .traversal_model import TraversalModel
from tkinter import Event 
import math

class TaversalController():
    def __init__(self, screen, model : TraversalModel): 
        self.__screen = screen 
        self.__model = model  
        self.__nodes = []
        self.__hi = 1
    
    # Draws a circle (node) on the canvas 
    def spawnNode(self):   
        # Gets a reference to the canvas 
        canvas = self.__screen.getCanvas()   

        # If no more nodes can currently be spawned
        if(not self.__canNodeBeSpawned()):   
            # Change the add node buttons text to red 
            self.__screen.changeNodeButtonColour("red")
            return  
        # if node can be drawn, change the buttons colour back to black
        else: self.__screen.changeNodeButtonColour("black")

        # X-Y coords of where the node will spawn -> this is the same for evey node 
        x0, y0, x1, y1 = self.__model.getInitialCoords()   
        # Draws the circle 
        circle = canvas.create_oval(x0, y0, x1, y1, outline = "black", fill="blue")     
        # Create corresponding object for the circle 
        canvasNode = CanvasNode(circle, x0, y0, x1, y1)  
        # Adds node to array containing nodes 
        self.__nodes.append(canvasNode)
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Enter>", lambda _: self.__changeColourOnHover(circle))
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Leave>", lambda _: self.__changeColourOnLeave(circle)) 
        # Add event listener to move node when it's dragged by the mouse 
        canvas.tag_bind(circle, "<B1-Motion>", lambda event: self.__moveNode(event, canvasNode))   

        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update() 
    
    # Checks if a new node can be added to the screen.  
    # Nodes can be added to the screen if there are no 
    # other nodes in a given radius or if the maximum number
    # of nodes has not been exceeded 
    def __canNodeBeSpawned(self): 
        # Coordinates the node will be drawn at 
        x0, y0, x1, y1 = self.__model.getInitialCoords()  
        spaceBetweenNodes = self.__model.getSpaceBetweenNodes() * 2  
        # Get's ID of any nodes within a set radius 
        conflictingNodes = list(self.__screen.getCanvas()
                                .find_overlapping(
                                    x0 - spaceBetweenNodes, 
                                    y0 - spaceBetweenNodes, 
                                    x1 + spaceBetweenNodes,
                                    y1 + spaceBetweenNodes)) 
        # Returnd True if the node can be drawn, else False 
        return False if conflictingNodes or \
            len(self.__nodes) == self.__model.getMaxNumNodes() else True
        
    # Moves the node to follow the users mouse 
    def __moveNode(self, event : Event, canvasNode : CanvasNode) -> None:  
        # Reference to the canvas 
        canvas = self.__screen.getCanvas()
        # Radius of the nodes
        circleSize = self.__model.getCircleSize()  
   
        # I don't know why but this stops the circles only being partially 
        # drawn when being moved around (works on windows only)
        canvas.configure(cursor='arrow')

        # Handles if the mouse moves of off the canvas 
        xCoord, yCoord = self.__adjustCoords(event.x, event.y)

        # Updates coords in the CanvasNode object
        canvasNode.updateCoords(xCoord, yCoord, xCoord + circleSize, yCoord + circleSize)
        # Applies forces to each node 
        self.__calculateForces(canvasNode)

        # Updates coords in the CanvasNode object
        canvasNode.updateCoords(xCoord, yCoord, xCoord + circleSize, yCoord + circleSize)
        
        self.__redrawNodes()
        # Moves center of the circle to the coordinates specified 
        #canvas.moveto(canvasNode.getCanvasID(), xCoord, yCoord) 
        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update()
    
    def __adjustCoords(self, x : int, y : int) -> tuple: 
        canvas = self.__screen.getCanvas()
        circleSize = self.__model.getCircleSize()
        circleOffset = circleSize // 2 
        
        # Checks if mouse has gone out of bounds to the left 
        # Stops the node from moving off the canvas
        xCoord = max(x - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds to the right 
        # Stops the node from moving off the canvas
        xCoord = min(xCoord, canvas.winfo_width() - self.__model.getCanvasUpperBoundOffset() - circleSize) 

        # Checks if mouse has gone out of bounds by going above the canvas
        # Stops the node from moving off the canvas 
        yCoord = max(y - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds by going below the canvas
        # Stops the node from moving off the canvas 
        yCoord = min(yCoord, canvas.winfo_height() - self.__model.getCanvasUpperBoundOffset() - circleSize)  

        # The above could be done in one line but just because it can doesn't mean it should 
        # Doing it in one line would make the calculations very hard to read  

        return(xCoord, yCoord)

    def __redrawNodes(self): 
        canvas = self.__screen.getCanvas()
        for node in self.__nodes:  
            x0, y0, _, _ = node.getCoords()
            canvas.moveto(node.getCanvasID(), x0, y0)

    # Changes the nodes colour the mouse is hovering to red
    def __changeColourOnHover(self, circle : int) -> None: 
        self.__screen.changeCircleColour(circle, "red")
    
    # Changes the mouse stops hovering over a node it's colour is set to blue 
    def __changeColourOnLeave(self, circle : int) -> None:
        self.__screen.changeCircleColour(circle, "Blue")

    # Calculates the forces that will be applied to each node 
    def __calculateForces(self, canvasNode : CanvasNode): 
        n = len(self.__nodes)
        circleSize = self.__model.getCircleSize()
        circleOffset = circleSize// 2 
        
        # Step one apply coulumbs laws to each node  
        for i in range(n): 
            for j in range(i + 1, n):   
                # XY coordinates of the nodes
                x0, y0, _, _ = self.__nodes[i].getCoords()
                x1, y1, _, _, = self.__nodes[j].getCoords()   
                # XY coords of the centre of each circle
                centreX0, centreY0 = x0 + circleOffset, y0 + circleOffset
                centreX1, centreY1 = x1 + circleOffset, y1 + circleOffset
 
                # Calculated pythagorean distance between the circles
                dist = self.__calculateDistance(centreX0, centreY0, centreX1, centreY1)  
                # If the circles are far apart the result force would be neglible 
                if(dist > self.__model.getMaximumForceDistance()): 
                    continue
                
                # Resultant force as a scalar 
                force = self.__model.getForceConstant() / dist 

                # COnvert scalar force to vector form
                forceX = ((centreX1 - centreX0) / dist) * force
                forceY = ((centreY1 - centreY0) / dist) * force 

                # Update coords of each node 
                self.__updatedCoords(x0, y0, -forceX, -forceY, self.__nodes[i])
                self.__updatedCoords(x1, y1, forceX, forceY, self.__nodes[j])
           
    # Updates the X-Y coordinates using the resultant forces
    def __updatedCoords(self, x : int, y : int, forceX : int, forceY : int, canavsNode : CanvasNode):  
        circleSize = self.__model.getCircleSize()
        canvas = self.__screen.getCanvas()
        x0 = x + forceX 
        y0 = y + forceY

        # If the resulting force along the x-axis causes the node 
        # to go out of bounds to the left or the right of the canvas 
        # The x-axis resultant force is reversed 
        if(x0 <= self.__model.getCanvasLowerBoundOffset() 
           or x0 >= canvas.winfo_width() - self.__model.getCanvasUpperBoundOffset() - circleSize): 
            x0 = x - forceX
        
        # If the resulting force along the y-axis causes the node 
        # to go out of bounds above or below the canvas 
        # The y-axis resultant force is reversed 
        if(y0 <= self.__model.getCanvasLowerBoundOffset() or y0 >= 
           canvas.winfo_height() - self.__model.getCanvasUpperBoundOffset() - circleSize): 
            y0 = y - forceY

        # Rounds the new coordinates up to the nearest whole number
        x0 = math.ceil(x0)
        y0 = math.ceil(y0)

        # Updates the coordinates of the relevant node 
        canavsNode.updateCoords(x0, y0, x0 + circleSize, y0 + circleSize) 
    
    def __calculateDistance(self, x0 : int, y0 : int, x1 : int, y1 : int) -> float: 
        return math.sqrt(math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2))

    
# Listen to Paranoid by Black Sabbath