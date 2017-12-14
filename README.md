# CoNLL-U_cycles
## Summary
This program takes a CoNLL-U file and finds dependency cycles in its dependency graph.

## What is a dependency cycle?

A dependency cycle occurs when node N depends on the value of node N, either indirectly through a chain of dependencies that loop back or directly by listing itself as a dependency.

## Running

```bash
python3 main.py file.txt
```

This will parse a file.txt in the conllu format, and list cycles.