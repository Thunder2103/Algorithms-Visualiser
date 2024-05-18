# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

class TaversalController():
    def __init__(self, screen, model): 
        self.__screen = screen 
        self.__model = model   

# Listen to Paranoid by Black Sabbath