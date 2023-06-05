# TO DO:
# a logo would be cool but idk where it would be placed (do last, get it working then make it look nice)
# adds button to display a list of algorithms(?)
# Markdown -> Make it look presentable -> title -> table -> introduction paragraph -> list of algorithms

from view import *
from screens import *

if(__name__ == "__main__"):
    view = View(750, 500) 
    view.create()
    view.addScreen(Introduction(view))
    view.show()

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  


