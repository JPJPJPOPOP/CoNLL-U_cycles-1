#!/usr/bin/python3
# main.py
import sys
from conllu.parser import parse
from graph import Graph

if len(sys.argv) != 2:
    raise Exception('Invalid Input')
data = parse(open(sys.argv[1], 'r').read())
print(data)
g = Graph(len(data[0])+1)
# head_to_tail = {}
for word in data[0]:
    print(word['head'], " ", word['id'])
    g.add_edge(word['head'], word['id'])
print(g.is_cyclic())
#     if (word['head'] in head_to_tail):
#         head_to_tail[word['head']].append(word['id'])
#     else:
#         head_to_tail[word['head']] = [word['id']]
# #    head_to_tail[word['head']] = head_to_tail[word['head']].append(word['id'])
#     #print(head)
# print(head_to_tail)
