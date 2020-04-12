import unittest

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_dict = {}
    s2_dict = {}

    for char in s1:
        if char in s1_dict:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1

    for char in s2:
        if char in s2_dict:
            s2_dict[char] += 1
        else:
            s2_dict[char] = 1

    for key, value in s1_dict.items():
        if key not in s2_dict or value != s2_dict[key]:
            return False

    return True

class Test(unittest.TestCase):
    def test_check_permutation(self):
        self.assertTrue(check_permutation("god", "dog"))
        self.assertFalse(check_permutation("abcdefgh", "abcdefgk"))

if __name__=="__main__":
    unittest.main()

