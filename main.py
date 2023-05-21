import tkinter as tk 

# Size of the application
window_width = 750 
window_height = 500

# Size of bodyFrame 
# The body frame is made smaller than the window by a small offset
# Creates a nice border and makes UI look less cluttered
bodyFrame_width = window_width - 15
bodyFrame_height = window_height - 15

# The introductory text is kept as a string 
# as it makes it easier to change (and makes code easier to read)
introText = "This program visualises algorithms in a user friendly way. \n\
    Including array searching and sorting and tree traversal algorithms. \n\
        Press one of the buttons to start."


# Declaring window
window = tk.Tk()
window.title('Useful Algorithms')
# windows dimensions
window.geometry(f'{window_width}x{window_height}')
window.resizable(False, False)
#changed window colour to grey 
# gives window solid black border
window.config(bg = "#CCCCCC", borderwidth = 2, relief = "solid")

# Declaring and customising the frame
bodyFrame = tk.Frame(window, height = bodyFrame_height, width = bodyFrame_width, borderwidth = 2, relief = "solid", bg = "white")

# Header label
header = tk.Label(bodyFrame, text = "Welcome to [name pending].", font = ("Arial", 18, "underline"), bg = "white")\
    .pack(pady = 10)

# Label that contains the introduction text
introPara = tk.Label(bodyFrame, text = introText, font = ("Arial", 14), justify = "center", bg = "white")\
    .pack(pady = 5)


# Adds a frame for the buttons widgets 
# Adding this frame makes positioning the buttons much easier
buttonsFrame = tk.Frame(bodyFrame, bg = "white")
buttonsFrame.pack()

treeButton = tk.Button(buttonsFrame, text = "Tree Traversal", font = ("Arial", 12), height = 2, width = 15, relief = "solid")\
    .pack(pady = (25, 0)) 

searchButton = tk.Button(buttonsFrame, text = "Searching",  font = ("Arial", 12), height = 2, width = 15, relief = "solid")\
    .pack(side = "left", pady = 15, padx = (100, 0))

sortButton = tk.Button(buttonsFrame, text = "Sorting",  font = ("Arial", 12), height = 2, width = 15, relief = "solid")\
    .pack(side = "left", padx = 100) 

credits = tk.Label(bodyFrame, text = "Created by Thomas Gibson", bg = "white", justify = "left")\
    .pack(side = "bottom", anchor = "w", pady = 10, padx = 10)


 # Makes the frame centred in the GUI window
bodyFrame.place(relx = .5, rely = .5, anchor = "center")

# Stops frame resizing to same size as components inside it 
bodyFrame.pack_propagate(False)

#draws window
window.mainloop()
