def cakes(recipe, ingredients):
    smallest = ingredients.items()[0].value #figure this out next time!
    for recipe_key, recipe_value in recipe.items():
        ingredients_value = ingredients.get(recipe_key)
        if ingredients_value is None:
            return 0
        ingredient_difference = ingredients_value // recipe_value
        if ingredient_difference < smallest:
            smallest = ingredient_difference

    return smallest


