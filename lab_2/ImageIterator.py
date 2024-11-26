import csv


class ImageIterator:
    def __init__(self, annotation_file: str):
        self.annotation_file = annotation_file
        self.images_path = self.__get_images_path()
        self.limit = len(self.images_path)
        self.counter = 0

    def __get_images_path(self) -> list:
        with open(self.annotation_file, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            return [row[1] for row in reader]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.images_path[self.counter - 1]
        else:
            raise StopIteration
