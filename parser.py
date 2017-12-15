#!/usr/bin/python3
# parser.py


def parse(text):
    lines = str(text).splitlines()
    while("" in lines):
        lines.remove("")
    words = []
    for l in lines:
        row = str(l).split(" ")
        while("" in row):
            row.remove("")
        word = {"id":int(row[0]),"head":int(row[6]),"form":row[1]}
        words.append(word)
    return words
