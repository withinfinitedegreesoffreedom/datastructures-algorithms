import unittest

def binary_search_no_size(a, x):
    return find_len_binary_search(a, x)

def find_len_binary_search(a, x):
    ind = 1
    while elementAt(a, ind)!=-1 and x>a[ind]:
        ind*=2
    return binary_search(a, x, ind//2, ind)

def elementAt(a, ind):
    if ind > len(a):
        return -1
    else:
        return a[ind]

def binary_search(a, x, low, high):
    if low>high:
        return -1

    mid = (low+high)//2

    if a[mid]==x:
        return mid
    elif a[mid] == -1:
        return binary_search(a, x, low, mid-1)
    elif x > a[mid]:
        return binary_search(a, x, mid+1, high)
    elif x < a[mid]:
        return binary_search(a, x, low, mid-1)

class Test(unittest.TestCase):
    def setUp(self):
        self.a = [0,5,10,15,20,25,30,35,40,50,70,90,100]
        
    def test(self):
        self.assertEqual(binary_search_no_size(self.a, 70), 10)
        self.assertEqual(binary_search_no_size(self.a, 5), 1)

if __name__=="__main__":
    unittest.main()
