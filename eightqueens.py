
def n_ways(columns, row, results, grid_size):
    if row == grid_size:
        results.append(columns)
        return 

    for col in range(0, grid_size):
        if is_valid(columns, row, col, grid_size):
            cols_copy = columns[:]
            cols_copy[row] = col
            n_ways(cols_copy, row+1, results, grid_size)

def is_valid(columns, row, col, grid_size):
    if col in columns:
        return False

    for row2, col2 in enumerate(columns):
        if col2 is not None:
            if abs(col-col2) == abs(row-row2):
                return False
    return True

def queens(num_queens):
    grid_size = num_queens
    columns = [None]*num_queens
    row = 0
    results = []
    n_ways(columns, row, results, grid_size)
    return results

print(len(queens(8)))