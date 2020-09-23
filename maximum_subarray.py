class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #local maxima
        curr = nums[0]
        #global maxima
        max_val = nums[0]
        n = len(nums)
        for i in range(1,n):
            curr = max(nums[i], curr + nums[i])
            max_val = max(curr, max_val)
        return max_val
    
        
        
