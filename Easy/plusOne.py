from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        s = ''.join(s)
        num = int(s)
        res = num +1
        num2 = list(map(int, str(res)))

        return num2
    

sol = Solution()
digits= [1,2,3]
print(sol.plusOne(digits))