from sortedcontainers import SortedList
from heapq import heappush, heappop
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # sorted list to check free servers - add when requests run out, pop when server needed
        # heap - to keep track of busy servers
        # add when server gets busy, pop when server is available

        available = SortedList([i for i in range(k)])
        heap = []
        
        count = [0]*k
        
        for i in range(len(arrival)):
            arrivalTime, loadVal = arrival[i], load[i]   
            
            # check if any servers can be freed at this time
            while heap and heap[0][0]  <= arrivalTime:
                time, x = heappop(heap)
                available.add(x)
            
            # check for next server
            # if no available server. drop request
            
            if len(available) == 0:
                continue
                
            ind = i % k
            index = available.bisect_left(ind)
            
            if index >= len(available):
                index = available.bisect_left(0)
                
            assigned = available[index]
            
            count[assigned] += 1
            
            available.remove(assigned)
            
            heappush(heap, (loadVal + arrivalTime, assigned))
            
        
        ans = 0
        res = []
        for i in range(k):
            if ans < count[i]:
                ans = count[i]
        for i in range(k):
            if count[i] == ans:
                res.append(i)
                
        return res
