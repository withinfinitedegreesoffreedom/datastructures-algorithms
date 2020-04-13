# Find the last occurence of a number in a sorted array

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

arr=[10,10,10,10,10,10,15,20,35,35]
x=15
print(search_last_index(arr,x))
