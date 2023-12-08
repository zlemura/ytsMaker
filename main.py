import ProgressFrame
import Root
import StepFrame
import TikTokLinkCapture

#TODO
# Show screen for capturing TikTok link.
# Download TikTok video.
# Show screen for specifying narration.
# Take narration and generate narration audio.
# Take narration and generate narration video.
# Show screen for positioning narration video.
# Show video in frame.
# Drag and drop narration video.
# Resize narration video.
# Generate final video.


def main():
    window_width = 800
    window_height = 800
    root = Root.create_root_window(window_width, window_height)
    root = ProgressFrame.initialise_progress_frame(root)
    root = StepFrame.initialise_step_frame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

