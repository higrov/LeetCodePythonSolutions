import re
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin = f"{n:02b}"
        res = re.sub('0', '', bin)
        return len(res)
    


sol = Solution()
n = 11
print(sol.hammingWeight(11))