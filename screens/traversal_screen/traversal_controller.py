# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

from canvas_node import CanvasNode 
from tkinter import Event

class TaversalController():
    def __init__(self, screen, model): 
        self.__screen = screen 
        self.__model = model 
        self.__mouseRadiusID = None   
    
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
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Enter>", lambda _: self.__changeColourOnHover(circle))
        # Add event to change nodes colour when the mouse hovers over them
        canvas.tag_bind(circle, "<Leave>", lambda _: self.__changeColourOnLeave(circle)) 
        # Add event listener to move node when it's dragged by the mouse 
        canvas.tag_bind(circle, "<B1-Motion>", lambda event: self.__moveNode(event, canvasNode))   

        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update() 
    
    def __canNodeBeSpawned(self): 
        # Coordinates the node will be drawn at 
        x0, y0, x1, y1 = self.__model.getInitialCoords()  
        spaceBetweenNodes = self.__model.getSpaceBetweenNodes() * 2  
        # Get's ID of any items in the radius
        conflictingNodes = list(self.__screen.getCanvas()
                                .find_overlapping(
                                    x0 - spaceBetweenNodes, 
                                    y0 - spaceBetweenNodes, 
                                    x1 + spaceBetweenNodes,
                                    y1 + spaceBetweenNodes)) 
        
        # Remove the invinsible collision detection circle
        if(self.__mouseRadiusID in conflictingNodes): 
            conflictingNodes.remove(self.__mouseRadiusID) 
        # Returnd True if the node can be drawn, else False 
        return False if conflictingNodes else True
        
    # Moves the node to follow the users mouse 
    def __moveNode(self, event : Event, canvasNode : CanvasNode) -> None:  
        # Reference to the canvas 
        canvas = self.__screen.getCanvas()
        # Radius of the nodes
        circleSize = self.__model.getCircleSize()  
        # Offset to keep center of circle underneath mouse  
        circleOffset = circleSize // 2 

        # I don't know why but this stops the circles only being partially 
        # drawn when being moved around (works on windows only)
        canvas.configure(cursor='arrow')

        # Checks if mouse has gone out of bounds to the left 
        # Stops the node from moving off the canvas
        xCoord = max(event.x - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds to the right 
        # Stops the node from moving off the canvas
        xCoord = min(xCoord, canvas.winfo_width() - self.__model.getCanvasUpperBoundOffset() - circleSize) 

        # Checks if mouse has gone out of bounds by going above the canvas
        # Stops the node from moving off the canvas 
        yCoord = max(event.y - circleOffset, self.__model.getCanvasLowerBoundOffset()) 
        # Checks if mouse has gone out of bounds by going below the canvas
        # Stops the node from moving off the canvas 
        yCoord = min(yCoord, canvas.winfo_height() - self.__model.getCanvasUpperBoundOffset() - circleSize)
     
        # Space that should exist between each node
        spaceBetweenNodes = self.__model.getSpaceBetweenNodes() * 2 
        # Moves mouse radius to specified coordinated 
        canvas.moveto(self.__mouseRadiusID, xCoord - spaceBetweenNodes, yCoord - spaceBetweenNodes)

        # The above could be done in one line but just because it can doesn't mean it should 
        # Doing it in one line would make the calculations very hard to read  

        # Gets a list of ID's the of the nodes that have been collided with 
        # If the list is non-empty at least one collision has occured 
        # The node is not moved 
        if(self.__findCollidingNodes(canvasNode.getCanvasID(), self.__mouseRadiusID) ): return

        # Moves center of the circle to the coordinates specified 
        canvas.moveto(canvasNode.getCanvasID(), xCoord, yCoord) 
        # Updates coords in the CanvasNode object
        canvasNode.updateCoords(xCoord, yCoord, xCoord + circleSize, yCoord + circleSize)
        # Updates screen so node can be seen onscreen
        self.__screen.getWindow().update()
  
    # Returns a list containing the ID's of any nodes that are the collision range
    def __findCollidingNodes(self, circle : int, boundary : int) -> list:  
        x0, y0, x1, y1 = self.__screen.getCanvas().coords(boundary)
        collidedNodes = list(self.__screen.getCanvas().find_overlapping(x0, y0, x1, y1))   
        # Removes the circle that is being moved from the overlapping list
        if(circle in collidedNodes): collidedNodes.remove(circle)
        # Removes the boundary from the overlapping list 
        if(boundary in collidedNodes):
            collidedNodes.remove(boundary)
        return collidedNodes

    # Draws a circle that follows the mouse as it moves a node around the canvas
    def __drawBoundaryCircle(self, x : int, y : int) -> int: 
        circleSize = self.__model.getCircleSize()
        circleOffset = circleSize // 2 
        boundarySize = self.__model.getSpaceBetweenNodes() * 2
        # Returns the ID of circle created 
        # This allows the circle to be moved rather than redrawn whenever the mouse is moving a node 
        return self.__screen.getCanvas().create_oval(x - circleOffset - boundarySize, 
                                            y - circleOffset - boundarySize, 
                                            x + circleOffset + boundarySize, 
                                            y + circleOffset + boundarySize, 
                                            outline="white")
            
    # Changes the nodes colour the mouse is hovering to red
    def __changeColourOnHover(self, circle : int) -> None: 
        self.__screen.getCanvas().itemconfig(circle, fill="red") 
    
    # Changes the mouse stops hovering over a node it's colour is set to blue 
    def __changeColourOnLeave(self, circle : int) -> None:
        self.__screen.getCanvas().itemconfig(circle, fill="blue")  
    
    # Creates the invisible circle used to check if nodes collide
    def createBoundaryCircle(self) -> None: 
        x, y, _, _ = self.__model.getInitialCoords() 
        circleOffset = self.__model.getCircleSize() // 2
        self.__mouseRadiusID = self.__drawBoundaryCircle(x + circleOffset , y + circleOffset)

# Listen to Paranoid by Black Sabbath