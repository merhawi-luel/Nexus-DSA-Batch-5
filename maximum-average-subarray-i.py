class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum=0
        sliding_sum=0
        for i in range(k):
            sliding_sum+=nums[i]
        left=0
        max_sum=sliding_sum

        
        for i in range(k,len(nums)):
            sliding_sum=sliding_sum+nums[i]-nums[left]
            left+=1
            if sliding_sum>max_sum:
                max_sum=sliding_sum
            
        return float(max_sum)/k
