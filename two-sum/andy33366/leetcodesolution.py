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
            compliment = target - i

            if compliment in nums:
                answer = [i, compliment]
            #else, continue with the brute force
            else:
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        answer = [i, j]

        return answer
