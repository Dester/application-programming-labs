import os
import csv


def write_annotation(annotation_file: str, folder_name: str) -> None:
    """
    Write absolute and relative paths in annotation file
    :param annotation_file: name of annotation file
    :param folder_name: images storage folder
    :return:
    """
    if annotation_file is not None and folder_name is not None:
        data = ["Absolute path", "Relative path"]
        with open(annotation_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            for i in os.listdir(folder_name):
                writer.writerow([os.path.abspath(os.path.join(folder_name, i)), os.path.join(folder_name, i)])
    else:
        raise ValueError("folder name or name of annotation file not found")
