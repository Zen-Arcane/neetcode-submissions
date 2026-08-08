class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            s = target - v

            if s in seen:
                return [seen[s], i]

            seen[v] = i