#https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True
        
        visited = { i : 0 for i in range(0, numCourses)}
        courseMap = {}
        
        for prerequisite in prerequisites:
            if prerequisite[1] not in courseMap:
                courseMap[prerequisite[1]] = []
            courseMap[prerequisite[1]].append(prerequisite[0])
            
        
        print(courseMap)
        
        
        def dfs(value):

            if not value in courseMap:
                visited[value] = 2
                return True
            
            if visited[value] == 1:
                return False
            
            if visited[value] == 2:
                return True
            
            visited[value] = 1
                
            for pres in courseMap[value]:
                if not dfs(pres):
                    return False

            visited[value] = 2
                
            return True
        
        
                
        for value in range(0, numCourses):                
            if not dfs(value):
                return False
                
        for value in range(0, numCourses):
            if visited[value] != 2:
                return False

        return True