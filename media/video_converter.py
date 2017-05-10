import subprocess

class VideoConverter():
    def transformImageToVideo(self, image , video_output):
        cmd = "ffmpeg -loop 1 -i %s -t 2 -c:v libx264 -preset ultrafast -pix_fmt yuv420p %s" %(image, video_output)
        subprocess.call(cmd, shell=True)
