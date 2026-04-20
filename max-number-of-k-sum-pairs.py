class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left<right:
            result=nums[left]+nums[right]
            if result==k:
                left+=1
                right-=1
                count+=1
                
            elif result>k:
                right-=1
            else:
                left+=1
        return count


            
