class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        number = 0  
        for char in s:
            number += roman_numerals[char]

            # if 'IV' in s or 'IX' in s:
            #     x -= 2
            # if 'XL' in s or 'XC' in s:
            #     x -= 20
            # if 'CD' in s or 'CM' in s:
            #     x -= 200

        return number
            