class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make the adjaceny list
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites :
            preMap[crs].append(pre)

        #visit set to store all courses along current dfs path
        visitSet = set()

        def dfs(crs) :
            #base case
            if crs in visitSet :
                #detected a loop so false
                return False
            #base case
            #no pre reqs
            if preMap[crs] == [] :
                return True
            
            visitSet.add(crs)
            #recursively run dfs on this courses pre reqs
            for pre in preMap[crs] :
                if not dfs(pre) :
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses) :
            if not dfs(crs) :
                return False
        return True