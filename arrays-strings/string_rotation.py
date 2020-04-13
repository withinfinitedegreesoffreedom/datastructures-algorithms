import unittest

def string_rotation(s1, s2):
    if len(s1) == len(s2):
        if is_substring(s1+s1, s2):
            return True
    return False

def is_substring(s1, s2):
    return s2 in s1

class Test(unittest.TestCase):
    def test_string_rotation(self):
        self.s1 = "waterbottle"
        self.s2 = "bottlewater"
        self.assertTrue(string_rotation(self.s1, self.s2))

if __name__=="__main__":
    unittest.main()