class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i <= (x//2):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
            i += 1
        return -1
    

sol = Solution()

print(sol.mySqrt(100))