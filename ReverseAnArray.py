class Solution:
    def reverseArray(self, arr):
        # code here
        first = 0
        last = len(arr)-1
        
        while first < last:
            arr[first], arr[last] = arr[last], arr[first]
            first += 1
            last -= 1
        
        