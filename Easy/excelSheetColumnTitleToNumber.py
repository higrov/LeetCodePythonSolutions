class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        list_title= list(columnTitle)

        multiplier = 1
        res = 0
        while list_title:
            char = list_title.pop()

            place = ord(char) - ord('A') + 1
            res += place * multiplier

            multiplier *= 26
        
        return res
    



sol = Solution()
# print((2147483647 // 26)%26)

# z  y  x  w
# 26 25 24 23
print(sol.titleToNumber('FXSHRXW'))

