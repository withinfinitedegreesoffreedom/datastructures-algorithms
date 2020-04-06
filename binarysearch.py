# search in a sorted array

# iterative solution 

def binarysearch_iterative(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
    return -1

arr=[12, 19, 78, 105, 123, 135, 206, 569]
x=106
print(binarysearch_iterative(arr,x))

# recursive solution

def binarysearch_recursive(arr,x,low,high):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return binarysearch_recursive(arr,x,mid+1,high)
        elif arr[mid]>x:
            return binarysearch_recursive(arr,x,low,mid-1)
    else:
        return -1

arr=[12, 19, 78, 105, 123, 135, 206, 569]
x=106
print(binarysearch_recursive(arr,x,0,len(arr)-1))



