def compressed_row_sparse_matrix(dense_matrix):
    values = []
    columns = []
    row_ptr = [0]

    for row in dense_matrix:
        for j, value in enumerate(row):
            if value != 0:
                values.append(value)
                columns.append(j)

        row_ptr.append(len(values))

    return values, columns, row_ptr