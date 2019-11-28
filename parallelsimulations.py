import threading
import time
import os
import sys

try:
    # check args
    if len(sys.argv) != 2:
        print("Invalid arguments: Please put SUT as first argument")
    aliveMutants = []
    killedMutants = []
    # redirect stdout to file
    sys.stdout = open('parallel-mutant-generated-output.txt', 'w')

    # store all filenames of mutants folder in files list
    files = os.listdir("mutants")

    # write the correct answer on first line of the file
    # print("Expected value the software under test: ")
    exec(open(sys.argv[1]).read())
    # print("\n")

    # write the name of file then the output of the script
    for file in files:
        print("Actual value of the mutant file: " + file)
        exec(open("mutants/" + file).read())
    
    # redirect stdout back to normal
    sys.stdout = sys.__stdout__

    # store in list all lines
    with open("parallel-mutant-generated-output.txt") as f1:
        lines = f1.readlines()

    # remove '\n' chars from list
    for i in range(0, len(lines)):
        lines[i] = lines[i].replace('\n', '')

    rightAnswer = lines[0]

    # iterate through every second line to check if mutant killed or still alive
    
    

except IOError:
    type, value, traceback = sys.exc_info()
    print('Error opening %s: %s' % (value.filename, value.strerror))
    print("Error with file")


def threadingloop(l): 

    
        if  l != float(rightAnswer):
            # print("Killed Mutant", lines[i])
            killedMutants.append(l)
        else:
            # print("Mutant Alive", lines[i])
            aliveMutants.append(l)


for l in (0, len(lines), 6):
    try: 
        t1 = threading.Thread(target=threadingloop, args=[lines[l]])
        t2 = threading.Thread(target=threadingloop, args=[lines[l+2]])
        t3 = threading.Thread(target=threadingloop, args=[lines[l+4]])
    
        
        t1.start()
        t2.start()
        t3.start()
    except IndexError as error:

        print("Killed Mutants")
        print(killedMutants)

        print("Alive Mutants")
        print(aliveMutants)

        output = open("parallel-mutant-generated-output.txt", 'a')

        percentage = len(killedMutants) / (len(killedMutants) + len(aliveMutants))
        output.write("Mutants killed: %d\n" %len(killedMutants))
        output.write("Mutants alive: %d\n" %len(aliveMutants))
        output.write("Percentage of mutants killed: %d" %len(killedMutants) + "/ %d" %(len(killedMutants) + len(aliveMutants)) + "= %f" %percentage)
        output.close()


