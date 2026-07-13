class Solution:
    def trailingZeroes(self, n: int) -> int:
        c=0
        while n!=0:
            c+=n//5
            n=n//5
        return c
                


        

        