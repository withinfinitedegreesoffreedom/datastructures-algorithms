

def four_sum(nums, target):
    if nums is None:
        return []

    res = set()
    sum2d = {}
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            sum2 = nums[i]+nums[j]
            if sum2 in sum2d:
                sum2d[sum2].append((i,j))
            else:
                sum2d[sum2]=[(i,j)]

    for key in sum2d:
        x=target-key
        if x in sum2d:
            list1=sum2d[key]
            list2=sum2d[x]
            for (i,j) in list1:
                for (k,l) in list2:
                    if i!=k and i!=l and j!=k and j!=l:
                        candidate=[nums[i],nums[j],nums[k],nums[l]]
                        candidate.sort()
                        res.add(tuple(candidate))
    return [list(item) for item in res]

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))
