import cv2
import numpy as np


def channel_separation(img: np.ndarray) -> [np.ndarray, np.ndarray, np.ndarray]:
    """
    Splits the image into channels
    :param img: The image
    :return: Channelized images
    """
    if img is not None:
        red, green, blue = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        return red, green, blue
    else:
        raise FileNotFoundError("Image not found")


def save_image(img: np.ndarray, output_path: str) -> None:
    """
    Save the image along the specified path
    :param img: The image
    :param output_path: output path
    """
    if img is not None:
        if not (cv2.imwrite(output_path, img)):
            raise SystemError("Could not save file to specified path")
    else:
        raise FileNotFoundError("Image not found")