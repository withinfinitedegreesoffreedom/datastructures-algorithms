# Search in rotated sorted - recursive

def search(a,left,right,x):
    mid=(left+right)//2
    if a[mid]==x:
        return mid
    if right<left:
        return -1
    #find which part if ordered
    if a[left]<a[mid]: #--> left ordered
        if x>=a[left] and x<a[mid]:
            return search(a,left,mid-1,x)
        else:
            return search(a,mid+1,right,x)
    elif a[left]>a[mid]: #--> right ordered
        if x>a[mid] and x<=a[right]:
            return search(a,mid+1,right,x)
        else:
            return search(a,left,mid-1,x)
    elif a[mid]==a[left]:
        if a[mid]!=a[right]:
            return search(a,mid+1,right,x)
        else:
            result = search(a,left,mid-1,x)
            if result==-1:
                return search(a,mid+1,right,x)
            else:
                return result


# Search in rotated sorted array - iterative 

def _search(arr, x):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<=arr[high]:
            if x>arr[mid] and x<=arr[high]:
                low=mid+1
            else:
                high=mid-1
        elif arr[low]<=arr[mid]:
            if x>=arr[low] and x<arr[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1


a=[10,15,20,0,5]
a=[50,5,20,30,40]
a=[15,16,19,20,25,1,3,4,5,7,10,14]
x=15
print(search(a,0,11,x))
print(_search(a,x))