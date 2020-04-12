
import unittest
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)
        if u not in self.nodes:
            self.nodes.append(u)
        if v not in self.nodes:
            self.nodes.append(v)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        list_of_edges = []
        for key, value in self.graph.items():
            for node in value:
                list_of_edges.append((key, node))
        return list_of_edges

    def bfs(self, start_node):
        visited = dict.fromkeys(self.get_nodes(), False)
        queue = []
        queue.append(start_node)
        visited[start_node] = True
        traversal = str(start_node) + "-"

        while queue:
            next_node = queue.pop(0)

            for i, node in enumerate(self.graph[next_node]):
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    traversal += str(node) + "-"
        return traversal

    def dfs(self, start_node):
        visited = dict.fromkeys(self.graph.keys(), False)

        stack = []
        stack.append(start_node)

        traversal = ""

        while stack:
            s = stack[-1]
            stack.pop()

            if not visited[s]:
                visited[s] = True
                traversal += str(s) + "-"

            for node in self.graph[s]:
                if not visited[node]:
                    stack.append(node)
        return traversal

class Test(unittest.TestCase):
    def gen_graph(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('A', 'D')
        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        g.add_edge('B', 'E')
        g.add_edge('B', 'F')
        g.add_edge('C', 'G')
        g.add_edge('E', 'F')
        g.add_edge('G', 'H')
        '''g = Graph()
        g.addEdge(1, 0)
        g.addEdge(0, 2)  
        g.addEdge(2, 1)  
        g.addEdge(0, 3)  
        g.addEdge(1, 4)'''
        return g

    def test_get_nodes(self):
        g = self.gen_graph()
        print(g.get_nodes())
        #self.assertListEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], g.get_nodes())

    def test_get_edges(self):
        g = self.gen_graph()
        print(g.get_edges())
        #self.assertSetEqual({('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'G'), ('E', 'F'), ('G', 'H')}, set(g.get_edges()))

    def test_bfs(self):
        g = self.gen_graph()
        print(g.bfs('C'))
        #self.assertEqual('A-B-C-D-E-F-G-H-', g.bfs('A'))

    def test_dfs(self):
        g = self.gen_graph()
        print(g.dfs('B'))

if __name__=="__main__":
    unittest.main()
    





        



        
        


        

