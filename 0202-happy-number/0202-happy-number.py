"""
What is a happy number? by following the below:
    - Take squares if each digits in the number then get sum.
    - Repeat the process with the new number (result from above step).
    - Repeat until the result of the sum equals one.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def square_sum(number):
            # Helper function to get the sum if squares for digits
            total = 0
            for digit in str(number):
                total += int(digit)**2
                
            return total

        # Set to detect cycles and avoid infinite loops
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)

        
        return n == 1
