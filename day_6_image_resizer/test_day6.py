import os
from pathlib import Path
import unittest
from .day6 import ImageResizer

base_dir = Path(__file__).resolve().parent
photo_path = os.path.join(base_dir, 'photo')
destination_path = os.path.join(base_dir, 'smaller')


class TestImageResizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test = ImageResizer(photo_path, destination_path)
        print('Test for TestImageResizer started now..')

    def test_read_all_in(self):
        self.assertTrue(os.path.isdir(photo_path))
        self.assertCountEqual(self.test.read_all_in(), {
            'cat.jpg': os.path.join(base_dir, 'photo', 'cat.jpg'),
            'cat1.jpg': os.path.join(base_dir, 'photo', 'cat1.jpg')}
                              )

    def test_get_pixels_size_of(self):
        self.assertEqual(self.test.get_pixels_size_of(os.path.join(base_dir, 'photo', 'cat.jpg')), (512, 384))
        self.assertEqual(self.test.get_pixels_size_of(os.path.join(base_dir, 'photo', 'cat.jpg')), (607, 1024))

    def test_resize_all_images_in_and_save_to(self):
        self.assertTrue(os.path.isdir(destination_path))
        self.assertTrue(os.path.isdir(os.path.join(destination_path,'smaller', 'cat.jpg')))
        self.assertTrue(os.path.isdir(os.path.join(destination_path, 'smaller', 'cat1.jpg')))


    def test_get_image_folder_size(self):
        pass

    def test_calculate_saved_space_between(self):
        pass

    def test_recalculate_from_bytes_to_mg(self):
        pass


if __name__ == '__main__':
    unittest.main()
    print(base_dir)