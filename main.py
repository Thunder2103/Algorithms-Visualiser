from app_window import Window
from screens import IntroductionScreen

if(__name__ == "__main__"):
    window = Window(750, 500) 
    window.create()
    window.loadScreen(IntroductionScreen(window))
    window.show() 
else:
    print("This file has no functions to import")

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  
