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
        word = dict()
        word["id"] = int(row[0])
        word["head"] = int(row[6])
        words.append(word)
    return [words]
