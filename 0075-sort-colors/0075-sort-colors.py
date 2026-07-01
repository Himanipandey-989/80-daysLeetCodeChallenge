class Solution:
    def sortColors(self, arr: List[int]) -> None:
        
        left=0
        right=len(arr)-1
        digit =0
        while digit<=right:
            if arr[digit]== 0:
                
                temp = arr[left]
                arr[left]=arr[digit]
                arr[digit]=temp 
                
                left=left+1
                digit = digit+1
                
            elif arr[digit] == 1:
                
                digit = digit+1
                
            else:
                
                temp = arr[digit]
                arr[digit]=arr[right]
                arr[right]=temp 
                
                right= right-1
                
                
        return arr 