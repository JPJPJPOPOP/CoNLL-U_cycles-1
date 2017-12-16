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
id_to_word = dict()
for word in data:
    g.add_edge(word['id'], word['head'])
    id_to_word[word['id']] = word["form"]

print("Has Cycles:")
print(g.is_cyclic())
if g.is_cyclic():
    print("Cycle List:")
    c_list = g.cycle_list()
    for cycle in c_list:
        print(cycle)
        word_form = []
        for i in cycle:
            word_form.append(id_to_word[i])
        print("-->".join(word_form) + "-->")
