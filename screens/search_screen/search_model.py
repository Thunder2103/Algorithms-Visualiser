class SearchModel(): 
    def __init__(self) -> None: 
        # Dictionary pairing numbers to speed 
        # This allows the slider to show text rather than just numbers
        self.__numbersToText = {
            0: "Target: Random", 
            1: "Target: In array",
            2: "Target: Not in array"
        } 

    # Returns the text to be displayed above the target slider 
    def getSliderText(self, sliderValue : int) -> str: 
        return self.__numbersToText[sliderValue]
    
# Listen to Creep by Radiohead