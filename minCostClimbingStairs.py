class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        # either climb one step or two steps
        # either go for i+1 or i+2 from any i
        # minimize cost
        arr = [0]*N
        arr[0] = cost[0]
        arr[1] = cost[1]
        for i in range(2,N):
            if arr[i-1] + cost[i] < arr[i-2] + cost[i]:
                arr[i] = arr[i-1] + cost[i]
            else:
                arr[i] = arr[i-2] + cost[i]
        return min(arr[-1],arr[-2])

