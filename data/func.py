from typing import Any, Generator, List


def get_logs() -> None:
    """
    Функция считывания текстового файла
    :return: возвращает данные файла в виде списка строк
    """
    with open('apache_logs.txt', encoding='utf-8') as file:
        content = [_.strip() for _ in file]
    return content



def limit(lim: str, it: Any) -> list:
    """
    :param it:файл из которого нужно вытащить определенное количество строк
    :param lim: количество строк
    :return: возвращаем столько строк сколько указано в limit
    """
    return it[:int(lim)]


def sorting(val: str, it: Any) -> list:
    """
    :param it: объект требующий сортировки
    :param order:  в каком порядке сортировка
    :return: отсортированный объект
    """
    flag = False
    if val == 'desc':
        flag = True
    return sorted(it, reverse=flag)


def unique(_, it: Any) -> list:
    """
    :param it: передаваемый объект для уникализации его элементов или его самого
    :return: возврашает уникальные элементы объекта
    """
    return list(set(it))


def filtering(line: str, it: list) -> list:
    """
    :param line: строка которую мы ищем
    :param it: фильтрируемый объект
    :return:возвращает список строк имеющих строку line
    """
    return list(filter(lambda x: line in x, it))


def mapping(column: str, it: list) -> list:
    s = list(map(str.split, it))
    return [i[int(column)] for i in s]
