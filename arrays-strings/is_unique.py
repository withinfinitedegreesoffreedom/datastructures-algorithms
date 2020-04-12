
import unittest
def is_unique_dict(s):
    unique = {}

    for char in s:
        if char in unique:
            return False
        else:
            unique[char] = 1
    return True

def is_unique_ascii(s):
    unique = [None] * 128 #128 ascii characters

    for char in s:
        index = ord(char)
        if unique[index]:
            return False
        unique[index] = True
    return True


def is_unique_no_additional_ds(s):
    pass

def is_unique_with_sort(s):
    s = sorted(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

class Test(unittest.TestCase):
    def test_isunique_dict(self):
        self.assertTrue(is_unique_dict("abcdefghij"))
        self.assertFalse(is_unique_dict("345low5"))

    def test_isunique_ascii(self):
        self.assertTrue(is_unique_ascii("abcdefghij"))
        self.assertFalse(is_unique_ascii("345low5"))

    def test_isunique_sort(self):
        self.assertTrue(is_unique_with_sort("abcdefghij"))
        self.assertFalse(is_unique_with_sort("345low5"))

    def test_isunique_noadd_ds(self):
        pass
        
if __name__=="__main__":
    unittest.main()



