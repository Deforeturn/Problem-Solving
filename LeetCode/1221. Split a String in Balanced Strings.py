class Solution:
    def balancedStringSplit(self, s: str) -> int:
        checkArr = [0,0]
        result = 0
        for crnt in s:
            if crnt == "L":
                checkArr[0] += 1
            else:
                checkArr[1] += 1
            if checkArr[0] > 0 and checkArr[0] == checkArr[1]:
                result += 1
                checkArr[0] = 0; checkArr[1] = 0
        return result
        
