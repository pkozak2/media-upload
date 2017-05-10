import unittest
import os
from media.video_converter import VideoConverter

class TestVideoConverter(unittest.TestCase):
   def getAbsolutePath(self, filename):
       return os.path.join(os.path.dirname(__file__), filename)
   def setUp(self):
       video = self.getAbsolutePath('example.mov')
       if os.path.exists(video):
           os.remove(video)

   def test_run_video_converter(self):
       image = self.getAbsolutePath('example.png')
       video_output = self.getAbsolutePath('example.mov')
       converter = VideoConverter()
       converter.transformImageToVideo(image, video_output)
       assert(os.path.exists(video_output))
