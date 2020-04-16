class Solution:
    def findDisappearedNumbers(self, nums):
        if nums is None:
            return []
        ans=[]
        i=0
        while i<len(nums):
            if nums[i]!=i+1 and nums[nums[i]-1]!=(nums[i]-1)+1:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                #nums[i]=i+1
                i+=1
        i=0
        while i<len(nums):
            if nums[i]!=i+1:
                ans.append(i+1)
            i+=1
        return ans

nums=[4,3,2,7,8,2,3,1]
nums=[3,3,7,1,2,5,5,7]
s=Solution()
print(s.findDisappearedNumbers(nums))