class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return
        i=0
        while i<len(arr):
            if arr[i]==0:
                arr=arr[0:i+1]+[0]+arr[i+1:len(arr)-1]
                i+=2
            else:
                i+=1
        return arr
    
    def _duplicateZeros(self, arr):
        if not arr:
            return
        i=0
        while i<len(arr):
            if arr[i]==0:
                for j in range(len(arr)-2,i,-1):
                    arr[j+1]=arr[j]
                arr[i+1]=0
                i+=2
            else:
                i+=1
        return  arr

s=Solution()
arr=[1,0,2,3,0,4,5,0]
print(s._duplicateZeros(arr))