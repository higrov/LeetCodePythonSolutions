class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        return haystack.find(needle)
    



sol = Solution()
haystack = "leetcode"
needle = "leeto"

print(sol.strStr(haystack,needle))