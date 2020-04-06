def merge(a,b,c):
    na = len(a)
    nb = len(b)
    nc = len(c)

    if na == 0:
        return nb

    if nb == 0:
        return na

    i = 0
    j = 0
    k = 0
    inv=0
    while i < na and j < nb:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
            inv+=na-i
        k += 1
    while i < na:
        c[k] = a[i]
        k += 1
        i += 1
    while j < nb:
        c[k] = b[j]
        k += 1
        j += 1
    return inv, c

def mergesort(A,count):
    
    if len(A) == 0 or len(A) == 1:
        return count, A
    else:
        mid = len(A) // 2
        left = A[0:mid]
        right = A[mid:]
        count, left = mergesort(left,count)
        count, right = mergesort(right,count)
        inv, mergesorted = merge(left, right, A)
        count+=inv
        return count, mergesorted

#A = [89, 42, 10, 6, 75, 15, 23, 0]
#A = [2,1,3,1,2]
#A=[1,1,1,2,2]
#A=[1,3,5,7]
#A=[3,2,1]
A=[7,5,3,1]
print(mergesort(A,0))