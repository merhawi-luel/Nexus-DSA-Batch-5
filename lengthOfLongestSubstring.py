class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        for _, i in enumerate(s):
            map = {}
            map[i] = 1
            count = 1
            for j in s[_+1:]:
                if j in map:
                    break
                map[j] = 1
                count += 1
            if count > max_count:
                max_count = count

        return max_count
