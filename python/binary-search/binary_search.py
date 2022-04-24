def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
    index = len(search_list) // 2
    stored_index = 0
    while index < len(search_list):
        if search_list[index] == value:
            return index
        if index == stored_index:
            raise ValueError("value not in array")
        if search_list[index] > value:
            index = (index + stored_index) // 2
        else:
            stored_index = index
            index = (index + len(search_list)) // 2
