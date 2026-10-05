class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        x= 0 
        for x in range(0,len(nums)):
            y= 0 
            to_be_found = target - nums[x]
            for y in range(0,len(nums)):
                if (nums[y] == to_be_found) and (x!=y):
                    array = [x,y]
                    return array
        """

        seen = {number: index for index, number in enumerate(nums)}        
        for x in range(len(nums)):
            to_find = target - nums[x]

            if ((to_find) in seen) and (x!= (seen[to_find])):
                array = [x,seen[to_find]]
                return(array)






