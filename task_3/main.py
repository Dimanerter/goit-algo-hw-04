import sys
from pathlib import Path
from colorama import Fore

# создание функции для красивого вывода 
def tree(directory, space = "|---"):
    # проверка существует ли директория, и является ли она директорией  
    if directory.is_dir() and directory.exists():
        if space == "|---":
            print(Fore.YELLOW + directory.name + Fore.RESET)
        # создание списка файлов и директорий в указаной директории
        items = list(directory.iterdir())
        # первый проход по директории в поисках других директорий
        for item in items:
            if item.is_dir():
                # если директория найдена то выводиться ее имя в необходимом цвете
                print(space, Fore.YELLOW + item.name + Fore.RESET)
                # запуск рекурсии что б найти все файлы в найденной директории
                tree(item, '    ' + space)
        # после нахождения всех директорий начинаеться поиск файлов
        for item in items:
            if item.is_file():
                # после того, как файл найден, 
                format = item.name.split('.')[1]
                # создание match для добавления разного цывета именам файлов при разном разширении файлов
                match format:
                    # указание цвета для png файлов
                    case 'png':
                        print(space, Fore.MAGENTA + item.name + Fore.RESET)
                    # указание цвета для svg файлов
                    case 'svg':
                        print(space, Fore.LIGHTCYAN_EX + item.name + Fore.RESET)
                    # указание цвета для jpg файлов
                    case 'jpg':
                        print(space, Fore.LIGHTRED_EX + item.name + Fore.RESET)
                    # указание цвета для всех отсльных файлов
                    case _:
                        print(space, item.name)
    else:
        # если директория не найдена
        print('Directory with this name does not exist')

    

def main():
    tree(Path(sys.argv[1]))
    # directory = Path(sys.argv[1])
    # if directory.is_dir() and directory.exists():
    #     print(Fore.YELLOW + directory.name + Fore.RESET)
    #     tree(directory)
    # else:
    #     print('Directory with this name does not exist')

if __name__ == "__main__":
    main()
