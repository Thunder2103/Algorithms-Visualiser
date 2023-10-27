from Window import Window 
from Introduction_Screen import Introduction

if(__name__ == "__main__"):
    window = Window(750, 500) 
    window.create()
    window.addScreen(Introduction(window))
    window.show()  
else:
    print("This file has no functions to import")

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  