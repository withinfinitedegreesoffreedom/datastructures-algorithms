
def three_sum(nums, target):
    if nums is None:
        return []
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(0, n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        x=target-nums[i]
        start=i+1
        end=n-1
        while start<end:
            if nums[start]+nums[end]==x:
                res.append([nums[start],nums[end],nums[i]])
                start+=1
                while start>end and nums[start]==nums[start-1]:
                    start+=1
            elif nums[start]+nums[end]>x:
                end-=1
            elif nums[start]+nums[end]<x:
                start+=1
    return res


nums=[-1,0,1,2,-1,-4]
target=0
print(three_sum(nums, target))
