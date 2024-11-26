from icrawler.builtin import GoogleImageCrawler


def get_images(folder_name: str, search_word: str) -> None:
    """
    Search and download images for this word
    :param folder_name: images storage folder
    :param search_word: word by which the search is performed
    """
    if folder_name is not None and search_word is not None:
        google_crawler = GoogleImageCrawler(storage={'root_dir': folder_name})
        google_crawler.crawl(keyword=search_word, max_num=90)
    else:
        raise ValueError("folder name or search word not found")
