def hourglassSum(arr):
    grid_size = len(arr[0])
    sums = []
    for row in range(1, grid_size-1):
        for col in range(1, grid_size-1):
            sums.append(arr[row][col] + arr[row-1][col] + arr[row-1][col-1] + arr[row-1][col+1] + arr[row+1][col] + arr[row+1][col-1] + arr[row+1][col+1])
    return max(sums)

arr=[[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))