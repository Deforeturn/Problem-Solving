class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        for i in range(len(nums)):
            if target == nums[i]:
                result = i
                break
        return result
