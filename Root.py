from tkinter import *

def create_root_window(window_width, window_height):
    root = Tk()

    progress_frame = Frame(root, name= "progress_frame", bg='blue', width=(window_width * 0.33), height=window_height)
    #sticky= directions (north, south, east, west) to stick too if the cell is larger than the widget -
    # i.e. stick to things when window expans to resize.
    progress_frame.grid(row=0, column=0, sticky="nsew")
    progress_frame.grid_propagate(False)

    step_frame = Frame(root, name= "step_frame", bg='yellow', width=(window_width * 0.67), height=window_height)
    step_frame.grid(row=0, column=1, sticky="nsew")
    step_frame.grid_propagate(False)

    #Allows for the root to resize child objects.
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


    return root