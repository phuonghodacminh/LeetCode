class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        k = len(queries)
        m = len(grid)
        n = len(grid[0])
        hashmap = {}
        sorted_queries = sorted(queries)
        idx = 0
        check = True
        for i in range(k):
            hashmap[sorted_queries[i]] = 0
            if sorted_queries[i] > grid[0][0] and check:
                idx = i
                check = False
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = {}
        leftover = deque()
        q = deque()
        q.append((0, 0))
        total_sum = 0
        while len(q) and idx < k:
            x, y = q.popleft()
            if grid[x][y] < sorted_queries[idx]:
                visited[(x, y)] = True
                total_sum += 1
                for i in range(4):
                    new_x = x + direction[i][0]
                    new_y = y + direction[i][1]
                    if new_x >=0 and new_y >= 0 and new_x < m and new_y < n and ((new_x, new_y) not in visited or not visited[(new_x, new_y)]):
                        q.append((new_x, new_y))
                        visited[(new_x, new_y)] = True
            else:
                leftover.append((x, y))
            
            if not len(q):
                if not len(leftover):
                    hashmap[sorted_queries[idx]] = total_sum
                    break
                else:
                    if idx < k:
                        hashmap[sorted_queries[idx]] = total_sum
                        curr = sorted_queries[idx]

                        while sorted_queries[idx] == curr:
                            idx += 1
                            if idx == k:
                                break

                        while leftover:
                            q.append(leftover.popleft())
                    else:
                        break
        
        while idx < k:
            hashmap[sorted_queries[idx]] = total_sum
            idx += 1

        result = []
        for i in queries:
            result.append(hashmap[i])

        return result


        
