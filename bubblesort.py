#arr = [64, 34, 25, 12, 22, 11, 90]
arr = [7,6,5,4,3,2,1]

for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-1):
        if  arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)