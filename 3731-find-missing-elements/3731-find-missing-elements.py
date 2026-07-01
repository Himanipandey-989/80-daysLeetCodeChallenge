class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result=[]
        start=min(nums)
        end=max(nums)
       
        for i in range(start,end+1):
            if i not in nums:
                result.append(i)
        return result
