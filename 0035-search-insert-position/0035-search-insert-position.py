class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # must write an algorithm with "O(log n)" runtime complexity => binary search
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2 # integer
            guess = nums[mid]
            
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1 
                
        # If not found, return the index where it would be if it were inserted in order.
        return low 
        
