class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=math.floor(math.sqrt(c))
        

        while left<=right:
            result=left*left + right*right
            print(result)
            
            if c==result:
                
                return True
            elif c<result:
                right-=1
            else:
                left+=1
            
        

        

        return False 
        
