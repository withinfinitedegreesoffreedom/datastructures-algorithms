class Solution:
    def threeSumClosest(self, nums, target):
        if nums is None:
            return 
        nums.sort()
        closest_sum=None
        n=len(nums)
        for i in range(0, n):
            start=i+1
            end=n-1
            while start<end:
                s=nums[i]+nums[start]+nums[end]
                if closest_sum is None:
                    closest_sum=s
                elif abs(closest_sum-target) > abs(s-target):
                    closest_sum=s
                if s>target:
                    end-=1
                else:
                    start+=1
        return closest_sum

s=Solution()
nums=[-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums,target))