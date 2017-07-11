import sys

def Title(title, original,intent):
    return {
        'value' : title,
        'intent': intent,
        'original': original
    }

def isHash(value):
    return value == '#'

def isSpace(value):
    return value == ' '

def validateHash(value):
    return isHash(value) or isSpace(value)

def inc(i):
    return i + 1

def getTitles(i, lines, titles):
    if i == len(lines):
        return titles
    return getTitles(inc(i), lines, addTitle(lines[i], titles))

def addTitle(line, titles):
    if len(line) > 0 and isHash(line[0]):
        titles.append(Title(removeHash(line), line, getIntentLevel(0, line)))
    return titles

def getIntentLevel(intent, line):
    if isHash(line[intent]):
        return getIntentLevel(inc(intent), line)
    return intent

def removeHash(line):
    if validateHash(line[0]):
        line = removeHash(line[1:])
    return line
