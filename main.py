from view import *
from screens import *

if(__name__ == "__main__"):
    view = View(1250, 500) 
    view.create()
    view.addScreen(Introduction(view))
    view.show() 
else:
    print("This file has no functions to import")

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  


