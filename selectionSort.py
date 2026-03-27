class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            min_index=i
            for j in range(i+1,len(arr)):
                if arr[min_index]>arr[j]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
