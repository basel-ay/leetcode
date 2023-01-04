class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_representation_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        # remove '1' that does not map to any letters.
        digits = digits.replace('1', '')

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(digits_representation_dic[digits[0]])  # ['a', 'b', 'c']

        # get list representation of every digit except the last one
        prev = self.letterCombinations(digits[:-1])
        additional = digits_representation_dic[digits[-1]]

        # concatenate
        return [s + c for s in prev for c in additional]

        # return list(map(''.join, itertools.product(*map(digits_representation_dic.__getitem__, digits)))) if digits else ''
