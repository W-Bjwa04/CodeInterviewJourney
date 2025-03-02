class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create an dictionary(hashmap) to uniquely stores the keys 
        hashmap = {}

        for i in range(len(nums)):

            if(nums[i] in hashmap):
                return True

            else: 
                hashmap[nums[i]] = nums[i]
        
        return False