from tkinter import *
import Root
import StepFrame
import WidgetUtilities

def initialise_progress_frame(root):
    progress_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "progress_frame")

    # Five labels for each step name.
    step_1_button = Button(progress_frame, text="1", command=lambda: raise_step_frame_by_number(1, root))
    step_2_button = Button(progress_frame, text="2", command=lambda: raise_step_frame_by_number(2, root))
    step_3_button = Button(progress_frame, text="3", command=lambda: raise_step_frame_by_number(3, root))
    step_4_button = Button(progress_frame, text="4", command=lambda: raise_step_frame_by_number(4, root))
    step_5_button = Button(progress_frame, text="5", command=lambda: raise_step_frame_by_number(5, root))

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

def raise_step_frame_by_number(step_number, root):
    frame = None

    if step_number == 1:
        step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")
        frame = WidgetUtilities.fetch_widget_by_name_from_frame(step_frame, "step_one_frame")
    if step_number == 2:
        step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")
        frame = WidgetUtilities.fetch_widget_by_name_from_frame(step_frame, "step_two_frame")
    if step_number == 3:
        step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")
        frame = WidgetUtilities.fetch_widget_by_name_from_frame(step_frame, "step_three_frame")
    if step_number == 4:
        step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")
        frame = WidgetUtilities.fetch_widget_by_name_from_frame(step_frame, "step_four_frame")
    if step_number == 5:
        step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")
        frame = WidgetUtilities.fetch_widget_by_name_from_frame(step_frame, "step_five_frame")

    if frame != None:
        frame.tkraise()