def minimumSwaps(arr):
    if len(arr)==0 or len(arr)==1:
        return 0
    swaps = 0
    i = 0
    while i<len(arr)-1:
        if arr[i]!=i+1:
            tmp=arr[i]
            arr[i],arr[tmp-1]=arr[tmp-1],arr[i]
            swaps+=1
        else:
            i+=1
    return swaps


arr=[4,3,1,2]
print(minimumSwaps(arr))