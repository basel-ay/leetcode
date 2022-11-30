class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1

        # step 1: find the decreasing number
        while i > 0 and nums[i] <= nums[i-1]:
            i-=1

        # if arrangement is not possible
        if i == 0:   
            nums.reverse()
            return 
        # step 2: find higher than the decreasing number then replace them
        k = i - 1 # the decreasing number

        while nums[k] >= nums[j]:
            j-=1
        nums[k], nums[j] = nums[j], nums[k] # replace the two numbers

        # step 3: rearrange rest of numbers
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1
