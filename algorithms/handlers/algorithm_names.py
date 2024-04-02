# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import os
import inspect
import importlib 
import sys
from ..algorithm import Algorithm

# This is kinda cool 
# I don't want to manually add a new algorithm everytime I make one (that's kinda cringe)
# Instead I have spent more time than it's worth to automate it
# Also enforces some standards

# Makes sure only files containing the algorithms are selected  
# Provided files containing algorithms follow the naming convention -> (name)_search.py
def filterFileNames(file : str) -> bool:
    return True if file[-9:] == "search.py" else False 

# Checks that relevant files follow inheritance and naming convenvtions 
# Checks if any class name has words "Algorithm" or "Search" in them
def filterClassNames(className : str) -> bool:
    return True if "Search" in className or "Algorithm" in className else False

# Returns the name of each algorithm that has been written
# Provided the naming conventions have been followed
def getAlgorithms() -> tuple:
    # Get the name of each algorithm module
    moduleNames = getModuleNames()
    # Returns a list of the every algorithms name
    return getAlgorithmNames(moduleNames)

# Gets modules names in this package 
def getModuleNames() -> list:
    path = "./algorithms/searching"
    # Gets every file in the given directory
    # and filters out files that don't contain the algorithms
    algorithmFiles = filter(filterFileNames, os.listdir(path)) 
    # removes the .py file extension - leaving only the module names
    return [module.removesuffix(".py") for module in algorithmFiles]

def errorWrapper(errorMessage : str) -> None:
    print(errorMessage, file=sys.stderr)

# Returns a tuple containing every algorithms name 
# So the names can be seen in the drop down menu
def getAlgorithmNames(modules : list) -> tuple:
    algorithmNames = []
    # Imports relevant modules and gets relevant classes
    for module in modules:
        
        # Imports module
        try:
            algorithmModule = importlib.import_module("algorithms.searching." + module)
        # Incase there is an error importing the module
        except Exception as error:
            errorWrapper(f"Could not import algorithms.searching.{module}")
            continue
       
        # This just creates a list of all classes in the imported module 
        # I love one line list comprehensions (Thx Haskell)
        moduleClasses = [name for name, _ in inspect.getmembers(algorithmModule)] 
        # filters out any classes that aren't needed (classes without the words "Algorithm" or "Search")
        algorithmClasses = list((filter(filterClassNames, moduleClasses)))
        
        # Checks algorithm class has at least imported the Algorithm class
        if "Algorithm" in algorithmClasses: algorithmClasses.remove("Algorithm")
        else:
            errorWrapper(f"{module} is not a child of Algorithm class")
            continue

        # If the list is empty then "Search" was not included in the class name
        if not algorithmClasses: 
            errorWrapper(f"{module} does not contain 'Search' in class name")
            continue

        # Checks if "Search" is at the end of the algorithms class name or not
        # If not then the naming convention has not been followed and the algorithm won't be added
        if not algorithmClasses[0][-6:] == "Search": continue 
        
        # Attempts to create an instance of given class
        # An error is thrown if the constructor is incorrect or if there is no implementation for abstract methods
        try:
            algorithmInstance = getattr(algorithmModule, algorithmClasses[0])("Foo Fighters #1") 
        except Exception as error: 
            errorWrapper(f"{algorithmClasses[0]}: {error}")
            continue
        
        # Gets classes the algorithm instance has inherited from
        parentClasses = algorithmInstance.__class__.__bases__ 
        # Checks if class has actually inherited the Algorithms class
        if(not Algorithm in parentClasses):
            errorWrapper(f"{module} is not a child of Algorithm class")
   
        # Checks correct function is in algorithm class -> so it can be called later
        algorithmFunction = algorithmClasses[0][0].lower() + algorithmClasses[0][1:]
        # List of all functions in given algorithm class
        classFunctions = dir(algorithmInstance) 

        # Tests that algorithms have implemented the constructor properly 
        # If the Algorithm classes constructor has not been called then an error is thrown
        try:
            algorithmInstance.getDataModel()
        except Exception as error:
            errorWrapper(f"{module}: {error}")
            continue
        
        # If required function not in algorithm class -> it can't be called later
        # so class is not added to list
        if not algorithmFunction in classFunctions: 
            errorWrapper(f"{module} does not contain valid naming convention for the algorithm implementation function")
            continue 

        algorithmNames.append(algorithmInstance.getName())

    # Convert list to tuple and returns it 
    return tuple(algorithmNames)

# Listen to Last Nite By The Strokes
