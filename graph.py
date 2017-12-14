#!/usr/bin/python3
# graph.py
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
    #internal
    def is_cyclic_util(self, v, visits_p,n):
        visits=list(visits_p)
        visits[v] +=1
        bads=[]
        if(visits[v]>1):
            if(not(v==n)):
                visits[v] +=-1
                return []
            return [[v]]
            bads.append(v)
        for neighbor in self.graph[v]:
            cyclic_data=self.is_cyclic_util(neighbor, visits,n)
            if len(cyclic_data)>0:
                for bad in cyclic_data:
                    if(v in bad):
                        bad.remove(v)
                    b=[v]+bad
                    if(not(b in bads)):
                        bads.append(b)

        return bads
    
    def normalize_cycle(self,a):
        b=list(a)
        b.sort()
        loc=a.index(b[0])
        g=[0]*len(a)
        for x in range(0,len(a)):
            g[x-loc]=a[x]
        return g
    #returns existing cycles in the form of lists of node ids which are in a cycle
    def cycle_list(self):
        cycles=[]
        visits= [0] * self.V
        for node in range(self.V):
            if visits[node]<1:
                rec= [0] * self.V
                c_datas=self.is_cyclic_util(node, rec,node)
                for c_data in c_datas:
                    if(len(c_data)>0):
                        c_data=self.normalize_cycle(c_data)
                        if(not(c_data in cycles)):
                            cycles.append(c_data)
        
        return cycles
    #checks if graph has cycles
    def is_cyclic(self):  
        return len(self.cycle_list())>0
