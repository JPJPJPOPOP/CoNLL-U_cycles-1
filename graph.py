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
    def _is_cyclic_util(self, current_vertex, visits_p, start_vertex):
        visits = list(visits_p)
        visits[current_vertex] += 1
        bads = []
        if visits[current_vertex] > 1:
            if current_vertex == start_vertex:
                return [[current_vertex]]
            return []
        for neighbor in self.graph[current_vertex]:
            cyclic_data = self._is_cyclic_util(neighbor, visits, start_vertex)
            for bad in cyclic_data:
                if current_vertex in bad:
                    bad.remove(current_vertex)
                b = [current_vertex] + bad
                if not(b in bads):
                    bads.append(b)
        return bads

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
            rec = [0] * self.verticies
            c_datas = self._is_cyclic_util(node, rec, node)
            for c_data in c_datas:
                if len(c_data) > 0:
                    c_data = self.normalize_cycle(c_data)
                    if(not(c_data in cycles)):
                        cycles.append(c_data)

        return cycles

    # checks if graph has cycles
    def is_cyclic(self):
        return len(self.cycle_list()) > 0
