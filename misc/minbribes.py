def minimumBribes(q):
    if len(q) == 0:
        return 0
    if len(q) == 1:
        return 0
    n = len(q)
    swaps = 0
    swaped = False
    for i in range(0, n):
        if q[i] > i+1 and q[i]-1-i > 2:
            return "Too chaotic"

    for i in range(0, n-1):
        for j in range(0, n-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps+=1
                swaped=True
        if swaped:
            swaped=False
        else:
            break
    return swaps


        
q = [1, 2, 5,3,7,8,6,4]
print(minimumBribes(q))

'''if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(type(q))

        print(q)

        print(minimumBribes(q))'''

