
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) == 0:
        return 0
    if len(c) == 1 and c[0] == 1:
        return 0
    i = 0
    jumps = []
    while i < len(c):
        if c[i] == 0:
            jumps.append(i)
            if i+2 < len(c):
                i += 2
            else:
                i += 1
        else:
            jumps.append(i-1)
            i += 1
    return len(jumps)-1

c = [0, 0, 0, 1, 0, 0]
c1 = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))
print(jumpingOnClouds(c1))
