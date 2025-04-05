class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      list_size = len(nums)

      for i in range(list_size):
        num_1 = nums[i]

        for j in range(list_size):
            if i == j: 
                continue
            num_2 = nums[j]
            final_sum = num_1 + num_2
            if final_sum == target:
                return [i,j]
        