#!/usr/bin/python

import sys
temp = []
if len(sys.argv) != 3:
    print("Invalid arguments: Please put SUT as first argument and mutants as second")
    sys.exit()

print("Generating Mutant files for:"), str(sys.argv[1]), "and ", str(sys.argv[1])

try:
    SUTLineNumber = 1
    mutantLineNumber = 1

    with open(str(sys.argv[2])) as f1:
        MutantLines = f1.readlines()

    with open(str(sys.argv[1])) as f2:
        SUTlines = f2.readlines()

    for MutantLine in MutantLines:
        lineNumberToInject = MutantLine[:MutantLine.find('\t\t')]
        temp = []
        temp = list(SUTlines)
        # print(temp)

        newLine1 = temp[int(lineNumberToInject) - 1]
        # print(newLine1)
        newLine2 = newLine1[:newLine1.find('=') + 1]
        # print(newLine2)
        newLine3 = newLine2 + ' ' + MutantLine[MutantLine.find('\t\t') :].strip()
        # print(newLine3)
  
        # [.find('='):] + MutantLine[MutantLine.find('\t\t') + 1:]
        # print(newLine)
        temp[int(lineNumberToInject) - 1] = newLine3 + '\n'
                
        with open(str(mutantLineNumber) + str(SUTLineNumber) + ".py", "w") as f1:
            f1.writelines(temp)   
            SUTLineNumber += 1
        mutantLineNumber += 1

except IOError:
    type, value, traceback = sys.exc_info()
    print('Error opening %s: %s' % (value.filename, value.strerror))
    print("Error with file")
    # sys.exit()