from unittest import TestCase
from .day6 import ImageResizer

base_dir = ""
new_dir = ""

class TestImageResizer(TestCase):

    def setUpClass(self):
        print('Test for TestImageResizer started now..')
        test_object = ImageResizer(base_dir, new_dir)

