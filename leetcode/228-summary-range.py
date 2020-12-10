from typing import *

resuls = []
l = []


class Solution:
    def summaryRanges(self, nums: List[int], nextPick=False) -> List[str]:
        if(len(nums) == 1):
            nums.append(-1)

        if(nextPick == -1):
            return "Done"
        else:
            index = 0
            currNum = nums[index]
            nextNum = nums[index + 1]

            if(currNum+1 == nextNum):
                nums.remove(currNum)
                l.append(currNum)
                self.summaryRanges(nums, False)
            else:
                if nextPick:
                    nums.remove(currNum)
                    resuls.append(str(f"{currNum}"))
                    self.summaryRanges(nums, nextNum)
                else:
                    l.append(currNum)
                    nums.remove(currNum)
                    if(len(l) == 1):
                        resuls.append(f"{currNum}")
                    else:
                        resuls.append(f"{l[0]}->{currNum}")
                    l.clear()
                    self.summaryRanges(nums, nextNum)
        index += 1


solution = Solution()
# solution.summaryRanges([1, 2, 3, 4, 7, 8, 9, 10], False)
solution.summaryRanges([1, 2, 3, 4, 5, 7, 8, 9, 19, 20], False)

print(resuls)
