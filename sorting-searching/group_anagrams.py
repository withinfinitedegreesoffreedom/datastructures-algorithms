import unittest

def group_anagrams(alist):
    anagrams_dict = {}
    result = []
    for s in alist:
        item = ''.join(sorted(s))
        if item not in anagrams_dict:
            anagrams_dict[item] = [s]
        else:
            anagrams_dict[item].append(s)
    for key,value in anagrams_dict.items():
        result.extend(value)
    return result

class Test(unittest.TestCase):
    def setUp(self):
        self.alist = ['dog', 'god', 'apple', 'jym', 'ppeal', 'myg', 'abc']

    def test(self):
        self.assertEqual(group_anagrams(self.alist), ['dog', 'god', 'apple', 'ppeal', 'jym', 'myg', 'abc'])

if __name__=="__main__":
    unittest.main()
        