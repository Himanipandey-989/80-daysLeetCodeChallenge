class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fre=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                fre.append(abs(nums[i]))
            else:
                nums[index]=-nums[index]
        return fre
        