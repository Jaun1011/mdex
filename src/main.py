import sys

import file
import titleparser

def main(argv):
    content = file.loadFile('../README.md')
    lines = file.toLines(content)
    print titleparser.getTitles(0,lines,[])

if __name__ == "__main__":
    main(sys.argv)