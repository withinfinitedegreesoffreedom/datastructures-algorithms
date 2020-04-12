
import unittest

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def get_nodes(self):
        return list(self.graph.keys())


def get_build_order(g):
    nodes =  list(g.keys())
    build_order = []
    #while (set(nodes) - set([item for sublist in g.graph.values() for item in sublist])):
    while g:
        nodes_with_no_incoming_links = set(nodes) - set([item for sublist in g.values() for item in sublist])
        if g and len(nodes_with_no_incoming_links)==0:
            raise ValueError("Cycle")

        build_order.extend(nodes_with_no_incoming_links)
        for node in nodes_with_no_incoming_links:
            g.pop(node)
            nodes.remove(node)
    return build_order

def build_order_driver(projects, dependencies):
    if projects and dependencies:
        g = dict()
        for project in projects:
            g[project] = []
        for prev, after in dependencies:
            g[prev].extend(after)
    return get_build_order(g)

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
print(build_order_driver(projects, dependencies))
