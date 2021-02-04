from typing import *


class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        index = 0
        while index <= N:
            if(self.isGood(index)):
                result += 1
            index += 1
            
        return result

    def isGood(self, number):
        if('3' in str(number) or '4' in str(number) or '7' in str(number)):
            return False
        elif('2' in str(number) or '5' in str(number) or '6' in str(number) or '9' in str(number)):
            return True
        


solution = Solution()
print(solution.rotatedDigits(1))
