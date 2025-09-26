from typing import List, Tuple

import bisect
class Solution:
    def countFairPairs(self, nums:List[int], lower:int, upper:int)-> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = bisect.bisect_left(nums, lower-nums[i], 0, i)
            right = bisect.bisect_right(nums, upper-nums[i], 0, i)
            
            res += right - left
        return res
    

def _run_code() -> None:
    solver = Solution()
    tests: List[Tuple[List[int], int, int, int]] = [
        [[0,1,7,4,4,5], 3, 6, 6],
        [[1,7,9,2,5], 11, 11, 1]
    ]
    for cnt, (nums, lower, upper, expected) in enumerate(tests):
        res = solver.countFairPairs(nums, lower, upper)
        print(f"Result of Test #{cnt + 1}: {res}, Expected: {expected}")
        if res != expected:
            print(f"################## Test {cnt+1} Failed ##################")
        
        
if __name__ == "__main__":
    _run_code()