class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # num: index
        for i, num in enumerate(nums):
            a = target - num  # find complement
            if a in map:  # if complement exists
                return [map[a], i]  # return indices
            map[num] = i  # store num and index
