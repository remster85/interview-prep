#https://leetcode.com/problems/network-delay-time
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graphs = {i : [] for i in range(1,n+1)} 
        for edge in times:
                u, v, weight = edge
                graphs[u].append((v, weight)) 
        
        distances = {i : float('inf') for i in range(1,n+1)}
        distances[k] = 0

        pq = [(k, 0)]
        
        while pq:
            u, current_duration = heapq.heappop(pq)
            
            if current_duration > distances[u]:
                continue
                
            for to, duration in graphs[u]:
                distance =  current_duration + duration
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(pq, [to, distance])
                    
        output = float('-inf')
        for k,v in distances.items():
            output = max(output, v)
        
        return -1 if output == float('inf') else output
        