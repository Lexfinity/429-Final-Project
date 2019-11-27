import os
import sys

try:
    # check args
    if len(sys.argv) != 2:
        print("Invalid arguments: Please put SUT as first argument")
    aliveMutants = []
    killedMutants = []
    # redirect stdout to file
    sys.stdout = open('mutant-generated-output.txt', 'w')

    # store all filenames of mutants folder in files list
    files = os.listdir("mutants")

    # write the correct answer on first line of the file
    exec(open(sys.argv[1]).read())

    # write the name of file then the output of the script
    for file in files:
        print(file)
        exec(open("mutants/" + file).read())
    
    # redirect stdout back to normal
    sys.stdout = sys.__stdout__

    # store in list all lines
    with open("mutant-generated-output.txt") as f1:
        lines = f1.readlines()

    # remove '\n' chars from list
    for i in range(0, len(lines)):
        lines[i] = lines[i].replace('\n', '')

    rightAnswer = lines[0]

    # iterate through every second line to check if mutant killed or still alive
    for i in range(1, len(lines), 2):
        if int(lines[i + 1]) == int(rightAnswer):
            # print("Killed Mutant", lines[i])
            killedMutants.append(lines[i])
        else:
            # print("Mutant Alive", lines[i])
            aliveMutants.append(lines[i])

    print("Killed Mutants")
    print(killedMutants)

    print("Alive Mutants")
    print(aliveMutants)

except IOError:
    type, value, traceback = sys.exc_info()
    print('Error opening %s: %s' % (value.filename, value.strerror))
    print("Error with file")
