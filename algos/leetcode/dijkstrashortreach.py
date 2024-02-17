#!/bin/python3

import os
import heapq


def dijkstra(graph, start): 
    # Initialize the distances 
    distances = {vertex: float('infinity') for vertex in graph} 
    distances[start] = 0
     
    # Create a priority queue 
    priority_queue = [(0, start)] 
     
    while priority_queue: 
        # Extract the vertex with the smallest distance 
        current_distance, current_vertex = heapq.heappop(priority_queue) 
         
        # Check if we have found a shorter path 
        if current_distance > distances[current_vertex]: 
            continue 
         
        # Update the distance of the neighbours 
        for neighbour, weight in graph[current_vertex].items(): 
            distance = current_distance + weight 
            if distance < distances[neighbour]: 
                distances[neighbour] = distance 
                print(f"pushing to queue {(distance, neighbour)}")
                heapq.heappush(priority_queue, (distance, neighbour)) 
                 
    return distances 


def shortestReach(n, edges, s):

    graph = {}
    for element in edges:
        if element[0] not in graph:
            graph[element[0]] = {}
        if element[1] not in graph:
            graph[element[1]] = {}
        graph[element[0]][element[1]] = element[2]  
        graph[element[1]][element[0]] = element[2]  

    
    start_vertex = s

    res = dijkstra(graph, start_vertex)

    del res[s]
    
    output = [str(res[value]) for value  in sorted(res.keys())] 
    
    if len(output) < n-1:
        for i in range(0, n-len(output)-1):
            output += [-1]
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
