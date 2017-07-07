import re
import sys


def loadFile(filename):
    return open(filename, "r").read()

def toLines(value):
    return value.split('\n')

def addTitle(line, titles):
    if len(line) > 0 and line[0] == '#':
        titles.append(line)
    return titles

def getTitles(lines, titles):
    if not lines:
        return titles
    titles = addTitle(lines[0], titles)
    lines.pop(0)
    return getTitles(lines, titles)

def main(argv):
    content = loadFile('../res/markdown.md')
    lines = toLines(content)
    print getTitles(lines[:], [])

if __name__ == "__main__":
    main(sys.argv)
