# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import importlib

# Creates instance of algorithm  
def callAlgorithm(Searching, algorithm : str) -> None:
    # Constructs name of module where algorithm class is stored
    fileName = "_".join(algorithm.split(" ")).lower()
    # Imports module
    algorithmModule = importlib.import_module("algorithms.searching." + fileName)
    # Constructs name of class so it can be instantiated
    algorithmClass = algorithm.replace(" ", "")
    # Create instance of the relevant class 
    algorithmInstance = getattr(algorithmModule, algorithmClass)() 
    # Constructs name of function that needs to be called to run algorithm 
    algorithmFunction = algorithmClass[0].lower() + algorithmClass[1:]
    # Calls algorithm function 
    getattr(algorithmInstance, algorithmFunction)(Searching) 

# Listen to What's my age again by Blink-182