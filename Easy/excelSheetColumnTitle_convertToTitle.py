class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        f = lambda columnNumber: "" if columnNumber==0 else self.convertToTitle((columnNumber-1)//26)+chr((columnNumber-1)%26+ord("A"))

        return  f(columnNumber)


sol = Solution()

print(sol.convertToTitle(2147483647))