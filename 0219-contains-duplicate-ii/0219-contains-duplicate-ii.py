class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map={}
        for i in range(len(nums)):
            compliment=nums[i]
            if compliment in map and i-map[compliment]<=k:

                return True
            else:
                map[nums[i]]=i
        
        return False   