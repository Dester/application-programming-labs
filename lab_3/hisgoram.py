import cv2
import matplotlib.pyplot as plt
import numpy as np


def make_histogram(img: np.ndarray, channel: int) -> np.ndarray:
    """
    Make histogram
    :param img: The image
    :param channel: The channel in image
    :return: A histogram made by the color of a given channel
    """
    if img is not None:
        histogram = cv2.calcHist([img], [channel], None, [256], [0, 256])
        return histogram
    else:
        raise FileNotFoundError("Image not found")


def show_histogram(img: np.ndarray) -> None:
    """
    Show the histogram made by the all color
    :param img: The image
    """
    colors = ("b", "g", "r")
    plt.title("Histogram")
    plt.xlabel("Brightness")
    plt.ylabel("Number of pixels")
    for channel, color in enumerate(colors):
        hist = make_histogram(img, channel)
        plt.plot(hist, color=color)
        plt.xlim([0, 255])
    plt.show()