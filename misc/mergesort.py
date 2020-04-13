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
    while i < na and j < nb:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    while i < na:
        c[k] = a[i]
        k += 1
        i += 1
    while j < nb:
        c[k] = b[j]
        k += 1
        j += 1
    return c

def mergesort(A):
    if len(A) == 0 or len(A) == 1:
        return A
    else:
        mid = len(A) // 2
        left = A[0:mid]
        right = A[mid:]
        left = mergesort(left)
        right = mergesort(right)
        mergesorted = merge(left, right, A)
        return mergesorted

A = [89, 42, 10, 6, 75, 15, 23, 0]

print(mergesort(A))