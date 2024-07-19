class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False 
        
        s = s.lower()
        st2 = [c for c in s if c.isalnum()]
        clean_str = "".join(st2)
        
        i = 0
        j = len(clean_str)-1

        while i <= j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
    


sol = Solution()

string = "race a car"

print(sol.isPalindrome(string))