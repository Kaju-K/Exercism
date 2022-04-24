def annotate(minefield):
    for index_i, i in enumerate(minefield):
        if i == "":
            break
        if (index_i < len(minefield) - 1):
            if len(i) != (len(minefield[index_i + 1])):
                raise ValueError("The board is invalid with current input.")
        for index_j, j in enumerate(minefield[index_i]):
            if minefield[index_i][index_j] == "*":
                continue
            if minefield[index_i][index_j] != " ":
                raise ValueError("The board is invalid with current input.")
            number = 0
            for i_2 in range(-1,2):
                if index_i == 0 and i_2 == -1:
                    continue
                if index_i == (len(minefield) - 1) and i_2 == 1:
                    continue
                for j_2 in range(-1,2):
                    if index_j == 0 and j_2 == -1:
                        continue
                    if index_j == (len(minefield[0]) - 1) and j_2 == 1:
                        continue
                    if minefield[index_i + i_2][index_j + j_2] == "*":
                        number += 1
            if number != 0:
                minefield_list = list(minefield[index_i])
                minefield_list[index_j] = str(number)
                minefield[index_i] = "".join(minefield_list)
    return minefield
