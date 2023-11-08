def search_replace(my_list, search, replace):
    return [replace if char == search else char for char in my_list]
