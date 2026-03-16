class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        zeros=[]
        for i in range(len(nums)):
        
            if  i!=len(nums)-1:
               if  nums[i]==nums[i+1]:
                    nums[i]=nums[i]*2
                    nums[i+1]=0
                
            if nums[i]!=0:
                arr.append(nums[i])
            else:
                zeros.append(0)
        return arr+zeros

        

        
        
