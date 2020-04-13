# Find the number of rotations in a circularly sorted array
# Find the pivot element in a circularly sorted array

# assumptions - array has no duplicates 

# based on the principle of binary search 

def find_num_rotations(rotated_arr):
    low = 0
    high = len(rotated_arr)-1

    while low<=high:
        mid=(low+high)//2
        if rotated_arr[low]<=rotated_arr[high]:
            return low
        nxt=rotated_arr[mid+1]
        prev=rotated_arr[mid-1]
        if nxt>rotated_arr[mid] and prev>rotated_arr[mid]:
            return mid
        if rotated_arr[low]<=rotated_arr[mid]:
            low=mid+1
        elif rotated_arr[mid]<=rotated_arr[high]:
            high=mid-1
    return -1

rotated_arr=[11,12,20,25,35,61,-1,2,5,6,8]
print(find_num_rotations(rotated_arr))

def find_pivot_element(rotated_arr):
    low=0
    high=len(rotated_arr)-1

    while low<=high:
        mid=(low+high)//2
        if rotated_arr[low]<=rotated_arr[high]:
            return rotated_arr[low]
        nxt=rotated_arr[mid+1]
        prev=rotated_arr[mid-1]
        if rotated_arr[mid]<nxt and rotated_arr[mid]<prev:
            return rotated_arr[mid]
        if rotated_arr[mid]>=rotated_arr[low]:
            low=mid+1
        elif rotated_arr[mid]<=rotated_arr[high]:
            high=mid-1
    return None

rotated_arr=[11,12,20,25,35,61,6,8]
print(find_pivot_element(rotated_arr))


