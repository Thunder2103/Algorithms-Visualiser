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
# Provided files containing algorithms follow the naming convention -> (name)_(algorithm type).py
def filterFileNames(file : str, algorithmType : str) -> bool:
    return True if file.split("_")[-1] == f"{algorithmType}.py" else False 

# Checks that relevant files follow inheritance and naming convenvtions 
# Checks if any class name has words "Algorithm" or "Search" in them
def filterClassNames(className : str, classType : str) -> bool:
    return True if classType in className or "Algorithm" in className else False

# Returns the name of each algorithm that has been written
# Provided the naming conventions have been followed
def getAlgorithms(algorithmsType : str) -> tuple: 
    # Converts passed string to lower case
    algorithmsType = algorithmsType.lower()
    # Get the name of each algorithm module
    moduleNames = getModuleNames(algorithmsType) 
    # Returns a list of the every algorithms name
    return getAlgorithmNames(moduleNames, algorithmsType)

# Gets modules names in this package 
def getModuleNames(algorithmsType : str) -> list:
    path = f"./algorithms/{algorithmsType}ing"
    # Gets every file in the given directory
    # and filters out files that don't follow the specified naming convention
    algorithmFiles = filter(lambda file : filterFileNames(file, algorithmsType), os.listdir(path)) 
    # removes the .py file extension - leaving only the module names
    return [module.removesuffix(".py") for module in algorithmFiles]

def errorWrapper(errorMessage : str) -> None:
    print(errorMessage, file=sys.stderr)

# Returns a tuple containing every algorithms name 
# So the names can be seen in the drop down menu
def getAlgorithmNames(modules : list, algorithmsType : str) -> tuple:
    algorithmNames = []
    # Class type is the algorithm type with the first letter capitalized 
    classType = algorithmsType.capitalize()
    # Imports relevant modules and gets relevant classes
    for module in modules:
        # Imports module
        try:
            algorithmModule = importlib.import_module(f"algorithms.{algorithmsType}ing." + module)
        # Incase there is an error importing the module
        except Exception as error:
            errorWrapper(f"Could not import algorithms.{algorithmsType}ing.{module}")
            continue
       
        # This just creates a list of all classes in the imported module 
        # I love one line list comprehensions (Thx Haskell)
        moduleClasses = [name for name, _ in inspect.getmembers(algorithmModule)] 
        # filters out any classes that aren't needed (classes that don't meet the naming convnetions or don't subclass the Algorithm class)
        algorithmClasses = list((filter(lambda algorithmClass: filterClassNames(algorithmClass, classType), moduleClasses)))
        
        # Checks algorithm class has at least imported the Algorithm class
        if "Algorithm" in algorithmClasses: algorithmClasses.remove("Algorithm")
        else:
            errorWrapper(f"{module} is not a child of Algorithm class")
            continue

        # If the list is empty then the algorithms type was not included in the classes name
        if not algorithmClasses: 
            errorWrapper(f"{module} does not contain '{classType}' in class name")
            continue

        # Checks if the class name ends with the algorithms type 
        # If not then the naming convention has not been followed and the algorithm won't be added
        if not algorithmClasses[0].endswith(classType): 
            errorWrapper(f"{module} class name does not end in {classType}")
            continue 
        
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
