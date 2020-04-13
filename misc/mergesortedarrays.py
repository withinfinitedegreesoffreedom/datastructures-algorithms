def merge_sorted(A, B):
    i = 0
    j = 0
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i+=1
        else:
            A.insert(i, B[j])
            i+=1
            j+=1
    while j < len(B):
        A.insert(i,B[j])
        i+=1
        j+=1
    return A

B=[10,15,20,25,100]
A=[17,23,27,29,30,45]
print(merge_sorted(A,B))