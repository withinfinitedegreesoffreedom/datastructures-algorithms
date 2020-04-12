
import unittest

def one_away(s1, s2):
    if s1 == s2:
        return True
    elif len(s1) == len(s2):
        return equal_size_check(s1, s2)
    elif abs(len(s1)-len(s2))>1:
        return False
    else:
        if len(s1) < len(s2):
            large=s2
            small=s1
        else:
            large=s1
            small=s2
        return unequal_size_check(large, small)

def equal_size_check(s1, s2):
    count_odds = False
    for i, char in enumerate(s1):
        if char != s2[i]:
            if count_odds:
                return False
            count_odds = True
    return count_odds

def unequal_size_check(large, small):
    l, s, count_missing = 0, 0, False
    while s < len(small):
        if large[l] != small[s]:
            if count_missing:
                return False
            count_missing = True
            l += 1
        else:
            l += 1
            s += 1
    return True


class Test(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('one','onef'))
        self.assertTrue(one_away('one','one'))
        self.assertTrue(one_away('one','onf'))
        self.assertTrue(one_away('on','onf'))
        self.assertTrue(one_away('','o'))
  
        self.assertFalse(one_away('one','two'))
        self.assertFalse(one_away('one','onerr'))
        self.assertFalse(one_away('blah','blabber'))

if __name__=="__main__":
    unittest.main()


