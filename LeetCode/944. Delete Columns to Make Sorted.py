from typing import List
class Solution:
    def minDeletionSize(self,strs: List[str]) -> int:
        result = 0
        for i in range(0, len(strs[0])):
            for j in range(0, len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    result += 1
                    break
        return result
