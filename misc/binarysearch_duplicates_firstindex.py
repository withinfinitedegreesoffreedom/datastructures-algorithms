# Find the first occurence of a number in a sorted array

def search_first_index(arr,x):
    low=0
    high=len(arr)-1
    result=None
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            result=mid
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
    return result

arr=[5,7,7,8,8,10]
x=8
print(search_first_index(arr,x))


