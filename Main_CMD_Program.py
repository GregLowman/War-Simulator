"""Use ffprobe to detect video rotation (0, 90, 180, or 270 degrees)."""
import subprocess
import shlex
import json


def get_rotation(file_path_with_file_name):
    """
    Function to get the rotation of the input video file.
    Adapted from gist.github.com/oldo/dc7ee7f28851922cca09/revisions using the ffprobe comamand by Lord Neckbeard from
    stackoverflow.com/questions/5287603/how-to-extract-orientation-information-from-videos?noredirect=1&lq=1

    Returns a rotation None, 90, 180 or 270
    """
    cmd = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1"
    args = shlex.split(cmd)
    args.append(file_path_with_file_name)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobe_output = subprocess.check_output(args).decode('utf-8')
    if len(ffprobe_output) > 0:  # Output of cmdis None if it should be 0
        ffprobe_output = json.loads(ffprobe_output)
        rotation = ffprobe_output

    else:
        rotation = 0

    return rotation


video_path = "C:/Users/glowm/OneDrive/Desktop/new_database/" \
             "First Neighborhood/Videos/DJI_20220519_114715_641_video.MP4"

video_2_path = "C:/Users/glowm/OneDrive/Desktop/new_database/" \
               "First Neighborhood/Videos/DJI_20220519_114746_984_video.MP4"

get_rotation(video_2_path)
