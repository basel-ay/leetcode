class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Two pointers method
        left_ptr, right_ptr = 0, 1
        max_profit = 0

        # Loop until end of prices
        while right_ptr < len(prices):
            # Check if the first value less than the second value
            if prices[left_ptr] < prices[right_ptr]:
                profit = prices[right_ptr] - prices[left_ptr]
                # return the maximum value even the calculated profit or a previous profit
                max_profit = max(max_profit, profit)

            else:
                # Update the left value so the right value will be the left to move on
                left_ptr = right_ptr

            right_ptr += 1

        return max_profit