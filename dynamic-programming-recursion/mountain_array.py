class Solution:
    def validMountainArray(self, nums):
        if not nums:
            return 
        i=1
        seen_mountain=False
        while i<len(nums):
            if nums[i]>nums[i-1]:
                i+=1
                seen_mountain=True
            else:
                break
        if i==1 and seen_mountain==False:
            return False
        i+=1
        seen_valley=False
        while i<len(nums):
            if nums[i]<nums[i-1]:
                i+=1
                seen_valley=True
            else:
                break
        if seen_valley==False:
            return False
        return seen_mountain and seen_valley

s=Solution()
arr=[0,2,3,3,5,2,1,0]
print(s.validMountainArray(arr))