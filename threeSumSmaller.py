class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        i, j, k = 0, 1, 2
        n = len(nums)
        ans = 0
        nums = sorted(nums)
        for k in range(2, n):
            i = 0
            j = k-1
            while i < j :
                if nums[i] + nums[j] + nums[k] < target:
                    ans += j -i
                    i += 1
                else:
                    j -= 1
                    
        return ans
                    
        
        
