import sys
from pathlib import Path
from colorama import init, Fore, Style

def main():
    """
    Головна функція для обробки аргументів командного рядка та ініціації виведення структури директорії.
    """
    # Ініціалізація colorama для кольорового виведення
    init()

    # Перевірка наявності шляху до директорії
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python hw03.py /шлях/до/директорії" + Style.RESET_ALL)
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    # Перевірка існування шляху та чи є він директорією
    if not dir_path.exists():
        print(Fore.RED + f"Помилка: Шлях '{dir_path}' не існує." + Style.RESET_ALL)
        sys.exit(1)
    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: Шлях '{dir_path}' не є директорією." + Style.RESET_ALL)
        sys.exit(1)

    # Початок виведення структури директорії
    print(Fore.BLUE + dir_path.name + Style.RESET_ALL)
    display_directory_structure(dir_path)

def display_directory_structure(path, prefix=''):
    """
    Рекурсивно виводить структуру директорії, починаючи з заданого шляху.

    :param path: Об'єкт Path, що представляє директорію для виведення
    :param prefix: Рядок, що використовується для відступів у виведенні
    """
    # Список всіх елементів у директорії, сортування директорій перед файлами
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    # Ітерація по елементах з їх індексом
    for index, item in enumerate(items):
        # Визначення відповідного з'єднувача
        connector = '└── ' if index == len(items) - 1 else '├── '

        if item.is_dir():
            # Виведення назви директорії синім кольором
            print(prefix + connector + Fore.BLUE + item.name + Style.RESET_ALL)
            # Розширення префіксу для піделементів
            extension = '    ' if index == len(items) - 1 else '│   '
            # Рекурсивне виведення вмісту піддиректорії
            display_directory_structure(item, prefix + extension)
        else:
            # Виведення назви файлу зеленим кольором
            print(prefix + connector + Fore.GREEN + item.name + Style.RESET_ALL)

if __name__ == '__main__':
    main()