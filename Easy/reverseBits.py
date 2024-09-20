class Solution:
    def reverseBits(self, n: int) -> int:
        s = f"{n:032b}"
        rev = s[::-1]
        res = int(rev,2)
        return res
    

sol = Solution()
n = 43261596
print(sol.reverseBits(n))