# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from canvas_node import CanvasNode 
from .traversal_model import TraversalModel
from tkinter import Event 
import math
import random

class TraversalController():
    def __init__(self, screen, model : TraversalModel): 
        self.__screen = screen 
        self.__model = model  
        self.__isEdgeBeingDrawn = False 
        self.__currentEdge = None 
        self.__destinationNode = None 

    def addCanvasEvents(self): 
        canvas = self.__screen.getCanvas() 
        # Add event to delete current edge being drawn when the canvas is clicked
        canvas.bind("<Button-1>", lambda _: self.__deleteEdge())

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
        self.__model.addNode(canvasNode)
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Enter>", lambda _: self.__changeColourOnHover(canvasNode))
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Leave>", lambda _: self.__changeColourOnLeave(canvasNode)) 
        # Add event listener to move node when it's dragged by the mouse 
        canvas.tag_bind(circle, "<B1-Motion>", lambda event: self.__moveNode(event, canvasNode))   
        # Add event listener to add an edge when a node is clicked 
        canvas.tag_bind(circle, "<Button-1>", lambda _: self.__createEdge(canvasNode))

        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update() 
    
    # Creates a line that follows the mouse until another node is clicked 
    def __createEdge(self, canvasNode : CanvasNode):     
        # If edge is being drawn on screen
        if(self.__isEdgeBeingDrawn): 
            # Tuple containing canvas ID of the edge 
            # and the two nodes the edge connectes
            edgeTuple = (self.__currentEdge, self.__destinationNode, canvasNode)
            revEdgeTuple = (self.__currentEdge, canvasNode, self.__destinationNode)
            # If the edge starts and ends at the same node
            # Or if the edge already exists between the two nodes
            if(self.__destinationNode == canvasNode or self.__model.getEdge(edgeTuple) != -1 
               or self.__model.getEdge(revEdgeTuple) != -1):
                # Delete edge 
                self.__deleteEdge()  
            # If the node start and ends at the two different nodes
            else:
                # Add edge to the dictionary, with a random weight
                self.__model.addEdge(edgeTuple, random.randint(10, 100))
                # Moves line to the centre of the destination node
                self.__centreEdge(canvasNode)
                self.__stopMovingEdge()
        # If an edge is not being draw on screen
        else: 
            # Adds canvas event to draw lines
            self.__addCanvasEvent(canvasNode)
            # Sets variable to True
            self.__isEdgeBeingDrawn = True   
            # Sets desination node to current node passed to function
            self.__destinationNode = canvasNode
        # Updates window to display changes
        self.__screen.getWindow().update() 
    
    def __stopMovingEdge(self):
        # Remove event that draws line
        self.__deleteCanvasEvent()
        # Set edge being drawn to False
        self.__isEdgeBeingDrawn = False
        # Set current edge to None
        self.__currentEdge = None 
        # Sets desintation node to None 
        self.__destinationNode = None 

    # Deletes current edge from the screen 
    def __deleteEdge(self): 
        if(self.__currentEdge != None): 
            self.__screen.getCanvas().delete(self.__currentEdge) 
            self.__stopMovingEdge()
        
    # Add event to draw a line representing an edge
    def __addCanvasEvent(self, canvasNode : CanvasNode): 
        self.__screen.getCanvas().bind("<Motion>", lambda event: self.__drawEdge(event, canvasNode))

    # Removes the event that draws lines representing edges 
    def __deleteCanvasEvent(self):  
        canvas = self.__screen.getCanvas()
        if("<Motion>" in canvas.bind()):
            canvas.unbind("<Motion>")

    # Draws an edge from the given circle to the mouses current position
    def __drawEdge(self, event : Event, canvasNode : CanvasNode) -> None:  
        canvas = self.__screen.getCanvas()   
        circleOffset = self.__model.getCircleSize() // 2
        x0, y0, _, _ = canvasNode.getCoords() 
        lineCoords = None

        # Checks if mouse has left the node the edge starts from
        collisions = canvas.find_overlapping(event.x, event.y, event.x, event.y)  
        # If the mouse is still in the node, the edge is not drawn yet
        if(canvasNode.getCanvasID() in collisions): return  
        # If there is no current edge 
        if(self.__currentEdge == None): 
            # Create a new edge and assign it to a variable 
            self.__currentEdge = canvas.create_line(x0 + circleOffset, y0 + circleOffset, 
                                                    event.x, event.y, width = "3")  
            # Lowers the priority of the edge, so it appears below nodes 
            canvas.tag_lower(self.__currentEdge) 
        # If there is an edge being drawn on screen
        else:   
            # Gets current coordinates of the line
            lineCoords = canvas.coords(self.__currentEdge)
            # Change XY coordinates to where the mouse is
            lineCoords[2] = event.x 
            lineCoords[3] = event.y 
            # Updates the lines coordinates 
            canvas.coords(self.__currentEdge, lineCoords)
        
    # Draws an edge to the centre of the circle
    def __centreEdge(self, canvasNode : CanvasNode) -> None: 
        x1, y1, _, _ = canvasNode.getCoords() 
        circleOffset = self.__model.getCircleSize() // 2 
        canvas = self.__screen.getCanvas() 
        # Gets current coords of the edges
        coords = canvas.coords(self.__currentEdge) 
        # Upate coords of the edge to be in the middle of the passed node
        coords[2] = x1 + circleOffset 
        coords[3] = y1 + circleOffset 
        # Send updated coords to the canvas
        canvas.coords(self.__currentEdge, coords)

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
            len(self.__model.getNodes()) == self.__model.getMaxNumNodes() else True
        
    # Moves the node to follow the users mouse 
    def __moveNode(self, event : Event, canvasNode : CanvasNode) -> None:  
        # Disables canvas event that draws edges if it binded 
        self.__deleteCanvasEvent()
        # Sets False so another edge cna be drawn later
        self.__isEdgeBeingDrawn = False

        # Reference to the canvas 
        canvas = self.__screen.getCanvas()
        # Radius of the nodes
        circleSize = self.__model.getCircleSize()  
        # I don't know why but this stops the circles only being partially 
        # drawn when being moved around (works on windows only)
        canvas.configure(cursor='arrow')
        # Sets the circles colour to Red, makes sure the colour remains 
        # red even if the mouse is moved off the circle 
        self.__screen.changeCircleColour(canvasNode.getCanvasID(), "Red")

        # Handles if the mouse moves of off the canvas 
        xCoord, yCoord = self.__adjustCoords(event.x, event.y)

        # Updates coords in the CanvasNode object
        canvasNode.updateCoords(xCoord, yCoord, xCoord + circleSize, yCoord + circleSize)
        # Applies forces to each node 
        self.__calculateForces(canvasNode)

        # Updates coords in the CanvasNode object
        canvasNode.updateCoords(xCoord, yCoord, xCoord + circleSize, yCoord + circleSize)
        self.__redrawNodes()
        self.__redrawEdges()
        # Moves center of the circle to the coordinates specified 
        #canvas.moveto(canvasNode.getCanvasID(), xCoord, yCoord) 
        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update()

    # Changes the coordinates of a circle when when the user drags it across the screen
    def __adjustCoords(self, x : int, y : int) -> tuple:  
        
        canvas = self.__screen.getCanvas()
        circleSize = self.__model.getCircleSize()
        circleOffset = circleSize // 2 
        self.__stopMovingEdge()
        
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
        for node in self.__model.getNodes():  
            x0, y0, _, _ = node.getCoords()
            canvas.moveto(node.getCanvasID(), x0, y0)
    
    def __redrawEdges(self):
        canvas = self.__screen.getCanvas() 
        circleOffset = self.__model.getCircleSize() // 2  
        # Iterate through each edge
        for edgeID, destNode, sourceNode in self.__model.getEdges().keys():  
            # Get coordinates of the nodes the edges should be between
            x0, y0, _, _ = destNode.getCoords() 
            x1, y1, _, _ = sourceNode.getCoords()   
            # Get current coords of edge
            coords = canvas.coords(edgeID)
            # Update coords of edge 
            coords[0] = x0 + circleOffset
            coords[1] = y0 + circleOffset 
            coords[2] = x1 + circleOffset 
            coords[3] = y1 + circleOffset 
            # Send updated coords to the canvas
            canvas.coords(edgeID, coords)
            
    # Changes the nodes colour the mouse is hovering to red
    def __changeColourOnHover(self, canvasNode : CanvasNode) -> None: 
        self.__screen.changeCircleColour(canvasNode.getCanvasID(), 
                                         canvasNode.getHighlightColour())
    
    # Changes the mouse stops hovering over a node it's colour is set to blue 
    def __changeColourOnLeave(self, canvasNode : CanvasNode) -> None:
        self.__screen.changeCircleColour(canvasNode.getCanvasID(), 
                                         canvasNode.getMainColour())

    # Calculates the forces that will be applied to each node 
    def __calculateForces(self, canvasNode : CanvasNode): 
        n = len(self.__model.getNodes())
        circleSize = self.__model.getCircleSize()
        circleOffset = circleSize// 2 
        # Step one apply Coulombs laws to each node  
        for i in range(n): 
            for j in range(i + 1, n):   
                # XY coordinates of the nodes
                x0, y0, _, _ = self.__model.getNode(i).getCoords()
                x1, y1, _, _, = self.__model.getNode(j).getCoords()   
                # XY coords of the centre of each circle
                centreX0, centreY0 = x0 + circleOffset, y0 + circleOffset
                centreX1, centreY1 = x1 + circleOffset, y1 + circleOffset
 
                # Calculated pythagorean distance between the circles
                dist = self.__calculateDistance(centreX0, centreY0, centreX1, centreY1)  
                # If the circles are far apart the result force would be neglible 
                if(dist > self.__model.getMaximumForceDistance()): 
                    continue
                
                # Resultant force as a scalar 
                force = self.__model.getForceConstant() / max(dist, 1) 

                # Convert scalar force to vector form
                forceX = ((centreX1 - centreX0) / dist) * force
                forceY = ((centreY1 - centreY0) / dist) * force 

                # Update coords of each node 
                self.__updatedCoords(x0, y0, -forceX, -forceY, self.__model.getNode(i))
                self.__updatedCoords(x1, y1, forceX, forceY, self.__model.getNode(j))
           
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
    
    # Calculates distance between two nodes using the pythagoras theorem 
    def __calculateDistance(self, x0 : int, y0 : int, x1 : int, y1 : int) -> float: 
        return math.sqrt(math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2))

    
# Listen to Paranoid by Black Sabbath