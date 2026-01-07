class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)
        vis = [False] * n
        
        for i in range(n):
            if 0 < arr[i] <= n:
                vis[arr[i]-1] = True
                
        for i in range(1,n+1):
            if not vis[i-1]:
                return i
        
        return n+1        