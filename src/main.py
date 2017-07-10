import re
import sys

###############################################################################
# File
###############################################################################
def loadFile(filename):
    return open(filename, 'r').read()

def toLines(value):
    return value.split('\n')

###############################################################################
# Title
###############################################################################
def Title(title, intent):
    return {
        'value' : title,
        'intent': intent
    }

def isHash(value):
    return value == '#'

def getTitles(i, lines, titles):
    if i == len(lines):
        return titles
    return getTitles(i + 1, lines, addTitle(lines[i], titles))

def addTitle(line, titles):
    if len(line) > 0 and isHash(line[0]):
        titles.append(Title(line, getIntentLevel(0, line)))
    return titles

def getIntentLevel(intent, line):
    if(isHash(line[intent])):
        return getIntentLevel(intent + 1, line)
    return intent

###############################################################################
# Content
###############################################################################
def prepareContentTable():


def main(argv):
    titles =  getTitles(0, toLines(loadFile('../res/markdown.md')), [])
    print titles

if __name__ == "__main__":
    main(sys.argv)