"""

The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted. Therefore, we can sort the array and return the element at index n/2.

"""

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return nums[len(nums) // 2]
    

"""

The intuition behind using a hash map is to count the occurrences of each element in the array and then identify the element that occurs more than n/2 times. By storing the counts in a hash map, we can efficiently keep track of the occurrences of each element.

"""    

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a defaultdict with default value 0
        m = defaultdict(int)
        # For each element nums[i], it increments its count in the hash map m by using the line m[nums[i]]++
        
        #    1) If nums[i] is encountered for the first time, it will be added to the hash map with a count of 
        #    2) If nums[i] has been encountered before, its count in the hash map will be incremented by 1.
        for num in nums:
            m[num] += 1
    
        for key, value in m.items():
            if value > len(nums) // 2:
                return key
    
    