class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        
        if n<2:
            return -1
        
        current_max = current_second_max = float('-inf')
        
        for num in arr:
            if num > current_max:
                current_second_max = current_max
                current_max = num
            elif num > current_second_max and num != current_max:
                current_second_max = num
            
        if current_second_max == float('-inf'):
            return -1 
        else:
            return current_second_max