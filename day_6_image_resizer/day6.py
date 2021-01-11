"""
#IMAGE #RESIZER
Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne (w określonych formatach,
 np. jpg, png, bmp itp.), następnie zmniejszy ich rozdzielczość o 50% i zapisze je w podkatalogu “smaller”
  z odpowiednimi nazwami. Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami.
Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji
(odczytaj rozmiar plików w pierwotnym folderze oraz "smaller" i porównaj obie wartości - bezwzględnie i w %)
"""

import os
from PIL import Image
from typing import Dict


class ImageResizer:
    def __init__(self, file_path: str, destination_path: str) -> None:
        self.file_path = file_path
        self.destination_path = destination_path

    def read_all_in(self) -> Dict:
        image_paths = {file: os.path.join(self.file_path, file) for file in os.listdir(self.file_path) if file.endswith('.jpg')}
        return image_paths

    @staticmethod
    def get_pixels_size_of(image: Image) -> tuple:
        height, width = image.size
        return height, width

    def copy_all_images_in_and_save_to(self) -> None:
        paths = self.read_all_in()
        for file, filepath in paths.items():
            image = Image.open(filepath)
            height, width = self.get_pixels_size_of(image)
            new_image = image.resize((height/2, width/2))
            base_dir = os.path.join(self.destination_path, file)
            with open(base_dir, 'w') as f:
                pass
            new_image.save(base_dir)

    @staticmethod
    def get_image_folder_size(file_path:str) -> int:
        return sum(os.path.getsize(file) for file in os.listdir(file_path) if os.path.isfile(file_path))

    def calculate_saved_space_between(self) -> int:
        size_of_original_path = self.get_image_folder_size(self.file_path)
        size_of_processed_path = self.get_image_folder_size(self.destination_path)
        return size_of_original_path-size_of_processed_path

    def recalculate_from_bytes_to_mg(self) -> float:
        size = self.calculate_saved_space_between()
        return round(size/1024, 2)

    @property
    def savings(self):
        return self.recalculate_from_bytes_to_mg()


def main():
    base_dir = os.getcwd()
    photo_path = os.path.join(base_dir, 'photo')
    destination_path = os.path.join(base_dir, 'smaller')
    conversion = ImageResizer(photo_path, destination_path)
    print(conversion.savings)


if __name__ == '__main__':
    main()