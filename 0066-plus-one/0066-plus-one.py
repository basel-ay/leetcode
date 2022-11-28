class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits) - 1 # len of the array
        
        while digits[length] == 9: # check the last element if equal 9 to change it to 0
            digits[length] = 0
            length -= 1
        if(length < 0): # if the array have no elements
            digits = [1] + digits
        else:
            digits[length] += 1 # if none of above just increase last element
            
        return digits