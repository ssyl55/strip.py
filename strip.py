#!/usr/bin/env python

"""
Python Script to strip trailing whitespace at the end of lines in files

AUTHOR: Stephen Liu
DATE:   03/03/16
"""

import sys

def findTrailingWhitespace(line):
    start = 0
    wlength = 0
    index = len(line) - 1

    if index > 0:
        while line[index] == '\n' or line[index] == ' ' or line[index] == '\t':
            if line[index] == ' ' or line[index] == '\t':
                wlength = wlength + 1
            index = index - 1
            if index < 0:
                break
        start = (len(line) - 1) - wlength
    else:
        start = 0

    return start


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for f in range(1, len(sys.argv)):
            lines = []
            file = open(sys.argv[f], 'r')

            print "Opening file: " + str(file)
            for line in file:
                if len(line) > 0:
                    start = findTrailingWhitespace(line)
                    print (line, len(line), line[start])
                    lines.append(line[:start] + line[len(line) - 1])
                else:
                    lines.append(line)
            file.close()

            with open(sys.argv[f], 'w') as file:
                file.writelines(lines)
            file.close()
    else:
        print "Error: Must include at least one filename as an argument."
