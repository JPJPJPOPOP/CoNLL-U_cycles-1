#!/usr/bin/python3
# parser.py

def parse(text):
    lines=str(text).splitlines()
    while("" in lines):
            lines.remove("")
    words=[]
    for l in lines:
        row=str(l).split(" ")
        while("" in row):
            row.remove("")
        word=dict()
        word["head"]=int(row[0])
        word["id"]=int(row[6])
        word["token"]=row[1]
        word["normalized"]=row[2]
        words.append(word)
    return [words]