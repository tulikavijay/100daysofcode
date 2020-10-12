class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequency = [0]*k
        ans = 0
        for i in range(len(arr)):
            x = arr[i]
            frequency[x % k] += 1
        for i in range(1, k//2 + 1):
            if frequency[i] != frequency[k - i]:
                return False
        return frequency[0] %2 == 0
                
                
                
            
