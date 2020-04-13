#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
'''def activityNotifications(expenditure, d):
    n = len(expenditure)
    if n==d or d>n:
        return 0
    notifications=0
    ex=expenditure[0:d]
    ex.sort()
    for i in range(d, n):
        new_ex=expenditure[i]
        if new_ex>ex[-1]:
            ex.append(new_ex)
        elif new_ex<ex[0]:
            ex=[new_ex].extend(ex[:])
        else:
            for j in range(0, len(ex)-1):
                if (ex[j]==new_ex) or (ex[j]>new_ex and ex[j+1]<new_ex):
                    l=ex[0:j]
                    l.append(new_ex)
                    l.extend(ex[j+1:])
                    ex=l
                    break
        mid=(len(ex)-1)//2
        if i%2==0:       
            median=(ex[mid]+ex[mid+1])/2
        else:
            median=ex[mid]
        if new_ex>=2*median:
            notifications+=1
    return notifications'''

def activityNotifications(expenditure, d):
    n = len(expenditure)
    if n==d or d>n:
        return 0
    notifications=0
    med_ind=d//2
    for i in range(d, n):
        ex=expenditure[i-d:i]
        ex.sort()
        if d%2==0:
            med=(ex[med_ind]+ex[med_ind-1])/2
        else:
            med=ex[med_ind]
        if expenditure[i]>=2*med:
            notifications+=1
    return notifications


expenditure=[2, 3, 4, 2, 3, 6, 8, 4, 5]
d=5
print(activityNotifications(expenditure,d))