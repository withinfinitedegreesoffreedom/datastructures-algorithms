def mult_by_add(m, n):
    if n == 1:
        return m
    else: 
        return m + mult_by_add(m, n-1)

print(mult_by_add(80, 5))

# doesn't work
def mult_by_add_memo(m, n, memo):
    if n == 0:
        return m
    elif memo[n-1] != -1:
        return memo[n-1]
    else:
        memo[n-1] = m + mult_by_add_memo(m, n, memo)
        return memo[n-1]

m = 80
n = 5
memo = [-1] * n
#print(mult_by_add_memo(80, 5, memo))

def getProd(a,b):
    if a < b:
        smaller = a
        bigger = b
    else:
        smaller = b
        bigger = a
    return getMul(smaller, bigger)

def getMul(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger 
    s = smaller >> 1
    halfprod = getMul(s, bigger)
    
    if smaller % 2 == 1:
        return halfprod + halfprod + bigger
    else:
        return halfprod + halfprod

print(getProd(10, 50))
    
