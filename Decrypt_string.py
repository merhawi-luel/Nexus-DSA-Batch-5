class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])      # take two digits before '#'
                result.append(chr(num + 96))
                i -= 3                   # skip the two digits and '#'
            else:
                num = int(s[i])          # single digit
                result.append(chr(num + 96))
                i -= 1                   # move one step left

        return ''.join(result[::-1])     # reverse because we processed from right to left
