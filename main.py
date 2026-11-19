import pprint
import os


def parse_ingredient(ingredient_line: str) -> dict:
    """
    Разбирает строку с ингредиентом и возвращает словарь.
    """
    name, quantity, measure = [item.strip() for item in ingredient_line.split('|')]

    return {
        'ingredient_name': name,
        'quantity': int(quantity),
        'measure': measure
    }


def get_cook_book(file_path: str) -> dict:
    """
    Читает файл с рецептами и формирует словарь cook_book.
    """
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        dish_name = lines[i]
        ingredients_count = int(lines[i + 1])

        ingredients_list = []
        for j in range(ingredients_count):
            ingredient_line = lines[i + 2 + j]
            ingredients_list.append(parse_ingredient(ingredient_line))

        cook_book[dish_name] = ingredients_list
        i += 2 + ingredients_count

    return cook_book
#1
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    """
    Формирует список покупок для заданных блюд на указанное количество персон.
    """
    cook_book = get_cook_book('recipes.txt')
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f"Предупреждение: блюдо '{dish}' не найдено в книге рецептов.")
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity
                }

    return shop_list


def read_file_info(file_path: str) -> tuple:
    """
    Читает файл и возвращает информацию о нем: (имя_файла, количество_строк, содержимое).
    """
    file_name = os.path.basename(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines_count = len(lines)
    content = ''.join(lines)

    return file_name, lines_count, content


def process_files(file_list: list) -> list:
    """
    Обрабатывает список файлов: читает их и сортирует по количеству строк.
    """
    files_info = []

    for file_path in file_list:
        file_info = read_file_info(file_path)
        files_info.append(file_info)

    # Сортируем по количеству строк (второй элемент кортежа)
    files_info.sort(key=lambda x: x[1])

    return files_info


def write_result_file(files_info: list, output_file: str) -> None:
    """
    Записывает отсортированные файлы в результирующий файл с служебной информацией.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for file_name, lines_count, content in files_info:
            # Записываем служебную информацию
            file.write(f'{file_name}\n')
            file.write(f'{lines_count}\n')
            # Записываем содержимое файла
            file.write(content)


def main():
    """
    Точка входа в программу.
    """
    # === Задача №1 ===
    print("=== Задача №1 ===")
    cook_book = get_cook_book('recipes.txt')
    pprint.pprint(cook_book, sort_dicts=False, width=100)

    # === Задача №2 ===
    print("\n=== Задача №2 ===")
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    pprint.pprint(shop_list, sort_dicts=False, width=100)

    # === Задача №3 ===
    print("\n=== Задача №3 ===")
    # Список файлов для обработки (замените на реальные имена файлов)
    files_to_process = ['1.txt', '2.txt']
    output_file = 'result.txt'

    # Обрабатываем и сортируем файлы
    files_info = process_files(files_to_process)

    # Записываем результат
    write_result_file(files_info, output_file)

    print(f"Файлы успешно объединены в '{output_file}'")
    print("Отсортированы по количеству строк (по возрастанию)")


if __name__ == '__main__':
    main()