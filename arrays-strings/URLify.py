import unittest

def URLify(s):
    s_copy = s
    s_copy = s_copy.split(' ')
    return '%20'.join(s_copy)

class Test(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual(URLify("hello world"), "hello%20world")
        self.assertEqual(URLify("helloworld"), "helloworld")

if __name__=="__main__":
    unittest.main()