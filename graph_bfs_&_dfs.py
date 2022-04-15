# BFS Algorithm implementation


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    
    def bfs(self, startNode):
        # visited = [False] * self.graph_dict   #if its graph_dict have int keys
        visited = {}
        queue = []
        path = []
        visited[startNode] = True
        queue.append(startNode)

        while queue:
            startNode = queue.pop(0)
            path.append(startNode)

            for i in self.graph_dict:
                # if visited[i] == False:   #if its graph_dict have int keys
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
        return path

    def dfs(self, start):
        stack = [start]
        path = []
        while stack:
            v = stack.pop()
            if v in path:
                continue
            path.append(v)
            for i in self.graph_dict[v]:
                stack.append(i)

        return path

        
routes = [
    ('mumbai','paris'),
    ('mumbai','dubai'),
    ('paris','dubai'),
    ('paris','newyork'),
    ('dubai','paris'),
    ('dubai','newyork'),
    ('newyork','torrento'),
    ('torrento','newyork'),
    ]


g = Graph(routes)

result = g.bfs('mumbai')
print('BFS :', result)

result2 = g.dfs('mumbai')
print('DFS :', result2)


