class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if "(" not in input_string:
        raise ValueError("tree missing")
    if input_string == "()":
        raise ValueError("tree with no nodes")
    storage = {}
    brackets = False
    ignore = False
    key_storage = ""
    things_for_values = ""
    value_storage = []
    child = False
    child_storage = {}
    children_key_storage = ""
    things_for_children_values = ""
    children_value_storage = []
    child_list = []
    for index, character in enumerate(input_string):
        if character in "();":
            continue
        if character == "\\":
            ignore = True
            continue
        if character == "[" and ignore == False:
            brackets = True
            continue
        if character == "]" and input_string[index+1] != "[" and ignore == False:
            if children_key_storage != "":
                if children_value_storage[-1].isupper():
                    child = True
                else:
                    child = False
                child_storage[children_key_storage] = children_value_storage
                children_key_storage = ""
                children_value_storage = []
                child_list.append(SgfTree(child_storage))
                child_storage = {}
            if key_storage != "":
                if value_storage[-1].isupper():
                    child = True
                storage[key_storage] = value_storage
                key_storage = ""
                value_storage = []
            brackets = False
            continue
        if character == "]" and ignore == False:
            continue
        if child == False:
            if brackets == False:
                if character.islower():
                    raise ValueError("property must be in uppercase")
                key_storage += character
            else:
                if character == "\t":
                    things_for_values += " "    
                else:
                    things_for_values += character
                if input_string[index+1] == "]":
                    value_storage.append(things_for_values)
                    things_for_values = ""
        else:
            if brackets == False:
                if character.islower():
                    raise ValueError("property must be in uppercase")
                children_key_storage += character
            else:
                if character == "\t":
                    things_for_children_values += " "    
                else:
                    things_for_children_values += character
                if input_string[index+1] == "]":
                    children_value_storage.append(things_for_children_values)
                    things_for_children_values = ""
        if input_string[index-1] == "\\":
            ignore = False
    if key_storage != "":
        raise ValueError("properties without delimiter")
    return SgfTree(properties=storage, children=child_list)
