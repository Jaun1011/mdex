import re
import sys

def loadFile(filename):
    return open(filename, 'r').read()

def toLines(value):
    return value.split('\n')