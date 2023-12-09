from tkinter import *
from tkVideoPlayer import TkinterVideo

import WidgetUtilities

# https://github.com/PaulleDemon/tkVideoPlayer/blob/master/examples/sample_player.py

# TODO
# Download video from URL.
# Set video as source for VideoPlayer.
# Add seek controls.
# Add next step button.

def initialise_frame(root):
    step_frame = WidgetUtilities.fetch_widget_by_name_from_root(root, "step_frame")

    step_one_frame = Frame(step_frame, name="step_one_frame", bg="white", width=step_frame.winfo_reqwidth(),
                           height=step_frame.winfo_reqheight())
    step_one_frame.grid_propagate(False)
    step_one_frame.grid(row=0, column=0, sticky="nsew")
    step_one_frame.grid_propagate(False)

    #Entry Frame.
    entry_frame = Frame(step_one_frame, name="entry_frame_step_one_frame", bg="green")
    entry_frame.grid(row=0, column=0, sticky="nsew")

    entry_frame.grid_columnconfigure(0, weight=1)

    #Label.
    Label(entry_frame, text = "Please specify TikTok URL:").grid(row=0, column=0, sticky="nsew")

    #Entry.
    tiktok_url_var = StringVar()
    tiktok_url_input = Entry(entry_frame, textvariable=tiktok_url_var, highlightthickness=2, highlightcolor="black")
    tiktok_url_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    def clear_temp_text(e):
        tiktok_url_input.delete(0, "end")
    tiktok_url_input.insert(0, "e.g. https://www.tiktok.com/@aejjmbk/video/7298709426490379526")
    tiktok_url_input.bind("<FocusIn>", clear_temp_text)

    #Fetch video Button.
    fetch_video_button = Button(entry_frame, text="Fetch video")
    fetch_video_button.grid(row=2, column=0, padx=10, pady=10)

    #Video Player.
    video_player = TkinterVideo(step_one_frame, scaled=True)
    video_player.load(r"assets/sample videos/file_example_MP4_1280_10MG.mp4")
    video_player.grid(row=2, column=0, sticky="nsew")
    video_player.pause()

    # Video control frame.
    video_control_frame = Frame(step_one_frame, name="video_control_step_one_frame", bg="red")
    video_control_frame.grid(row=1, column=0, sticky="nsew")

    # Play/Pause Button.
    play_pause_button = Button(video_control_frame, text="Play")
    play_pause_button.configure(command= lambda: play_pause(video_player, play_pause_button))
    play_pause_button.grid(row=2, column=0)


    # Row 0 = input.
    # Row 1 = video controls.
    # Row 2 = preview.

    for column_number in range(0, step_one_frame.grid_size()[0]):
        step_one_frame.grid_columnconfigure(column_number, weight=1)

    step_one_frame.grid_rowconfigure(0, weight=1)
    step_one_frame.grid_rowconfigure(1, weight=1)
    step_one_frame.grid_rowconfigure(2, weight=10)

    '''
    for row_number in range(0, step_one_frame.grid_size()[1]):
        step_one_frame.grid_rowconfigure(row_number, weight=1)
    '''

    return root

def play_pause(video_player, play_pause_button):
    print("Playing or pausing!")
    """ pauses and plays """
    if video_player.is_paused():
        video_player.play()
        play_pause_button["text"] = "Pause"

    else:
        video_player.pause()
        play_pause_button["text"] = "Play"