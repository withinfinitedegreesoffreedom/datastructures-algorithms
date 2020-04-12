
# write a function to check if there is route between tow given nodes in a directed graph

import unittest
from collections import defaultdict

# Graph class
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if u not in self.nodes:
            self.nodes.append(u)
        if v not in self.nodes:
            self.nodes.append(v)

# bfs solution for graph traversal
def has_route(graph, src, dest):
    visited = dict.fromkeys(graph.nodes, False)
    queue = []
    queue.append(src)
    visited[src] = True
    has_route = False

    while queue:
        to_explore = queue.pop(0)

        for node in graph.graph[to_explore]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                if node == dest:
                    has_route = True
                    return has_route
    return has_route

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
        return g

    def test_has_route(self):
        g = self.gen_graph()
        self.assertTrue(has_route(g, 'A', 'H'))
        self.assertFalse(has_route(g, 'F', 'H'))
        self.assertFalse(has_route(g, 'D', 'E'))
        self.assertTrue(has_route(g, 'B', 'F'))
        self.assertFalse(has_route(g, 'C', 'A'))

if __name__=="__main__":
    unittest.main()