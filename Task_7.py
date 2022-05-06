def zip_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding="utf-8") as file:
        for line in file:
            key = line.strip()
            num_ingr = int(file.readline().strip())
            all_ingredients = []
            for ingr in range(num_ingr):
                ingredient = file.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                all_ingredients.append(ingredients)
            cook_book[key] = all_ingredients
            file.readline()
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    with open('recipes.txt', 'r', encoding="utf-8") as file:
        for line in file:
            key = line.strip()
            num_ingr = int(file.readline().strip())
            for ingr in range(num_ingr):
                ingredient = file.readline().strip().split(' | ')
                if key in dishes:
                    ingredients = {'measure': ingredient[2], 'quantity': int(ingredient[1]) * int(person_count)}
                    shop_list[ingredient[0]] = ingredients
            file.readline()
    print(shop_list)


zip_cook_book()
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
