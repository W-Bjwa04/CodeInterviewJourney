class Solution(object):
    def twoSum(self, nums, target):
       
       #create a dictionery to serve the purpose of hashmap

        hashmap = dict()

        for i in  range(len(nums)):
            
            
            remainder = target - nums[i]

            # check if the remainder exits in the hahmap or not

            if (remainder in  hashmap):
                return [hashmap.get(remainder),i]
            
            # else add the current number in the hashmap 
            hashmap[nums[i]] = i

        return []

