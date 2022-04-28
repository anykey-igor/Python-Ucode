def search_cookbook(cookbook, recipe, section):
    if cookbook.get(recipe) is None:
        return f'There is no "{recipe}" recipe in the cookbook.'
    else:
        my_dict = cookbook.get(recipe)
    if my_dict.get(section) is not None:
        return my_dict.get(section)
    else:
        return f'There is no section "{section}" in the "{recipe}" recipe.'
