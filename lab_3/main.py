import argparse
import image
import hisgoram
import separation


def parse() -> [str, str]:
    """
    Parse folder name, search word and annotation file name from console
    :return: folder name, search word and annotation file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)
    args = parser.parse_args()
    return args.input_path, args.output_path


def main():
    try:
        parsing = parse()
        input_path = parsing[0]
        output_path = parsing[1]
        img = image.load_image(input_path)
        #img = image.load_image("images/000002.png")
        image.show_image(img, "hedgehog")
        image.image_info(img)
        hisgoram.show_histogram(img)
        red, green, blue = separation.channel_separation(img)
        separation.save_image(red, output_path + "/red.jpg")
        separation.save_image(green, output_path + "/green.jpg")
        separation.save_image(blue, output_path + "/blue.jpg")
        image.show_image(red, "red")
        image.show_image(green, "green")
        image.show_image(blue, "blue")
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except SystemError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
