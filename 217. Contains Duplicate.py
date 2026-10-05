class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = set(nums)
        if len(hash_set) != len(nums):
            return True

        return False

        