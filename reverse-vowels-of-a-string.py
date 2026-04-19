class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=["a","e","i","o","u","A","E","I","O","U"]
        str1=list(s)
        left,right=0,len(s)-1
        while left < right: #IceCream
            if str1[left] in arr and str1[right]in arr:
                str1[left],str1[right]=str1[right],str1[left]
                left+=1
                right-=1
            elif str1[right] in arr:
                left+=1
            elif str1[left] in arr:
                right-=1
            else:
                right-=1
                left+=1
        return "".join(str1)
            

