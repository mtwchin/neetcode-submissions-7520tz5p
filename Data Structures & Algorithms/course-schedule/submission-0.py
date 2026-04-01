class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course initially we want to map to empty list
        prev_map = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prev_map[crs].append(pre)
        # visited set will store all courses along the current 
        visited_path = set()
        def dfs(crs):
            if crs in visited_path:
                return False
            # course with no pre-reqs
            if prev_map[crs] == []:
                return True
            visited_path.add(crs)
            for pre in prev_map[crs]:
                if not dfs(pre): # if false, we can return false for the entire function
                    return False
            visited_path.remove(crs)
            # prev_map[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                