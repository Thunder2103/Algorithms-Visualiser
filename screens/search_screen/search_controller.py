# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

class SearchController():
    def __init__(self, screen) -> None:
        self.screen = screen

    # Largest number that can be displayed on screen
    def calculateMaximumPixels(self) -> int:
        # Two is taken from the canvas' height because the canvas widget has a border where no pixels are drawn   
        return self.screen.getArrayCanvas().winfo_height() - 2