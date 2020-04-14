import unittest

def sorted_merge_new_array(a, b, c):
    i, j, k = 0, 0, 0

    na, nb = len(a), len(b)

    while i < na and j < nb:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    while i < na:
        c[k] = a[i]
        i += 1
        k += 1
    while j < nb:
        c[k] = b[j]
        j += 1
        k += 1
    return c

def sorted_merge_first_array(a, b):
    i, j = 0, 0

    while i<len(a) and j<len(b):
        if b[j] > a[i]:
            i += 1
        else:
            temp = a[i:]
            a[i] = b[j]
            a[i+1:] = temp
            i += 1
            j += 1
    while j < len(b):
        a.append(b[j])
        #i += 1
        j += 1
    return a

class Test(unittest.TestCase):
    def setUp(self):
        self.a1 = [10,15,17,19,21]
        self.b1 = [16,18,20,23]
        self.a2 = [10,15]
        self.b2 = [16,18,20,23]
        self.a3 = [16,18,20,23]
        self.b3 = [10,15,17,19,21]

    def test(self):
        self.assertEqual(sorted_merge_first_array(self.a1, self.b1), [10,15,16,17,18,19,20,21,23])
        self.assertEqual(sorted_merge_first_array(self.a3, self.b3), [10,15,16,17,18,19,20,21,23])
        self.assertEqual(sorted_merge_first_array(self.a2, self.b2), [10,15,16,18,20,23])
        self.assertEqual(sorted_merge_new_array(self.a1, [11,12,13,14,22], [None]*(len(self.a1)+5)),[10,11,12,13,14,15,16,17,18,19,20,21,22,23])

if __name__=="__main__":
    unittest.main()


