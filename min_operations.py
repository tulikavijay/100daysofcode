class Solution:
    def minOperations(self, n: int) -> int:
        start = 1
        end = (2*(n-1)) + 1
        toequal = (start + end)//2
        ans = 0
        while end > toequal:
            ans += end - toequal
            end -= 2
        return ans
            
        
        
