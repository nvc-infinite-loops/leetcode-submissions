class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #solution is different for negative or positive target?
        #Didn't finish it sorry :,(

        #sort nums into pozz/neg and > or < target

        #sorts target as pozz or neg, bool is set as true if pozz or 0
        pozz = (target >= 0)

        # if target is pozz
        if pozz:

            nums_poz_lt_target = {}
            nums_neg = {}
            nums_poz_gt_target = {}

            #sorts nums into dictionary {<num>:<index>}
            for i in nums:
                if i < 0:
                    #add num and index to nums_neg dictionary
                    nums_neg[i] = nums.index(i)
                elif i < target:
                    nums_poz_lt_target[i] = nums.index(i)
                else:
                    nums_poz_gt_target[i] = nums.index(i)

            #check if there are negative numbers
            if not nums_neg:
                for (i = 0, i < len(nums_poz_lt_target), i += 1):
                    for (j = 0, i < len())




            #nums are both pozz < target

            #or

            #one num is pozz > target, the other num is neg

        # if target is neg
        else:
            #nums are both neg > target

            #or

            #one num is pozz > target, the other is neg < target

        #once sorted -->> bruteforce??

        #positive target

target = 8
nums = [6, 5, 2, 9]
test = Solution()
test.twoSum(nums, target)
