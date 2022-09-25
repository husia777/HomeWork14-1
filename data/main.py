from func import *


def main(list1):
    for i in input('Введите команды').split('|'):
        user_cmd, value_cmd = i.split()
        if user_cmd in dict_cmd:
            list1 = dict_cmd[user_cmd](value_cmd, list1)
        else:
            print('Ошибка ввода')
            return
    print(*list1, sep='\n')






dict_cmd = {'filter': filtering,
            'unique': unique,
            'map': mapping,
            'sort': sorting,
            'limit': limit
            }

if __name__ == "__main__":
    main(get_logs())