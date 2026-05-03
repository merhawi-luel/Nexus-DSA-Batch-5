class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        right = 0
        my_set=set()
        
        for left in range(length):
            
            while right < length and s[right] not in my_set:
                my_set.add(s[right])
                right += 1
            
            result = max(result, right - left)
            
            my_set.remove(s[left])
        
        return result
        
