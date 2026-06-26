class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        z=0
        t=len(nums)-1
        while(i<=t):
            if nums[i]==0:
                nums[z],nums[i]=nums[i],nums[z]
                z+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[t]=nums[t],nums[i]
                t-=1
        return nums