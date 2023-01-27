class Solution(object):
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Initialize triangle with all 1
        output = [[1]*i for i in range(1, num_rows+1)]
        
        for i in range(1, num_rows):
            for j in range(1, i):
                # update each as sum of two elements from above row
                output[i][j] = output[i-1][j] + output[i-1][j-1]   

        return output