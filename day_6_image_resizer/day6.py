import os
from PIL import Image
from typing import Dict


class ImageResizer:
    def __init__(self, file_path: str, destination_path: str) -> None:
        """
        :param file_path: folder path were original images are saved,
        :param destination_path:  folder path were processed images should be saved
        """
        self.file_path = file_path
        self.destination_path = destination_path

    def read_all_in(self) -> Dict:
        """
        get all file paths from folder directory
        :return: dictionary with key: file name and value as file path
        """
        image_paths = {file: os.path.join(self.file_path, file)
                       for file in os.listdir(self.file_path) if file.endswith('.jpg')}
        return image_paths

    @staticmethod
    def get_pixels_size_of(image: Image) -> tuple:
        """
        get pixels size of image
        :param image: image for which should be return size
        :return: height and width for image
        """
        width, height = image.size
        return width, height

    def resize_all_images_in_and_save_to(self) -> None:
        """
        resize all images and save to new location
        :return: None
        """
        paths = self.read_all_in()
        for file, filepath in paths.items():
            image = Image.open(filepath)
            new_image = image.copy()
            width, height = self.get_pixels_size_of(image)
            base_dir = os.path.join(self.destination_path, file)
            with open(base_dir, 'w') as f:
                pass
            new_image.save(base_dir)
            new_image.resize((int(width/2), int(width/2)))


    @staticmethod
    def get_image_folder_size(file_path: str) -> int:
        """
        get size of the folder
        :param file_path: path for folder
        :return:size of folder in bytes
        """
        return sum(os.path.getsize(file) for file in os.listdir(file_path) if os.path.isfile(file_path))

    def calculate_saved_space_between(self) -> int:
        """
        calculate saved space between original folder and processed folde
        :return: saved space in bytes
        """
        size_of_original_path = self.get_image_folder_size(self.file_path)
        size_of_processed_path = self.get_image_folder_size(self.destination_path)
        return size_of_original_path-size_of_processed_path

    def recalculate_from_bytes_to_kilo(self) -> float:
        """
        recalculation size from bytes to kilobytes
        :return: size in megabytes
        """
        size = self.calculate_saved_space_between()
        return round(size/1024, 2)

    @property
    def savings(self):
        return self.recalculate_from_bytes_to_kilo()


def main():
    base_dir = os.getcwd()
    #folder with photos to process
    photo_path = os.path.join(base_dir, 'photo')
    #folder for pocessed photos
    destination_path = os.path.join(base_dir, 'smaller')
    #init program
    conversion = ImageResizer(photo_path, destination_path)
    #print result and savings in mb
    print(conversion.savings)


if __name__ == '__main__':
    main()
