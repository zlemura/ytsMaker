from tkinter import *
import WidgetUtilities

def initialise_step_frame(root):
    step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")

    step_one_frame = Frame(step_frame, name="step_one_frame", bg="white", width=step_frame.winfo_reqwidth(), height=step_frame.winfo_reqheight())
    step_one_frame.grid_propagate(False)
    Label(step_one_frame, text="1").grid(row=0, column=0, sticky="nsew")
    step_one_frame.grid(row=0, column=0, sticky="nsew")
    for column_number in range(0, step_one_frame.grid_size()[0]):
        step_one_frame.grid_columnconfigure(column_number, weight=1)
    for row_number in range(0, step_one_frame.grid_size()[1]):
        step_one_frame.grid_rowconfigure(row_number, weight=1)

    step_two_frame = Frame(step_frame, name="step_two_frame", bg="white", width=step_frame.winfo_reqwidth(),
                           height=step_frame.winfo_reqheight())
    step_two_frame.grid_propagate(False)
    Label(step_two_frame, text="2").grid(row=0, column=0, sticky="nsew")
    step_two_frame.grid(row=0, column=0, sticky="nsew")
    for column_number in range(0, step_two_frame.grid_size()[0]):
        step_two_frame.grid_columnconfigure(column_number, weight=1)
    for row_number in range(0, step_two_frame.grid_size()[1]):
        step_two_frame.grid_rowconfigure(row_number, weight=1)

    step_three_frame = Frame(step_frame, name="step_three_frame", bg="white", width=step_frame.winfo_reqwidth(),
                           height=step_frame.winfo_reqheight())
    step_three_frame.grid_propagate(False)
    Label(step_three_frame, text="3").grid(row=0, column=0, sticky="nsew")
    step_three_frame.grid(row=0, column=0, sticky="nsew")
    for column_number in range(0, step_three_frame.grid_size()[0]):
        step_three_frame.grid_columnconfigure(column_number, weight=1)
    for row_number in range(0, step_three_frame.grid_size()[1]):
        step_three_frame.grid_rowconfigure(row_number, weight=1)

    step_four_frame = Frame(step_frame, name="step_four_frame", bg="white", width=step_frame.winfo_reqwidth(),
                             height=step_frame.winfo_reqheight())
    step_four_frame.grid_propagate(False)
    Label(step_four_frame, text="4").grid(row=0, column=0, sticky="nsew")
    step_four_frame.grid(row=0, column=0, sticky="nsew")
    for column_number in range(0, step_four_frame.grid_size()[0]):
        step_four_frame.grid_columnconfigure(column_number, weight=1)
    for row_number in range(0, step_four_frame.grid_size()[1]):
        step_four_frame.grid_rowconfigure(row_number, weight=1)

    step_five_frame = Frame(step_frame, name="step_five_frame", bg="white", width=step_frame.winfo_reqwidth(),
                            height=step_frame.winfo_reqheight())
    step_five_frame.grid_propagate(False)
    Label(step_five_frame, text="5").grid(row=0, column=0, sticky="nsew")
    step_five_frame.grid(row=0, column=0, sticky="nsew")
    for column_number in range(0, step_five_frame.grid_size()[0]):
        step_five_frame.grid_columnconfigure(column_number, weight=1)
    for row_number in range(0, step_five_frame.grid_size()[1]):
        step_five_frame.grid_rowconfigure(row_number, weight=1)

    return root

def raise_frame(frame):
    frame.tkraise()