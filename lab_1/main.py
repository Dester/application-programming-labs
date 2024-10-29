import argparse
import re


def get_filename() -> str:
    """
    Считывает название файла из консоли
    :return: название файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    return parser.parse_args().filename


def read_file(filename: str) -> str:
    """
    Считывает данные из файла
    :param filename: название файла
    :return: считанные данные
    """
    if filename is not None:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise FileNotFoundError("File not found")


def search(text: str) -> list:
    """
    Ищет все анкеты с кодом города 927
    :param text: текст, в котором производится поиск
    """
    pattern = r'\d+[)+]\n'
    forms = re.split(pattern, text)
    pattern2 = r'\+7 927'
    form = []
    for i in forms:
        if re.search(pattern2, i):
            form.append(i)
    return form


def prints(form: list) -> None:
    """
    Печатает анкеты, в которых встречается код города 927
    :param list: анкеты
    """
    for i in form:
        print(i)


def main():
    try:
        filename = get_filename()
        text = read_file(filename)
        form = search(text)
        prints(form)
    except FileNotFoundError as exc:
        print("Error: ", exc)
    except Exception as exc:
        print("Error: ", exc)


if __name__ == "__main__":
    main()
