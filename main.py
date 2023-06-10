# TO DO:
# a logo would be cool but idk where it would be placed (do last, get it working then make it look nice)
# adds button to display a list of algorithms(?) 
# Add layout adapting for different widths and heights -> update_idletasks()

from view import *
from screens import *

if(__name__ == "__main__"):
    view = View(800, 550) 
    view.create()
    view.addScreen(Introduction(view))
    view.show() 
else:
    print("This file has no functions to import")

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  


