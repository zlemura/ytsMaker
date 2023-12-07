from tkinter import *
import Root
import WidgetUtilities

def initialise_progress_frame(root):
    progress_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "progress_frame")

    # Five labels for each step name.
    step_1_button = Button(progress_frame, text="1")
    step_2_button = Button(progress_frame, text="2")
    step_3_button = Button(progress_frame, text="3")
    step_4_button = Button(progress_frame, text="4")
    step_5_button = Button(progress_frame, text="5")

    # Position equally throughout frame.
    step_1_button.grid(row=0, column =0, sticky="nesw", padx= 5, pady= 5)
    step_2_button.grid(row=1, column=0, sticky="nesw", padx= 5, pady= 5)
    step_3_button.grid(row=2, column=0, sticky="nesw", padx= 5, pady= 5)
    step_4_button.grid(row=3, column=0, sticky="nesw", padx= 5, pady= 5)
    step_5_button.grid(row=4, column=0, sticky="nesw", padx= 5, pady= 5)

    for column_number in range(0,progress_frame.grid_size()[0]):
        progress_frame.grid_columnconfigure(column_number, weight=1)

    for row_number in range(0,progress_frame.grid_size()[1]):
        progress_frame.grid_rowconfigure(row_number, weight=1)

    return root

