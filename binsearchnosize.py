def binarysearch(a,x,low,high):
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            low=mid+1
        elif x<a[mid] or a[mid]==-1:
            high=mid-1
    return -1

def sortedsearch(a,x):
    index=1
    while a[index]!=-1 and x>a[index]:
        index*=2
    return binarysearch(a,x,index//2,index)

a=[0,10,20,30,40,50,60,70,80,90,100]
x=70
print(sortedsearch(a,x))