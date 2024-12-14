import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_image(path: str) -> np.ndarray:
    """
    Load the image as specified path
    :param path: path to the image
    :return: The image
    """
    img = cv2.imread(path)
    if img is not None:
        return img
    else:
        raise FileNotFoundError("Image not found")


def show_image(img: np.ndarray, title: str) -> None:
    """
    Shows the image
    :param img: The image
    :param title: The title of image
    """
    if img is not None:
        plt.title(title)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
    else:
        raise FileNotFoundError("Image not found")


def image_info(img: np.ndarray):
    """
    Print information about image
    :param img: The image
    """
    if img is not None:
        height, width, channels = img.shape
        print(f"height: {height}, width: {width}, channels: {channels}")
    else:
        raise FileNotFoundError("Image not found")