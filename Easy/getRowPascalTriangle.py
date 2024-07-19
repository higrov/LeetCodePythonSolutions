from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = []
        first_row = [1]
        if rowIndex == 0:
            return first_row
        result.append(first_row)
        for i in range(1,rowIndex+1):
            previous_row = result[i-1]
            current_row = [1]

            for j in range(1,i):
                current_row.append(previous_row[j-1]+previous_row[j])
            
            current_row.append(1)
            result.append(current_row)

        return result[rowIndex]


    

sol = Solution()

numRows = 3

print(sol.getRow(numRows))