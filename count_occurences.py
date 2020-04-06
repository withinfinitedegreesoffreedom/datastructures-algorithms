# count the occurences of a number in sorted array

def search_first_index(arr,x):
    low=0
    high=len(arr)-1
    result=None
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            result=mid
            high=mid-1
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
    return result

def search_last_index(arr,x):
    low=0
    high=len(arr)-1
    result=None
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            result=mid
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
    return result

def count_occurences(arr,x):
    first_index = search_first_index(arr,x)
    last_index = search_last_index(arr,x)
    if first_index is None or last_index is None:
        return 1
    else:
        return (last_index-first_index+1)

arr=[10,10,10,10,10,10,15,20,35,35,35]
x=10
print(count_occurences(arr,x))