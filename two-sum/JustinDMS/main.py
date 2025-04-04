class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        for i in range(size):
            for j in range(size):
                # Can't use the same element
                if i == j:
                    continue
                
                if nums[i] + nums[j] == target:
                    return [i, j]