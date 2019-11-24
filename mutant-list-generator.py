#!/usr/bin/python

import sys

newLines = []
lineNumberCount = 1

if len(sys.argv) != 2:
    print("Invalid arguments: Please put SUT as second argument")
    sys.exit()

print('Generating Mutant List for:', str(sys.argv[1]))
newLines.append("Library of Mutants\n\n")
newLines.append("Line\t\tMutant\n")

with open(str(sys.argv[1])) as f:
    lines = f.readlines()

    for line in lines:
        if "/" in line or "+" in line or "-" in line or "=" in line or "*" in line:
            newLines.append(str(lineNumberCount) +  "\t\t" + str(line))
        lineNumberCount+=1

    # lines = [l for l in lines if "/" in l]
    with open("library-of-mutants.txt", "w") as f1:
        f1.writelines(newLines)
