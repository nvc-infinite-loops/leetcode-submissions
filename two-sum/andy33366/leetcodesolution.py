class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []


        for i in range(len(nums)):

            #if complement is in the list, skips the rest
            compliment = target - nums[i]
            if ((compliment in nums) and (compliment != nums[i])):
                answer = [i, nums.index(compliment)]
                break

            #else, continue with the brute force
            else:
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        answer = [i, j]

        return answer

