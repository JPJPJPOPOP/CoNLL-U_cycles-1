#!/usr/bin/python3
# graph.py
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.verticies = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # internal
    def _is_cyclic_util(self, start_vertex):
        current_vertex=start_vertex+0
        visited=[current_vertex]
        while len(self.graph[current_vertex])>0 and not(self.graph[current_vertex][0]==start_vertex):
            current_vertex=self.graph[current_vertex][0]
            visited.append(current_vertex+0)
        if len(self.graph[current_vertex])>0:
            return [visited]
        return []

    # rotates cycle so it starts with smallest id
    def normalize_cycle(self, a):
        b = list(a)
        b.sort()
        loc = a.index(b[0])
        g = [0] * len(a)
        for x in range(0, len(a)):
            g[x - loc] = a[x]
        return g

    # returns existing cycles in the form of lists of node ids which are in a cycle
    def cycle_list(self):
        cycles = []
        for node in range(self.verticies):
            c_datas = self._is_cyclic_util(node)
            for c_data in c_datas:
                if len(c_data) > 0:
                    c_data = self.normalize_cycle(c_data)
                    if(not(c_data in cycles)):
                        cycles.append(c_data)

        return cycles

    # checks if graph has cycles
    def is_cyclic(self):
        return len(self.cycle_list()) > 0
