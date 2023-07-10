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
# Provided files containing algorithms follow the naming convention
def filterFileNames(file):
    return True if "search" in file else False 

# Makes sure only algorithm classes are selected 
# Privded that the naming convention is followed
def filterClassNames(className):
    return True if "Search" in className else False

# Returns the name of each algorithm that has been written
# Provided the naming conventions have been followed
def getAlgorithms():
    # Get the name of each algorithm module
    moduleNames = getModuleNames()
    # Returns a list of the every algorithms name
    return getAlgorithmNames(moduleNames)

# Gets modules names in this package 
def getModuleNames():
    path = "./searching_algorithms"
    # Gets every file in the given directory
    # and filters out files that don't contain the algorithms
    algorithmFiles = filter(filterFileNames, os.listdir(path)) 
    # removes the .py file extension - leaving only the module names
    return [module.removesuffix(".py") for module in algorithmFiles]

# Returns a tuple containing every algorithms name 
# So the names can be seen in the drop down menu
def getAlgorithmNames(modules):
    algorithmNames = []
    # Imports relevant modules and gets relevant classes
    for module in modules:
        algorithmModule = importlib.import_module("searching_algorithms." + module)
        # This is just makes a list of all classes in a given module 
        # I love one line list comprehensions (Thx Haskell)
        moduleClasses = [name for name, obj in inspect.getmembers(algorithmModule)] 
        # filters out any classes that aren't needed (just in case)
        algorithmClass = "".join(filter(filterClassNames, moduleClasses))
        # Create instance of the relevant class 
        algorithmInstance = getattr(algorithmModule, algorithmClass)()
        # Just in case a class that doesn't have the required function slips through the cracks
        try: 
            # Add name of algorithm to list
            algorithmNames.append(algorithmInstance.getName())
        except(AttributeError): 
            print("The getName() method could not be found")
            continue
    # Convert list to tuple and returns it 
    return tuple(algorithmNames)


