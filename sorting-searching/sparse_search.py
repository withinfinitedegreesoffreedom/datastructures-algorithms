import unittest

def sparse_search(strings, x):
    if not strings or not x:
        return -1
    return sparse_binary_search(strings, x, 0, len(strings)-1)

def sparse_binary_search(strings, x, low, high):
    if low > high:
        return -1

    mid = (low+high)//2

    if strings[mid] == " ":
        left = mid-1
        right = mid+1
        while True:
            if left < low and right > high:
                return -1
            elif strings[left] != " " and left >= low:
                mid = left
                break
            elif strings[right] != " " and right <= high:
                mid = right
                break
            left -= 1
            right += 1
    if strings[mid] == x:
        return mid
    elif x > strings[mid]:
        return sparse_binary_search(strings, x, mid+1, high)
    elif x < strings[mid]:
        return sparse_binary_search(strings, x, low, mid-1)

class Test(unittest.TestCase):
    def setUp(self):
        self.strings = ["ball", "bat", "cat"," ","chips"," ","dog","film"," "," "," ","fish"]
    
    def test(self):
        self.assertEqual(sparse_search(self.strings, "film"), 7)
        self.assertEqual(sparse_search(self.strings, "fish"), 11)
        self.assertEqual(sparse_search(self.strings, "cat"), 2)

if __name__=="__main__":
    unittest.main()

             
