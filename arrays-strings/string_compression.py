
import unittest

def string_compression(s):
    if not s:
        return None
    if len(s) < 3:
        return s

    counter = [1]
    keys = [s[0]]

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter[-1] += 1
        else:
            counter.append(1)
            keys.append(s[i])

    compressed = ""
    for i,key in enumerate(keys):
        compressed += key+str(counter[i])
    
    if len(compressed) < len(s):
        return compressed
    else:
        return s

class Test(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression('aaabbb'), 'a3b3')
        self.assertEqual(string_compression('aaaaccccbaa'), 'a4c4b1a2')
        self.assertEqual(string_compression('ababa'), 'ababa')    


if __name__=="__main__":
    unittest.main()