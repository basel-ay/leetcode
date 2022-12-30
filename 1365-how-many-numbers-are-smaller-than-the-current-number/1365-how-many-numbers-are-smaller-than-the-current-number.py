class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nested loop
        sum_numbers = 0
        output_list = []

        for i in nums:
            for j in nums:
                if i > j:
                    sum_numbers += 1

            output_list.append(sum_numbers)
            sum_numbers = 0

        return output_list
        
        # by index
        # dct = {}
        # for i, n in enumerate(sorted(nums)):
        #     if n not in dct:
        #         dct[n] = i
        # return [dct[n] for n in nums]