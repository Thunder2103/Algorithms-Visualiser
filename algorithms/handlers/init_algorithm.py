# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import importlib
from typing import Callable

# Creates instance of algorithm  
def callAlgorithm(dataModel, algorithm : str, algorithmType : str, widgetsAlgorithmStops : Callable[[], None]) -> None:
    # Constructs name of module where algorithm class is stored
    fileName = "_".join(algorithm.split(" ")).lower()
    # Imports module
    algorithmModule = importlib.import_module(f"algorithms.{algorithmType.lower()}ing." + fileName)
    # Constructs name of class so it can be instantiated
    algorithmClass = algorithm.replace(" ", "")
    # Create instance of the relevant class 
    algorithmInstance = getattr(algorithmModule, algorithmClass)(dataModel) 
    # Constructs name of function that needs to be called to run algorithm 
    algorithmFunction = algorithmClass[0].lower() + algorithmClass[1:]
    # Calls algorithm function 
    getattr(algorithmInstance, algorithmFunction)()  
    # I generally dislike passing functions as parameters 
    # This disables and enables the appropriate widgets
    widgetsAlgorithmStops() 

# Listen to What's my age again by Blink-182
