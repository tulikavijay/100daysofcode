class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        d = {0:0}
        for ind, val in enumerate(nums,1):
            if val == 0:
                count -= 1
            else:
                count += 1
            if count in d:
                ans = max(ans, ind - d[count] )
            else:
                d[count] = ind
        return ans
                
                    
