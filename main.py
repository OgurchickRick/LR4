import os


def way():
    while True:
        way = str(input('Введите путь до папки:'))
        if os.path.exists(way):
            return way
        else:
            print("Неверный путь")


def dictionary(way):
    result = {}
    for filename in os.listdir(way):
        current_path = os.path.join(way, filename)
        if os.path.isdir(current_path):
            result.update(dictionary(current_path))
        else:
            result.update({current_path: os.path.getsize(current_path)})
    return result


def duplicate(a):
    copies = {}
    for key1 in a:
        for key2 in a:
            if key1 == key2:
                pass
            elif os.path.basename(key1) == os.path.basename(key2) and a[key1] == a[key2]:
                if key1 in copies:
                    continue
                copies.update({key1: a[key1]})
    else:
        return copies


def print_duplicate(copies):
    if copies == {}:
        print('Нет дубликатов')
    garbage = []
    for key1 in copies:
        if key1 not in garbage:
            print('\n', '-----', os.path.getsize(key1), 'байт -----')
            print(key1)
            for key2 in copies:
                if key1 == key2:
                    pass
                elif os.path.basename(key1) == os.path.basename(key2) and copies[key1] == copies[key2]:
                    print(key2)
                    garbage.append(key2)


if __name__ == '__main__':
    p = way()
    s = dictionary(p)
    duplicate(s)
    d = duplicate(s)
    print_duplicate(d)
