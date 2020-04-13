def group_anagrams(alist):
    anagram_dict={}
    biglist=[]
    for s in alist:
        item = ''.join(sorted(s))
        if item not in anagram_dict:
            anagram_dict[item] = [s]
        else:
            anagram_dict[item].append(s)
    for keys in anagram_dict.keys():
        biglist += anagram_dict[keys]
    return biglist

alist = ['dog', 'god', 'apple', 'jym', 'ppeal', 'myg', 'abc']
print(group_anagrams(alist))