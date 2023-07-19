def print_cookbook(book):
    print()
    for dish_name, dish_ingredients in book.items():
        print(dish_name + ':')
        for ingredient_properties in dish_ingredients:
            print(ingredient_properties['ingredient_name'], '|', ingredient_properties['quantity'], '|', ingredient_properties['measure'])
        print()
# Метод для вывода кулинарной книги, не влияет на алгоритм программы, добавил исключительно в целях повышения удобства/читабельности/красоты

# Функция задания номер 1
def get_dish_fromfile(file_name, book):
    dish_title = ""
    dish_ingredients_list = []
    ingredient_properties_list = []
    dish_title = file1.readline().strip()
    i_len = int(file1.readline())
    while i_len > 0:
        i_len -= 1
        ingredient_properties_dict = {}
        ingredient_properties_list = file1.readline().strip().split('|')
        ingredient_properties_dict['ingredient_name'] = ingredient_properties_list[0]
        ingredient_properties_dict['quantity'] = int(ingredient_properties_list[1])
        ingredient_properties_dict['measure'] = ingredient_properties_list[2]
        dish_ingredients_list.append(ingredient_properties_dict)
    book[dish_title] = dish_ingredients_list
# Читает по одному рецепту за раз и зацикливается в основном коде, есть ли смысл зацикливать внутри этой/отдельной функции или оставить исполнение как есть?

# Функция задания номер 2
def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        for dish_name, dish_ingredients in cook_book.items():
            if dish_name == dish:
                for ingredient_properties in dish_ingredients:
                    shopping_list[ingredient_properties['ingredient_name']] = {}
                    shopping_list[ingredient_properties['ingredient_name']]['measure'] = ingredient_properties['measure']
                    shopping_list[ingredient_properties['ingredient_name']]['quantity'] = 0
                    shopping_list[ingredient_properties['ingredient_name']]['quantity'] += (ingredient_properties['quantity'])*person_count
                    # Альтернативный вариант умножения на person_count-пройти циклом по словарю в самом конце функции и умножить quantity каждого ингредиента
                    # Примененный мной метод менее эффективен по времени при возрастании количества блюд, но уменьшает количество кода
                    # Другой вариант реализации умножения будет приведен в комментариях в конце функции
    for key, value in shopping_list.items():
        # Альтернативная реализация умножения:
        # output_dict[key][quantity] *= person_count
        print(key + ': ', shopping_list[key])



cook_book = {}

# В данном цикле выполняется задание 1
with open("recipes.txt", "r", encoding='utf-8') as file1:
    s = '1'
    while s != '':
        # Вызов функции задания 1
        get_dish_fromfile(file1, cook_book)
        s = file1.readline()

print_cookbook(cook_book)
# Вызов функции задания 2
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Формат вывода верный, но порядок ингредиентов неверный. Считается ли это за ошибку?
print("Формат вывода верный, но порядок ингредиентов неверный. Считается ли это за ошибку?")
