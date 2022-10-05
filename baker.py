def cakes(recipe, ingredients):
    smallest = 1000
    for recipe_key, recipe_value in recipe.items():
        ingredients_value = ingredients.get(recipe_key)
        if ingredients_value is None:
            return 0
        ingredient_difference = ingredients_value // recipe_value
        if ingredient_difference < smallest:
            smallest = ingredient_difference

    return smallest

# cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
