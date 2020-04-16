import unittest

def search_in_rotated_array(array,x):
    if not array:
        return None

    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low+high)//2
        if array[mid] == x:
            return mid
        elif array[mid+1] <= array[high]:
            if x >= array[mid+1] and x <= array[high]:
                low = mid+1
            else:
                high = mid-1
        elif array[low] <= array[mid-1]:
            if x >= array[low] and x <= array[mid-1]:
                high = mid-1
            else:
                low = mid+1
    return -1

def search_in_rotated_sorted_array_leetcode(array, x):
    if array is None:
        return -1

    if len(array)==1:
        if array[0]==x:
            return 0
        else:
            return -1

    low=0
    high=len(array)-1

    while low<=high:
        mid=(low+high)//2
        if array[mid]==x:
            return mid
        elif array[mid]<array[high]:
            if x>array[mid] and x<=array[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if x>=array[low] and x<array[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1


def search_in_rotated_array_recursive(array, low, high, x):
    mid = (low+high)//2
    
    if array[mid] == x:
        return mid
    if low > high:
        return -1

    if array[low] <= array[mid-1]:
        if x >= array[low] and x <= array[mid-1]:
            return search_in_rotated_array_recursive(array, low, mid-1, x)
        else:
            return search_in_rotated_array_recursive(array, mid+1, high, x)
    elif array[mid+1] <= array[high]:
        if x >= array[mid+1] and x<=array[high]:
            return search_in_rotated_array_recursive(array, mid+1, high, x)
        else:
            return search_in_rotated_array_recursive(array, low, mid-1, x)
    elif array[mid] == array[low]: # left is just repeats
        if array[mid] != array[high]:
            return search_in_rotated_array_recursive(array, mid+1, high, x)
        else:
            result = search_in_rotated_array_recursive(array, low, mid-1, x)
            if result == -1:
                return search_in_rotated_array_recursive(array, mid+1, high, x)
            else:
                return result


class Test(unittest.TestCase):
    def setUp(self):
        self.array = [11,12,13,14,15,1,4,5,7,10]
        self.array1  = [15,16,19,20,25,1,3,4,5,7,10,14]

    def test(self):
        self.assertEqual(search_in_rotated_array(self.array, 8),-1)
        self.assertEqual(search_in_rotated_array(self.array, 1),5)
        self.assertEqual(search_in_rotated_array(self.array, 10),9)
        self.assertEqual(search_in_rotated_array(self.array1, 5),8)
        self.assertEqual(search_in_rotated_array_recursive(self.array, 0, len(self.array)-1, 8),-1)
        self.assertEqual(search_in_rotated_array_recursive(self.array, 0, len(self.array)-1, 1),5)
        self.assertEqual(search_in_rotated_array_recursive(self.array, 0, len(self.array)-1, 10),9)
        self.assertEqual(search_in_rotated_array_recursive(self.array1, 0, len(self.array)-1, 5),8)
        self.assertEqual(search_in_rotated_array_recursive([3,4,5,6,1,2],0, 5, 2),5) # leetcode
        self.assertEqual(search_in_rotated_array([4,5,6,7,0,1,2], 0),4) #leetcode

if __name__=="__main__":
    unittest.main()



