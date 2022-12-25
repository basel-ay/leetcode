class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # rules of binary
        # 0 + 0 = 0
        # 0 + 1 = 1
        # 1 + 0 = 1
        # 1 + 1 =10
        # int(value, base [optional]) # base [optional] - the number system that the value is currently in integer representation of a number with a given base (0, 2, 8, 10, 16).
        # %s acts a placeholder for a string.
        # from binary to decimal then return in binary format again.
        sum = int("%s" % a, 2) + int("%s" % b, 2) 
        return "{0:b}".format(sum) # {0:b} just specifies that it will come out in binary format.
