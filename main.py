#!/usr/bin/python3
# main.py
import sys
from parser import parse
from graph import Graph

if len(sys.argv) != 2:
    raise ValueError(
        'Invalid Input, must be given a file which is in the CoNLL-U format')

data = parse(open(sys.argv[1], 'r').read())
print(data)
g = Graph(len(data[0]) + 1)
for word in data[0]:
    print(word['head'], " ", word['id'])
    g.add_edge(word['head'], word['id'])

print("Has Cycles:")
print(g.is_cyclic())
print("Cycle List:")
print(g.cycle_list())
