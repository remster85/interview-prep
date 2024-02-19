#!/bin/python3

import os
import heapq
import math
from io import StringIO

def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

def dijkstra(graph, start): 
    print(graph)
    # Initialize the distances 
    distances = {vertex: float('infinity') for vertex in graph} 
    distances[start] = 0
    print(distances)

    # Create a priority queue 
    priority_queue = [(0, start)] 
     
    while priority_queue: 
        # Extract the vertex with the smallest distance 
        show_tree(priority_queue)        
        current_distance, current_vertex = heapq.heappop(priority_queue) 
        print(f"popping{current_distance},{current_vertex} tab={distances}")
        print(distances)
        show_tree(priority_queue)

        
        # Check if we have found a shorter path 
        if current_distance > distances[current_vertex]: 
            print('continue')
            continue 
         
        # Update the distance of the neighbours 
        for neighbour, weight in graph[current_vertex].items(): 
            distance = current_distance + weight 
            print(f"check {neighbour} {weight} : distance = {current_distance} + {weight} = {distance} vs  neighbor {neighbour}:" + str(distances[neighbour]))
            if distance < distances[neighbour]: 
                distances[neighbour] = distance 
                print(f"pushing to queue {(distance, neighbour)} tab={distances}")
                heapq.heappush(priority_queue, (distance, neighbour)) 
                print(distances)
                show_tree(priority_queue)
                 
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

    edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]
    print(shortestReach(1, edges, 1))

