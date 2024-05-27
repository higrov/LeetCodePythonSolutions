class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        substrings = s.split(' ')
        substrings = [x for x in substrings if x != '']
        return len(substrings[-1])
    


sol = Solution()
s = "luffy is still joyboy"
print(sol.lengthOfLastWord(s))