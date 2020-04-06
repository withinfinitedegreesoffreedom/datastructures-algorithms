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

a=[10,15,20,0,5]
a=[50,5,20,30,40]
a=[15,16,19,20,25,1,3,4,5,7,10,14]
x=5
print(search(a,0,11,x))