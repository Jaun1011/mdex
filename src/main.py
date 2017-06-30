import re

def main()
    value = loadFile("../res/markdown.md")
    lines = toLines(value)
    res = null
    for line in lines:
        title = getTitle(line)
        if not title:
            res.append(title)
    print res

def loadFile(filename):
    f = open(filename, "r")
    return f.read()

def toLines(value):
    return value.split('\n', 1 )

def getTitle(line):
    if len(line) > 0 and line[0] == '#':
        return line
    return False

if __name__ == "__main__":
    main()
