def saddle_points(matrix):
    saddle_points = []
    if len(matrix) == 0:
        return saddle_points
    try:
        transposed_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    except:
        raise ValueError("irregular matrix")
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(transposed_matrix):
            if (column[row_index] == max(row)) and (column[row_index] == min(column)):
                saddle_points.append({"row": row_index + 1, "column": column_index + 1})
    return saddle_points