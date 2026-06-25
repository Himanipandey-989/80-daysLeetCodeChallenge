class Solution:

    def search(self, nums: List[int], target: int) -> int:

            def BS(arr,start,end,target):
                left = start
                right = end

                while(left<=right):
                    mid = left + (right-left)//2 

                    if(arr[mid]==target):
                        return mid
                    elif arr[mid]<target:
                            left = mid + 1
                    else:
                            right = mid -1
                
                return -1

            def mini(arr):
                left = 0
                right = len(arr)-1
                ans = -1
                end = arr[-1]

                while(left<=right):
                    mid = left + (right-left)//2 

                    if(arr[mid]<=end):
                        ans = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                
                return ans

            p = mini(nums)

            ans1 = BS(nums,0,p-1,target)
            ans2 = BS(nums,p,len(nums)-1,target)

            if(ans1!=-1):
                return ans1
            if(ans2!=-1):
                return ans2
            
            return -1
