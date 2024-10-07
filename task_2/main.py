
def get_cats_info(path):
    # Оброботка исключений при проблемах с файлои или доступом к нему
    try:
        # создание списка словарей
        cats = []
        # безопасное открытие файла
        with open(path, 'r', encoding="utf-8") as fh:
            # создание списка котов
            lines = [el.strip() for el in fh.readlines()]
            for line in lines:
                # раздиление всех элементов одной строки по запятой
                temp = line.split(',')
                # заполнение словаря
                cats.append({"id" : temp[0], "name" : temp[1], "age" : temp[2]})
            return cats
    except FileNotFoundError:
        # Если файл не найден то программа возвращает None и выводит "File not found"
        print("File not found")
        return None
    except UnicodeDecodeError:
        # Если файл не найден то программа возвращает None и выводит "The file is corrupted or cannot be read"
        print("The file is corrupted or cannot be read")
        return None

def main():
    cats_info = get_cats_info("path/to/cats_file.txt")
    if cats_info:
         print(cats_info)
    
if __name__ == '__main__':
    main()