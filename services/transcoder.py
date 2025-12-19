import os
import ffmpeg

class VideoTranscoder:
    def __init__(self,input_file,output_dir):
        self.input_file = input_file
        self.output_dir = output_dir

    def transcode(self):
        """
        Takes the input video and converts it into HLS format
        with multiple resolutions (variants).
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        renditions = [
            {'name': '1080p', 'width': 1920, 'height': 1080, 'bitrate': '5000k'},
            {'name': '720p', 'width': 1280, 'height': 720, 'bitrate': '2800k'},
            {'name': '480p', 'width': 854, 'height': 480, 'bitrate': '1400k'},
            {'name': '360p', 'width': 640, 'height': 360, 'bitrate': '800k'},
        ]
        # 1. Create the Master Playlist (the main menu)
        # This file just points to the other playlists.
        master_playlist_path = os.path.join(self.output_dir, 'master.m3u8')
        with open(master_playlist_path, 'w') as f:
            f.write('#EXTM3U\n#EXT-X-VERSION:3\n')
            for r in renditions:










