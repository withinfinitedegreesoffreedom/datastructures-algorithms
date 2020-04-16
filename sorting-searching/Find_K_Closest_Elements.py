'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
'''

import unittest

def k_closest_elements(arr, x, k):
    if not arr:
        return None
    if x < arr[0]:
        return arr[0:k]
    if x > arr[-1]:
        return arr[len(arr)-k:]
    low, high = interval_search_bs(arr, x, 0, len(arr)-1, k)
    '''if low == high:
        if low-k-1 < 0:
            low = 0
        else:
            low = low-k-1
        if high+k-1 >= len(arr)-1:
            high = len(arr)-1
        else:
            high = high+k-1'''
    if high-low < k and high==low:
        return arr[low:low+k]
    while (high-low) > k:
        if (x-arr[low]) > (arr[high]-x):# or high>len(arr)-1:
            low=low-1
        elif abs(x-arr[low]) <= abs(x-arr[high]):# or low<0:
            high=high-1
    print(arr[low:high])

def interval_search_bs(arr, x, low, high, k):
    if low > high:
        return -1

    while (high-low) > 2*k:
        mid = (low+high)//2
        if arr[mid]==x:
            return low, high
        if x > arr[mid]:
            low = mid+1
        elif x < arr[mid]:
            high = mid-1
    return low, high

#arr = list(range(0,55,3))
#arr = [1,1,2,3,3,3,4,6,8,8]
#arr = [1,2,3,4,5]
arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
k_closest_elements(arr, x, k)


