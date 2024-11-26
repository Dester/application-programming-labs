import argparse
import image
import annotation
import ImageIterator


def parse() -> [str, str, str]:
    """
    Parse folder name, search word and annotation file name from console
    :return: folder name, search word and annotation file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", type=str)
    parser.add_argument("search_word", type=str)
    parser.add_argument("annotation_file", type=str)
    args = parser.parse_args()
    return args.folder_name, args.search_word, args.annotation_file


def main():
    try:
        parsing = parse()
        folder_name = parsing[0]
        search_word = parsing[1]
        annotation_file = parsing[2]
        image.get_images(folder_name, search_word)
        annotation.write_annotation(annotation_file, folder_name)
        for images in ImageIterator.ImageIterator(annotation_file):
            print(images)
    except ValueError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
