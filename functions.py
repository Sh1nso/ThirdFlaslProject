from json import loads, dump, JSONDecodeError


def get_data_from_json():
    """
    Получает данные из JSON файла
    """
    try:
        with open("posts.json", encoding='utf-8') as file:
            data = loads(file.read())
    except FileNotFoundError:
        return f'Файл не найден'
    except JSONDecodeError:
        return f'Файл не удается преобразовать'
    return data


def search_post_by_user_words(user_words: str) -> list[dict]:
    """
    Ищет совпадения заданного слова пользователя с имеющимися данными
    """
    list_of_posts = []
    for post in get_data_from_json():
        print(post)
        if user_words.lower() in post['content'].lower():
            list_of_posts.append(post)
    return list_of_posts


def append_post_to_data(some_post: dict):
    """
    Добавляет данные о посте пользователя в JSON файл и перезаписывает его
    """
    try:
        with open("posts.json", 'r', encoding='utf-8') as file:
            data = loads(file.read())
            data.append(some_post)
        with open("posts.json", 'w', encoding='utf-8') as file1:
            dump(data, file1, ensure_ascii=False)
    except FileNotFoundError:
        return f'Файл не найден'
    except JSONDecodeError:
        return f'Файл не удается преобразовать'


def is_filename_allowed(filename):
    """
    Проверяет расширешние файла на совпадение с разрешенными
    """
    extension = filename.split(".")[-1]
    if extension in ['png', 'jpg']:
        return True
    return False
