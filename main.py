import app_window as w
import screens as sc

if(__name__ == "__main__"):
    window = w.Window(750, 500) 
    window.create()
    window.loadScreen(sc.IntroductionScreen(window))
    window.show() 
else:
    print("This file has no functions to import")

# Subscribe to Computerphile 
# Listen to Walk by foo fighters  