"""Let's go to a treasure hunt!
"""

def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    one_coordinate = ""
    for coordinate in combined_record_group:
        coordinate_list = list(coordinate)
        coordinate_list.remove(coordinate[1])
        one_coordinate += f"{tuple(coordinate_list)}\n" 
    return one_coordinate
