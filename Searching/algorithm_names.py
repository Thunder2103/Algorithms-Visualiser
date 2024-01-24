# If this isn't at the top the program breaks :/
# If the file is run as is message this returned and program exits
if(__name__ == "__main__"):
    print("This is file shouldn't be run on it's own. \nIt should be imported only.")
    exit()

import os
import inspect
import importlib

# This is kinda cool 
# I don't want to manually add a new algorithm everytime I make one (that's kinda cringe)
# Instead I have spent more time than it's worth to automate it

# Makes sure only files containing the algorithms are selected  
# Provided files containing algorithms follow the naming convention -> (name)_search.py
def filterFileNames(file) -> bool:
    return True if file[-9:] == "search.py" else False 

# Checks that relevant files follow inheritance and naming convenvtions 
# Checks if any class name has words "Algorithm" or "Search" in them
def filterClassNames(className) -> bool:
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
    path = "./Searching/Algorithms"
    # Gets every file in the given directory
    # and filters out files that don't contain the algorithms
    algorithmFiles = filter(filterFileNames, os.listdir(path)) 
    # removes the .py file extension - leaving only the module names
    return [module.removesuffix(".py") for module in algorithmFiles]

# Returns a tuple containing every algorithms name 
# So the names can be seen in the drop down menu
def getAlgorithmNames(modules) -> tuple:
    algorithmNames = []
    # Imports relevant modules and gets relevant classes
    for module in modules:
        # Imports module
        algorithmModule = importlib.import_module("Searching.Algorithms." + module)
       
        # This just creates a list of all classes in the imported module 
        # I love one line list comprehensions (Thx Haskell)
        moduleClasses = [name for name, obj in inspect.getmembers(algorithmModule)] 
        # filters out any classes that aren't needed (classes without the words "Algorithm" or "Search")
        algorithmClasses = list((filter(filterClassNames, moduleClasses)))
        
        # Check algorithm class includes the manditory Algorithm class
        if "Algorithm" in algorithmClasses: algorithmClasses.remove("Algorithm")
        else: continue

        # If the list is empty then "Search" was not included in the class name
        if not algorithmClasses: continue

        # Checks if "Search" is at the end of the algorithms class name or not
        # If not then the naming convention has not been followed and the algorithm won't be added
        if not algorithmClasses[0][-6:] == "Search": continue 
        
        # Attempts to create an instance of given class
        # If class doesn't have an implementation for all abstract methods then an error is thrown
        try:
            algorithmInstance = getattr(algorithmModule, algorithmClasses[0])() 
        except Exception as error: 
            print(f"{algorithmClasses[0]}:", error)
            continue

        # Checks correct function is in algorithm class -> so it can be called later
        algorithmFunction = algorithmClasses[0][0].lower() + algorithmClasses[0][1:]
        # List of all functions in given algorithm class
        classFunctions = dir(algorithmInstance) 

        # If required function not in algorithm class -> it can't be called later, 
        # so class is not added to list
        if not algorithmFunction in classFunctions: continue 

        algorithmNames.append(algorithmInstance.getName())

    # Convert list to tuple and returns it 
    return tuple(algorithmNames)