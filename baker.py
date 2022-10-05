def cakes(recipe, ingredients):
    flour_difference = ingredients['flour']//recipe['flour']
    sugar_difference = ingredients['sugar']//recipe['sugar']
    eggs_difference = ingredients['eggs']//recipe['eggs']

    arr = [flour_difference, sugar_difference, eggs_difference]

    smallest = 100

    for number in arr:
        if number < smallest:
            smallest = number

    return smallest


#cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})