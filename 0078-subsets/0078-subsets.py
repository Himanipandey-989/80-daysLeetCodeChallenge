class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sub(arr,start,temp):
            if start==len(arr):
                res.append(temp[:])
                return
            temp.append(arr[start])
            sub(arr,start+1,temp)
            temp.pop()
            sub(arr,start+1,temp)
        sub(nums,0,[])
        return res
        