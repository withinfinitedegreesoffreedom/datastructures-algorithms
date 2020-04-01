
# rotate matrix by 90  
import numpy
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
b = numpy.array(a)
print(len(a))
print(b)
print(b.shape)
print(b[0,1])


N = 4

for x in range(0, int(N/2)):
    for y in range(x, N-x-1):
        temp = b[x, y]
        b[x, y] = b[y, N-1-x]
        b[y, N-1-x] = b[N-1-x, N-1-y]
        b[N-1-x, N-1-y] = b[N-1-y, x]      
        b[N-1-y, x] = temp
print(b)