class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        
        num = x
        num_reversed = 0

        while num != 0:
            remainder = num % 10
            num_reversed = num_reversed * 10 + remainder
            num = num // 10

        if x == num_reversed:
            return True
        else:
            return False
