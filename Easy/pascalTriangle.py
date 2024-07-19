from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        first_row = [1]
        result.append(first_row)
        for i in range(1,numRows):
            previous_row = result[i-1]
            print(previous_row)
            current_row = [1]

            for j in range(1,i):
                print(previous_row[j])
                current_row.append(previous_row[j-1]+previous_row[j])
            
            current_row.append(1)
            result.append(current_row)

        return result

sol = Solution()

numRows = 5

print(sol.generate(numRows))
