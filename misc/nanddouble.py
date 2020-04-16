class Solution:
    def checkIfExist(self, arr):
        if arr is None:
            return
        d={}
        for i in range(0, len(arr)):
            d[arr[i]]=1
            if arr[i]//2 in d and arr[i]%2==0 and arr[i]!=0:
                return True
            if arr[i]*2 in d and arr[i]!=0:
                return True
        return False

s=Solution()
arr=[-2,0,10,-19,4,6,-8]
print(s.checkIfExist(arr))