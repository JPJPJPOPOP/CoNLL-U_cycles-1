#!/usr/bin/python3
# main.py
import sys
from parser import parse
from graph import Graph

if len(sys.argv) != 2:
    raise ValueError(
        'Invalid Input, must be given a file which is in the CoNLL-U format')

data = parse(open(sys.argv[1], 'r').read())
g = Graph(len(data) + 1)
for word in data:
    g.add_edge(word['id'], word['head'])

print("Has Cycles:")
print(g.is_cyclic())
print("Cycle List:")
print(g.cycle_list())
