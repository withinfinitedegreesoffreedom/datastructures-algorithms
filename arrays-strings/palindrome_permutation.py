
import unittest

def palindrome_permutation(s):
    if s ==  "":
        return False

    s_dict = {}
    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    count_odds = 0
    for key, value in s_dict.items():
        if value%2 == 1:
            count_odds += 1
            if count_odds > 1:
                return False
    return True

class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        # hash table solution
        self.assertTrue(palindrome_permutation('abcdeabcde'))
        self.assertTrue(palindrome_permutation('ddddeeeej'))
        self.assertTrue(palindrome_permutation('xyxyxyxyttu'))
        self.assertFalse(palindrome_permutation('abcdeabcdeae'))
        self.assertFalse(palindrome_permutation('aabbcdez'))
        self.assertFalse(palindrome_permutation('xyz'))

if __name__=='__main__':
    unittest.main()