

def powerset(s, idx, curr):
    if idx == len(s):
        print(curr)
        return
    else:
        existing_subsets = curr
        new_subsets = []
        for item in existing_subsets:
            new_subsets.append(item+s[idx])
        curr.extend(new_subsets)
        powerset(s, idx+1, curr)
        

s = "a"
idx = 0
curr = ['']
powerset(s, idx, curr)